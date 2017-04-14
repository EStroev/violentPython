from scapy.all import *


def test_ttl(pkt):
    # try:
        if pkt.haslayer(IP):
            ip_src = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            print('[+] Packet received from %s with TTL %s' % (ip_src, ttl))
    # except:
    #     pass


def main():
    sniff(iface='en0', prn=test_ttl, store=0)


if __name__ == '__main__':
    main()