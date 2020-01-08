# Author: Burak Karaduman <burakkaradumann@gmail.com>
# Thanks to hackertarget.com

import requests
import pydoc
import os
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def clear():
    if os.name.lower() == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def less(text):
    return pydoc.pager(text)

def get(url):
    r = requests.get(url, verify=False)
    return r.text

menu = """
|||||||||||||| IP TOOLS ||||||||||||||

1-  DNS Lookup
2-  Find DNS Host Records (Subdomains)
3-  Reverse DNS
4-  Whois Lookup
5-  Reverse IP
6-  TCP Port Scan
7-  Subnet Calculator
8-  HTTP Headers
9-  Page Links

'q' for quit

||||||||||||||||||||||||||||||||||||||

Select: """

while True:
    clear()
    choose = input(menu)
    if choose == "1":
        i = input('Enter domain: ')
        less(get(f"https://api.hackertarget.com/dnslookup/?q={i}"))
        input("\nEnter to continue")
    elif choose == "2":
        i = input('Domain name: ')
        less(get(f"https://api.hackertarget.com/hostsearch/?q={i}"))
        input("\nEnter to continue")
    elif choose == "3":
        i = input('IP Address / IP Range / Domain Name: ')
        less(get(f"https://api.hackertarget.com/reversedns/?q={i}"))
        input("\nEnter to continue")
    elif choose == "4":
        i = input('Enter IP or Domain for lookup: ')
        less(get(f"https://api.hackertarget.com/whois/?q={i}"))
        input("\nEnter to continue")
    elif choose == "5":
        i = input('Enter ip address: ')
        less(get(f"https://api.hackertarget.com/reverseiplookup/?q={i}"))
        input("\nEnter to continue")
    elif choose == "6":
        i = input('Enter ip address: ')
        less(get(f"https://api.hackertarget.com/nmap/?q={i}"))
        input("\nEnter to continue")
    elif choose == "7":
        i = input('Enter cidr or ip with netmask')
        less(get(f"https://api.hackertarget.com/subnetcalc/?q={i}"))
        input("\nEnter to continue")
    elif choose == "8":
        i = input('Enter web address: ')
        less(get(f"https://api.hackertarget.com/httpheaders/?q={i}"))
        input("\nEnter to continue")
    elif choose == "9":
        i = input('Enter web address: ')
        less(get(f"https://api.hackertarget.com/pagelinks/?q={i}"))
        input("\nEnter to continue")
    elif choose.lower() == "q":
        print("Script closed.")
        break
    else:
        print("Wrong choise, try again!")
        continue
