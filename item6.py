import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = {
    "ip": "192.168.56.119",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Show command that we execute.

#command = "show ip interface brief"
#command = "show running-config"
command = "show version"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans up the output so that only the show output is returned
print()
print(output)
print()
