import telnetlib
import time
import argparse


parser = argparse.ArgumentParser(description='Check Possibles IP Conflicts on cisco devices througth Telnet')
parser.add_argument('--ip','-i', help='Ip of the router to connect')
parser.add_argument('--username','-u', help='Username of the Router')
parser.add_argument('--password','-p', help='Password of the Router')
parser.add_argument('--hostname','-x', help='Hostname of the Router')
args = parser.parse_args()
###############################################
########Telnet Conection######################
HOST = args.ip
user = args.username
password = args.password
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")    
tn.read_until(bytes(args.hostname + "#", encoding="ascii"))
tn.write(b"sh arp\n")
tn.write(b"exit\n")


arp = tn.read_all().decode('ascii')

####################Scrapying arp table#################
arp = arp.split()

for i in range (11):
    arp.pop(0)
arp.pop(-1)
while "Internet" in arp:
    arp.remove("Internet")
while "ARPA" in arp:
    arp.remove("ARPA")

arpTable = {}

for i in range (len(arp)):
    if i == 0 or i % 4 == 0:
        print ("ip : " + arp[i] + ": mac : " + arp[i+2])
        arpTable[arp[i + 2]] = arp[i]
############looking for repeted ips#############

rev_arp ={}

for key, value in arpTable.items():
    rev_arp.setdefault(value, set()).add(key)

result = [key for key, values in rev_arp.items() if len(values) > 1]
print("IP Duplicated : " + str(result))
#print(arpTable)




