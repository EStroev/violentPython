import netaddr
from scapy.all import *
from optparse import OptionParser

ttl_values = {}
THRESH = 5


def check_ttl(ip_src, ttl):
    if netaddr.IPAddress(ip_src).is_private():
        return
    if not ttl_values.has_key(ip_src):
        pkt = sr1(IP(dst = ip_src) / ICMP(), retry=1, timeout=0, verbose=0)
        ttl_values[ip_src] == pkt.ttl
    if abs(int(ttl) - int(ttl_values[ip_src])) > THRESH:
        print('[!] Detected Possible Spoofed packet from %s' % ip_src)
        print('[!] TTL: %s Actual TTL: %s' % (ttl, ttl_values[ip_src]))


def test_ttl(pkt):
    try:
        if pkt.haslayer(IP):
            ip_src = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            check_ttl(ip_src, ttl)
    except:
        pass


def main():
    parser = OptionParser('usage%prog -i <interface> -t <tresh>')
    parser.add_option('-i', dest='iface', type='string', help='specify the network interface')
    parser.add_option('-t', dest='thresh', type='int', help='specify threshold counter')

    options, args = parser.parse_args()

    if options.iface is None:
        conf.iface = 'en0'
    else:
        conf.iface = options.iface

    if options.thresh is None:
        THRESH = options.thresh
    else:
        THRESH = 1

    sniff(prn=test_ttl, store=0)

if __name__ == '__main__':
    main()