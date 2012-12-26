#! /usr/bin/env python3

import subprocess
rt= subprocess.call("/sbin/ifconfig | grep inet > /home/yammsm/Ubuntu\ One/currentIP.txt" , shell=True)
rt2= subprocess.call("date >> /home/yammsm/Ubuntu\ One/currentIP.txt" , shell=True)
#subprocess.call("echo 'testing one' > /home/yammsm/Ubuntu\ One/currentIP.txt" , shell=True)

