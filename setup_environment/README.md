<h1>Drone Programming Installation Setup</h1>
<br>
<h4>Installing Ubuntu and Preparing Environment for Drone Programming</h4>
<p>To begin drone programming using <strong>MAVProxy</strong> and <strong>ArduPilot</strong>, follow these steps to set up Ubuntu on Windows using <strong>WSL (Windows Subsystem for Linux)</strong>:</p>

<h3>Step 1: Enable WSL on Windows</h3>
<ul>
  <li>Open <strong>"Turn Windows features on or off"</strong> from the Start menu.</li>
  <li>In the list, find and check the box for <strong>Windows Subsystem for Linux</strong>.</li>
  <li>Click OK, and when prompted, restart your computer.</li>
</ul>

<h3>Step 2: Install Ubuntu from Microsoft Store</h3>
<ul>
  <li>Open the <strong>Microsoft Store</strong>.</li>
  <li>Search for <strong>Ubuntu</strong>.</li>
  <li>Select the latest version: <code>Ubuntu 22.04.5 LTS</code>.</li>
  <li>Click <strong>Install</strong>.</li>
  <li>After installation, launch Ubuntu and create your Linux username and password.</li>
</ul>

<h3>Step 3: Environment & Simulation Setup in Ubuntu</h3>
<ul>
  <li><strong>Clone the project</strong>
    <pre><code>git clone https://github.com/ayaanahmedsoomro/drone-programming-setup.git</code></pre>
    <pre><code>cd drone-programming-setup</code></pre>
  </li>
  <li><strong>Run root-level installs</strong>
    <pre><code>sudo bash install_sudo_packages.sh</code></pre>
  </li>
  <li><strong>Run user-level setup</strong>
    <pre><code>python3 drone_setup.py</code></pre>
  </li>
  <li><strong>Start simulation</strong>
    <pre><code>cd ~/ardu-sim</code></pre>
    <pre><code>./ardu-sim.sh</code></pre>
  </li>
  <li><strong>Open MAVProxy (in new terminal)</strong>
    <pre><code>mavproxy.py --master 127.0.0.1:14550</code></pre>
  </li>
</ul>
