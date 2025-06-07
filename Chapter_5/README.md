<h2>Rally Points in MAVProxy</h2>
<br>

<h4>What are Rally Points?</h4>
<p><strong>Rally Points</strong> are predefined safe landing locations. If a drone is far from home, it will land at the nearest rally point instead of returning to the original takeoff location during <strong>RTL (Return to Launch)</strong>.</p>

<p>This is useful in:</p>
<ul>
  <li>Long-distance missions</li>
  <li>Emergency landings</li>
  <li>Providing alternate landing zones</li>
</ul>

<h3>Step-by-Step Guide to Use Rally Points</h3>

<pre><code>mode GUIDED</code></pre>
<pre><code>arm throttle</code></pre>
<pre><code>takeoff 50</code></pre>
<p><strong>Step 1:</strong> Start the flight by setting mode, arming, and taking off.</p>

<pre><code>param set RALLY_LIMIT_KM 0</code></pre>
<p><strong>Step 2:</strong> This removes the limit on distance, allowing use of any rally point.</p>

<pre><code>rally list</code></pre>
<p><strong>Step 3:</strong> Check existing rally points.</p>

<pre><code>set rallyalt 50</code></pre>
<p><strong>Step 4:</strong> Set the altitude at which the drone will approach the rally point.</p>

<pre><code>rally add</code></pre>
<p><strong>Step 5:</strong> Click a location on the map, then use this command in the terminal to add the rally point.</p>

<pre><code>mode RTL</code></pre>
<p><strong>Step 6:</strong> Trigger <strong>Return to Launch</strong>. The drone will fly to and land at the nearest rally point (or home if closer).</p>
