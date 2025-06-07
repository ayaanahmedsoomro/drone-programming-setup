<h2>Geofencing in MAVProxy</h2>
<br>

<h4>What is Geofencing?</h4>
<p><strong>Geofencing</strong> is a safety feature that sets:</p>
<ul>
  <li>A horizontal boundary (radius) the drone cannot fly beyond.</li>
  <li>A maximum altitude (height) limit.</li>
</ul>
<p>If the drone crosses these boundaries, it will automatically trigger an <strong>RTL (Return to Launch)</strong> to return to its starting point.</p>

<h3>Part A: Set a Geofence Radius (Horizontal Boundary)</h3>
<h4>Step-by-Step Commands</h4>
<pre><code>arm throttle</code></pre>
<pre><code>mode GUIDED</code></pre>
<pre><code>takeoff 20</code></pre>
<pre><code>fence enable</code></pre>
<pre><code>param show FENCE_RADIUS</code></pre>
<p>This shows the current allowed flying radius.</p>

<pre><code>module load misseditor</code></pre>
<p>Add a waypoint outside the radius using Mission Editor.</p>
<pre><code>module unload misseditor</code></pre>

<pre><code>mode AUTO</code></pre>
<p>The drone will automatically return home when it detects a breach of the defined radius.</p>

<h3>Part B: Set a Geofence Altitude (Vertical Boundary)</h3>
<h4>Step-by-Step Commands</h4>
<pre><code>param show FENCE_ALT_MAX</code></pre>
<pre><code>param set FENCE_ALT_MAX 50</code></pre>

<pre><code>module load misseditor</code></pre>
<p>Select a waypoint and set <strong>Altitude</strong> to <strong>60m</strong> (above the max).</p>
<pre><code>module unload misseditor</code></pre>

<pre><code>mode GUIDED</code></pre>
<pre><code>arm throttle</code></pre>
<pre><code>takeoff 10</code></pre>
<pre><code>mode AUTO</code></pre>
<p>The drone will return home after detecting it has breached the maximum altitude.</p>
