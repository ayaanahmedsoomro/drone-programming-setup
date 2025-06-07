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
<br>
<code>git clone https://github.com/ayaanahmedsoomro/drone-programming-setup.git</code>
<br>
<code>cd drone-programming-setup</code>

2) Run root-level installs
<br>
<code>sudo bash install_sudo_packages.sh</code>

3) Run user-level setup
<br>
<code>python3 drone_setup.py</code>

4) Start simulation
<br>
<code>cd ~/ardu-sim</code>
<br>
<code>./ardu-sim.sh</code>

5) Open MAVProxy (new terminal)
<br>
<code>mavproxy.py --master 127.0.0.1:14550</code>