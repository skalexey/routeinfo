# -*- coding: utf-8 -*-
# Detalized route table to an IP address with locations and organizations of the servers and some other info
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



