import os
import sys
import subprocess
import urllib.request
import platform

def run_cmd(command):
    print(f"\n>>> {command}")
    subprocess.run(command, shell=True, check=True)

def show_popup(title, message):
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(title, message)
    except:
        print(f"\n[Popup] {title}: {message}")

def check_requirements():
    if sys.version_info < (3, 6):
        sys.exit("Python 3.6+ required.")
    if platform.system() != "Linux":
        sys.exit("Only Linux/WSL supported.")
    try:
        urllib.request.urlopen("https://github.com", timeout=5)
    except:
        sys.exit("No internet connection. Check network.")

def configure_git():
    run_cmd('git config --global url."https://github.com/".insteadOf git@github.com:')
    run_cmd('git config --global url."https://".insteadOf git://')

def clone_ardupilot():
    run_cmd("git clone https://github.com/ArduPilot/ardupilot.git ~/ardupilot")
    run_cmd("cd ~/ardupilot && git submodule update --init --recursive")

    with open(os.path.expanduser("~/.bashrc"), "a") as f:
        f.write("\n# ArduPilot PATHs\n")
        f.write("export PATH=$PATH:$HOME/.local/bin\n")
        f.write("export PATH=$PATH:$HOME/ardupilot\n")
        f.write("export PATH=$PATH:$HOME/ardupilot/Tools/autotest\n")

def install_python_libs():
    run_cmd("pip3 install --break-system-packages empy==3.3.4")
    run_cmd("pip3 install --break-system-packages pymavlink MAVProxy dronekit pyproj shapely")

def build_sitl():
    run_cmd("cd ~/ardupilot && ./waf configure --board sitl")
    run_cmd("cd ~/ardupilot && ./waf copter")

def setup_sim():
    run_cmd("mkdir -p ~/ardu-sim/parameters")
    run_cmd("cp -a ~/ardupilot/build/sitl/bin/. ~/ardu-sim/")
    run_cmd("cp ~/ardupilot/Tools/autotest/default_params/copter.parm ~/ardu-sim/parameters/copter.parm")
    run_cmd("cp ~/ardupilot/Tools/autotest/models/plane.parm ~/ardu-sim/parameters/plane.parm")
    run_cmd("cp ~/ardupilot/Tools/autotest/default_params/rover.parm ~/ardu-sim/parameters/rover.parm")
    run_cmd("cp ~/ardupilot/Tools/autotest/default_params/sub.parm ~/ardu-sim/parameters/sub.parm")

    sim_script = os.path.expanduser("~/ardu-sim/ardu-sim.sh")
    with open(sim_script, "w") as f:
        f.write("""#!/bin/bash
screen -S vehicle -d -m bash -c "./arducopter -S --model + --speedup 1 --defaults parameters/copter.parm -I0"
screen -S proxy -d -m bash -c "mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550"
""")
    run_cmd(f"chmod +x {sim_script}")

def main():
    print("🚀 Drone Programming Environment Setup Starting...")
    check_requirements()
    configure_git()
    clone_ardupilot()
    install_python_libs()
    build_sitl()
    setup_sim()

    print("\n✅ Setup complete!")
    print("▶ Run simulation: cd ~/ardu-sim && ./ardu-sim.sh")
    print("▶ In new terminal: mavproxy.py --master 127.0.0.1:14550")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        show_popup("Command Error", f"❌ Failed: {e.cmd}")
        sys.exit(f"Command failed: {e.cmd}")
    except Exception as e:
        show_popup("Script Error", f"❌ {str(e)}")
        sys.exit(str(e))
