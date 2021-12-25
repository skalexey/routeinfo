# -*- coding: utf-8 -*-
# ========================================================================================
# Detalized route table to an IP address with locations and organizations of the servers and  some other info. Uses tracert on Windows to get the route and ipinfo.io to get the info of a server

# Usage:
# python routeinfo.py google.com

# Output
#   8     5 ms     3 ms     3 ms  5.143.253.245   Moscow, Moscow, AS12389 PJSC Rostelecom
#   9     3 ms     *       15 ms  108.170.250.113         Leningradskaya Oblast', Kirishi, AS15169 Google LLC
#  10    22 ms    18 ms     *     142.251.49.158  New York, New York City, AS15169 Google LLC
#  11    17 ms    17 ms    17 ms  216.239.57.222  Leningradskaya Oblast', Sosnovyy Bor
#  12    25 ms    18 ms    22 ms  142.250.210.103         California, Fremont, AS15169 Google LLC
#  13     *        *        *     Request timed out.
#  14     *        *        *     Request timed out.
#  15     *        *        *     Request timed out.
#  16     *        *        *     Request timed out.
#  17     *        *        *     Request timed out.
#  18     *        *        *     Request timed out.
#  19     *        *        *     Request timed out.
#  20     *        *        *     Request timed out.
#  21     *        *        *     Request timed out.
#  22     *       17 ms    17 ms  142.251.1.139   California, Fremont, AS15169 Google LLC
# ========================================================================================
import requests
import sys
import os
import subprocess
import re

if len(sys.argv) < 2:
    print('No arguments provided. Specify an IP adress to check with this script')
    sys.exit(1)

def addJsonFieldToStr(j, s, f):
    if f in j:
        if len(s) != 0:
            s = s + ', '
        s = s + j[f]
    return s

addr = sys.argv[1]
#addr = "yandex.ru"
if os.name == 'nt':
    outContent = subprocess.check_output('tracert -d -w 100 ' + addr)
    lines = outContent.split(b'\n')
    for line in lines:
        row = line.decode('utf-8')
        row = row.replace('\r', '')
        # Example of a row '1    <1 ms    <1 ms    <1 ms  192.168.1.1'
        searchResult = re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', row)
        if searchResult == None:
            #print('no match in ' + row)
            print(row)
            continue
        else:
            srvAddr = searchResult.group(0)
            #print('Found ' + srvAddr + ' in ' + row)
            r = requests.get("https://ipinfo.io/" + srvAddr)
            j = r.json()
            info = ''
            info = addJsonFieldToStr(j, info, 'region')
            info = addJsonFieldToStr(j, info, 'city')
            info = addJsonFieldToStr(j, info, 'org')
            if len(info) == 0:
                info = '[no info]'
            print(row + '\t' + info)
else:
    'Os ' + os.name + ' is not supported'
