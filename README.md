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
```