<h2>Telemetry Forwarding in MAVProxy</h2>
<br>

<h4>What is Telemetry Forwarding?</h4>
<p>Telemetry Forwarding allows real-time data from the drone (or simulation) to be shared across multiple terminals or computers. This is especially useful when:</p>
<ul>
  <li>Multiple users want to monitor the drone simultaneously.</li>
  <li>A backup connection is needed in case the primary connection fails.</li>
</ul>

<h4>Telemetry Data Includes:</h4>
<ul>
  <li><strong>Flight Mode:</strong> e.g., STABILIZE</li>
  <li><strong>Battery Level:</strong> e.g., 100%</li>
  <li><strong>Firmware Version:</strong> e.g., ArduCopter V4.7.0-dev</li>
  <li><strong>Frame Type:</strong> e.g., QUAD/PLUS</li>
  <li><strong>Parameters Received:</strong> e.g., 1349 total parameters</li>
</ul>

<h3>Steps to Use Telemetry Forwarding</h3>

<ul>
  <li><strong>Step 1: Start the Simulation</strong>
    <pre><code>cd ~/ardu-sim</code></pre>
    <pre><code>./ardu-sim.sh</code></pre>
    <p>This will launch the simulated drone and start a MAVProxy proxy in the background using <code>screen</code>.</p>
  </li>

  <li><strong>Step 2: Check Running Screens (Processes)</strong>
    <pre><code>screen -ls</code></pre>
    <p>This shows all active sessions, including your vehicle and proxy screens.</p>
  </li>

  <li><strong>Step 3: Connect to the Drone (Primary Connection)</strong>
    <pre><code>mavproxy.py --master=127.0.0.1:14550</code></pre>
    <p>This connects MAVProxy to the simulated drone.<br>You will see the telemetry data mentioned above.</p>
  </li>

  <li><strong>Step 4: Forward Telemetry to Additional Ports</strong>
    <pre><code>--out 127.0.0.1:10000 --out 127.0.0.1:20000</code></pre>
    <p>To test those additional ports, open two new terminals and run in each:</p>
    <pre><code>mavproxy.py --master=127.0.0.1:10000</code></pre>
    <pre><code>mavproxy.py --master=127.0.0.1:20000</code></pre>
  </li>
</ul>

<h3>Why Use Telemetry Forwarding?</h3>
<ul>
  <li><strong>Multiple Access:</strong> Several people can monitor or control the drone at the same time.</li>
  <li><strong>Redundancy:</strong> If one connection fails, others stay active.</li>
  <li><strong>Remote Monitoring:</strong> You can forward data to another machine over network/IP.</li>
</ul>
