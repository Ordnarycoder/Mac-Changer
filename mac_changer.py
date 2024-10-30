import subprocess
import argparse
import re

def get_user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change!", required=True)
    parser.add_argument("-m", "--mac", dest="mac_address", help="New MAC address", required=True)
    return parser.parse_args()

def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface]).decode('utf-8') 
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("MyMacChanger Started!")
user_input = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)
finalized_mac = control_new_mac(user_input.interface)

if finalized_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")
