from scapy.all import *


def dns_qr_test(pkt):
    if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode
        qname = pkt.getlayer(DNSQR).qname
        if rcode == 3:
            print('[!] Name request lookup failed: %s' % qname)
            return True
        else:
            return False


def main():
    un_ans_req = 0
    pkts = rdpcap('domainFlux.pcap')
    for pkt in pkts:
        if dns_qr_test(pkt):
            un_ans_req += 1
    print('[!] %s Total unAnswered ame Requests!' % str(un_ans_req))


if __name__ == '__main__':
    main()
