#!/usr/bin/python3

import os, re

fileContent = {}

for file in os.listdir("./ft_fun/"):
    with open("./ft_fun/%s" % file, 'r') as f:
        thisFile = f.read()
        f.close()
    fileNumber = re.findall('//file([0-9]*)', thisFile)
    if len(fileNumber) == 1:
        fileContent[int(fileNumber[0])] = thisFile
    else:
        print('numerous file numbers')
if os.path.exists('./read_fun') is True:
    os.remove('./read_fun')
with open('./read_fun', 'w') as f:
    for line in open('./ft_fun/BJPCP.pcap').readlines():
        if line.find('return') == -1:
            continue
        f.write(line)
    for key in sorted(fileContent):
        if fileContent[key].find('Got') != -1 or fileContent[key].find('useless') != -1:
            continue
        if fileContent[key].find('return') == -1:
            continue
        f.write(fileContent[key] +'\n')
    f.close()
