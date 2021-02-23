# Conflict IP detector for cisco networks
## Author: Matias Tillerias Ley

this is a simple python project that you can use to check your network and troubleshoot posibles ip conflicts

- it works over telnet (ssh soon)
- Clen report


## Usage

| Short Arg | Large Arg | Effect |
| ------ | ------ | ------ |
| -i | --ip | IP of the router or switch to connect
| -p | --password | Password of the device
| -u | --username | Username of the device
| -x | --hostname | Hostname of the device

```sh
python ./main.py -i 192.168.1.1 -u cisco -p ciscopass -x Router

ip : 192.168.1.1: mac : c401.0ad4.0000
ip : 192.168.1.2: mac : 0200.4c4f.4f50
ip : 172.20.10.11: mac : 7c25.da5e.d8cc
IP Duplicated : []
```

Also you can Download the Last relase for Windows 0x86_64 [here](https://github.com/MatiasTilerias/Conflic-arp-Cisco/releases/download/0.2/Conflict-Ip0.3.exe)