# Drone Programming Installation Setup
<br>
Installing Ubuntu and Preparing Environment for Drone Programming
To begin drone programming using MAVProxy and ArduPilot, follow these steps to set up
<br>
Ubuntu on Windows using WSL (Windows Subsystem for Linux):

### Step 1: Enable WSL on Windows
1) Open "Turn Windows features on or off" from the Start menu.
2) In the list, find and check the box for "Windows Subsystem for Linux".
3) Click OK, and when prompted, restart your computer.

### Step 2: Install Ubuntu from Microsoft Store
1) Open the Microsoft Store.
2) Search for Ubuntu.
3) Select the latest version: Ubuntu 22.04.5 LTS.
4) Click Install.
5) After installation, launch Ubuntu and create your Linux username and password.

### Step 3: Environment & Simulation Setup in Ubuntu

1) Clone the project
git clone https://github.com/ayaanahmedsoomro/drone-programming-setup.git
cd drone-programming-setup

2) Run root-level installs
sudo bash install_sudo_packages.sh

3) Run user-level setup
python3 drone_setup.py

4) Start simulation
cd ~/ardu-sim
./ardu-sim.sh

5) Open MAVProxy (new terminal)
mavproxy.py --master 127.0.0.1:14550