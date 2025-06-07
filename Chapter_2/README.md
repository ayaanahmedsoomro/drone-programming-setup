<h2>Arming and Disarming the Drone</h2>
<br>

<h4>What is Arming and Disarming?</h4>
<p><strong>Arming</strong> turns <strong>ON</strong> the drone’s motors and makes it ready for flight.<br>
<strong>Disarming</strong> turns <strong>OFF</strong> the motors, stopping the drone from flying.</p>

<h3>Step-by-Step Guide</h3>
<ul>
  <li><strong>Step 1: Arm the Vehicle</strong>
    <pre><code>arm throttle</code></pre>
    <p>This command prepares the motors for flight.<br>
    You will see a confirmation like <code>ARMING MOTORS</code>.</p>
  </li>

  <li><strong>Step 2: Check Default Disarm Delay</strong>
    <pre><code>param show DISARM_DELAY</code></pre>
    <p>This shows how many seconds the drone waits before disarming automatically.</p>
  </li>

  <li><strong>Step 3: Set Custom Disarm Delay</strong>
    <pre><code>param set DISARM_DELAY 10</code></pre>
    <p>This sets the delay to 10 seconds.<br>
    After being idle for 10 seconds, the drone will auto-disarm.</p>
  </li>
</ul>

<h3>Useful MAVProxy Options During Arming</h3>
<ul>
  <li><code>--console</code>: Opens a command-line interface for drone telemetry.</li>
  <img src="assets/chp3_i.png">
  <li><code>--map</code>: Opens a visual map showing your drone’s position.</li>
</ul>

<p>These options are typically included when launching the simulation like:</p>
<pre><code>mavproxy.py --console --map</code></pre>
