import os
import sys
import subprocess
import platform
import urllib.request

# Optional GUI message (fallback if Tkinter exists)
def show_popup(title, message):
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(title, message)
    except:
        print(f"\n[POPUP Fallback] {title}: {message}")

def run_cmd(command, sudo=False):
    if sudo and os.geteuid() != 0:
        command = f"sudo {command}"
    print(f"\n>>> Running: {command}")
    subprocess.run(command, shell=True, check=True)

def check_requirements():
    print("\n=== Checking system requirements ===")
    
    # Python version
    if sys.version_info < (3, 6):
        msg = "Python 3.6 or higher is required. Please upgrade your Python."
        show_popup("Python Version Error", msg)
        sys.exit(msg)

    # OS type
    if platform.system() not in ["Linux"]:
        msg = "This script is intended for Linux (including WSL)."
        show_popup("Unsupported OS", msg)
        sys.exit(msg)

    # Internet check
    try:
        urllib.request.urlopen("https://github.com", timeout=5)
    except:
        msg = "Internet not detected. Please check your connection or firewall/NAT settings."
        show_popup("Network Error", msg)
        sys.exit(msg)

def install_system_packages():
    print("\n=== Installing required system packages ===")
    run_cmd("apt-get update && apt-get upgrade -y", sudo=True)
    run_cmd("apt-get install -y git gitk git-gui screen nano", sudo=True)
    run_cmd("apt-get install -y python3 python3-pip python3-opencv", sudo=True)
    run_cmd("apt-get install -y libtool libxml2-dev pkg-config python3-matplotlib python3-dev python3-numpy", sudo=True)
    run_cmd("apt-get install -y python3-pygame python3-lxml", sudo=True)
    run_cmd("apt-get install -y python3-setuptools python3-wheel", sudo=True)

def configure_git():
    print("\n=== Configuring Git ===")
    run_cmd('git config --global url."https://github.com/".insteadOf git@github.com:')
    run_cmd('git config --global url."https://".insteadOf git://')

def clone_and_setup_ardupilot():
    print("\n=== Cloning ArduPilot and running setup ===")
    run_cmd("git clone https://github.com/ArduPilot/ardupilot.git ~/ardupilot")
    run_cmd("cd ~/ardupilot && git submodule update --init --recursive")
    run_cmd("cd ~/ardupilot/Tools/environment_install && ./install-prereqs-ubuntu.sh -y", sudo=True)

    # Add to bashrc
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "a") as f:
        f.write("\n# Drone Programming Environment Setup\n")
        f.write("export PATH=$PATH:$HOME/.local/bin\n")
        f.write("export PATH=$PATH:$HOME/ardupilot/Tools/autotest\n")
        f.write("export PATH=$PATH:$HOME/ardupilot\n")

def install_python_modules():
    print("\n=== Installing Python libraries ===")
    run_cmd("pip3 install pymavlink MAVProxy dronekit pyproj shapely")

def setup_sim_environment():
    print("\n=== Setting up simulation folder and shell script ===")
    run_cmd("mkdir -p ~/ardu-sim/parameters")
    run_cmd("cp -a ~/ardupilot/build/sitl/bin/. ~/ardu-sim/")
    run_cmd("cp ~/ardupilot/Tools/autotest/default_params/copter.parm ~/ardu-sim/parameters/copter.parm")
    run_cmd("cp ~/ardupilot/Tools/autotest/models/plane.parm ~/ardu-sim/parameters/plane.parm")
    run_cmd("cp ~/ardupilot/Tools/autotest/default_params/rover.parm ~/ardu-sim/parameters/rover.parm")
    run_cmd("cp ~/ardupilot/Tools/autotest/default_params/sub.parm ~/ardu-sim/parameters/sub.parm")

    # Create launcher script
    sim_script = os.path.expanduser("~/ardu-sim/ardu-sim.sh")
    with open(sim_script, "w") as f:
        f.write("""#!/bin/bash
screen -S vehicle -d -m bash -c "./arducopter -S --model + --speedup 1 --defaults parameters/copter.parm -I0"
screen -S proxy -d -m bash -c "mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550"
""")
    run_cmd(f"chmod +x {sim_script}")

def main():
    print("=== Drone Programming Auto Installer ===")
    check_requirements()
    install_system_packages()
    configure_git()
    clone_and_setup_ardupilot()
    install_python_modules()
    setup_sim_environment()
    
    print("\n✅ Installation Complete!")
    print("▶ To run simulation:")
    print("   cd ~/ardu-sim && ./ardu-sim.sh")
    print("▶ Then connect in new terminal:")
    print("   mavproxy.py --master 127.0.0.1:14550")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        msg = f"❌ Installation failed at command: {e.cmd}"
        show_popup("Command Error", msg)
        sys.exit(msg)
    except Exception as e:
        msg = f"❌ Unexpected error: {str(e)}"
        show_popup("Script Error", msg)
        sys.exit(msg)
