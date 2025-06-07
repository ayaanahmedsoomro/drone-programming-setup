<h2>Mission Editor in MAVProxy</h2>
<br>

<h4>What is the Mission Editor?</h4>
<p>The <strong>Mission Editor</strong> allows you to define a set of waypoints for the drone to follow automatically. After uploading the mission, the drone flies from point to point using <strong>AUTO</strong> mode, and finally performs <strong>RTL (Return to Launch)</strong> if programmed.</p>

<h3>Step-by-Step Guide</h3>
<ul>
  <li><strong>Step 1: Load the Mission Editor</strong>
    <pre><code>module load misseditor</code></pre>
    <p>Opens the Mission Editor window.<br>
    You can click on the map to define waypoints (1, 2, 3…).</p>
  </li>

  <li><strong>Step 2: Set the Drone to AUTO Mode</strong>
    <pre><code>mode AUTO</code></pre>
    <p>The drone will now automatically follow the uploaded waypoints.<br>
    This mode allows fully autonomous flight along the path.</p>
  </li>
</ul>

<h3>Optional: Speed Up Simulation</h3>
<pre><code>param set SIM_SPEEDUP 5</code></pre>
<p>Increases simulation speed 5×.<br>
Useful for testing full missions faster.</p>
