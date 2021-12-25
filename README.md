# routeinfo
Detalized route table to an IP address with locations and organizations of the servers and  some other info. Uses tracert on Windows to get the route and ipinfo.io to get the info of a server
<br>
Usage:<br>
python routeinfo.py google.com<br>
<br>
Output<br>
  8     5 ms     3 ms     3 ms  5.143.253.245   Moscow, Moscow, AS12389 PJSC Rostelecom<br>
  9     3 ms     *       15 ms  108.170.250.113         Leningradskaya Oblast', Kirishi, AS15169 Google LLC<br>
 10    22 ms    18 ms     *     142.251.49.158  New York, New York City, AS15169 Google LLC<br>
 11    17 ms    17 ms    17 ms  216.239.57.222  Leningradskaya Oblast', Sosnovyy Bor<br>
 12    25 ms    18 ms    22 ms  142.250.210.103         California, Fremont, AS15169 Google LLC<br>
 13     *        *        *     Request timed out.<br>
 14     *        *        *     Request timed out.<br>
 15     *        *        *     Request timed out.<br>
 16     *        *        *     Request timed out.<br>
 17     *        *        *     Request timed out.<br>
 18     *        *        *     Request timed out.<br>
 19     *        *        *     Request timed out.<br>
 20     *        *        *     Request timed out.<br>
 21     *        *        *     Request timed out.<br>
 22     *       17 ms    17 ms  142.251.1.139   California, Fremont, AS15169 Google LLC<br>
