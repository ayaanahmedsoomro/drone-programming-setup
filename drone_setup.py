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
        msg = "Python 3.6+ is required."
        show_popup("Python Error", msg)
        sys.exit(msg)

    if platform.system() != "Linux":
        msg = "Only Linux or WSL is supported."
        show_popup("OS Error", msg)
        sys.exit(msg)

    try:
        urllib.request.urlopen("https://github.com", timeout=5)
    except:
        msg = "No internet connection detected."
        show_popup("Network Error", msg)
        sys.exit(msg)

def configure_git():
    run_cmd('git config --global url."https://github.com/".insteadOf git@github.com:')
    run_cmd('git config --global url."https://".insteadOf git://')

def clone_and_setup_ardupilot():
    run_cmd("git clone https://github.com/ArduPilot/ardupilot.git ~/ardupilot")
    run_cmd("cd ~/ardupilot && git submodule update --init --recursive")
    run_cmd("cd ~/ardupilot/Tools/environment_install && ./install-prereqs-ubuntu.sh -y")

    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "a") as f:
        f.write("\n# ArduPilot Paths\n")
        f.write("export PATH=$PATH:$HOME/.local/bin\n")
        f.write("export PATH=$PATH:$HOME/ardupilot\n")
        f.write("export PATH=$PATH:$HOME/ardupilot/Tools/autotest\n")

def install_python_libraries():
    run_cmd("pip3 install --upgrade pip")
    run_cmd("pip3 install pymavlink MAVProxy dronekit pyproj shapely")

def setup_sim_environment():
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
    print("🔧 Drone Programming Environment Installer")
    check_requirements()
    configure_git()
    clone_and_setup_ardupilot()
    install_python_libraries()
    setup_sim_environment()

    print("\n✅ Setup complete!")
    print("▶ To run simulation:")
    print("   cd ~/ardu-sim && ./ardu-sim.sh")
    print("▶ Then open a new terminal and run:")
    print("   mavproxy.py --master 127.0.0.1:14550")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        show_popup("Command Error", f"❌ Failed: {e.cmd}")
        sys.exit(f"Command failed: {e.cmd}")
    except Exception as e:
        show_popup("Script Error", f"❌ {str(e)}")
        sys.exit(str(e))
