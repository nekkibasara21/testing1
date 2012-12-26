#! /usr/bin/env python3

import re,subprocess
import smtplib

from email.mime.text import MIMEText

ips = subprocess.call("/sbin/ifconfig | grep inet",shell=True)
msg = MIMEText(str(ips))

msg['Subject']="The IP using now"
msg['From']= "root@basaranekkiyam.no-ip.org"
msg['To']= "basara.msyam@gmail.com"

s=smtplib.SMTP('localhost')
s.sendmail("root@basaranekkiyam.no-ip.org","basara.msyam@gmail.com",msg.as_string())
s.sendmail("root@basaranekkiyam.no-ip.org","manson.yam@pacnet.com",msg.as_string())
s.quit
