from scapy.all import *

dns_records = {}


def handle_pkt(pkt):
    if pkt.haslayer(DNSRR):
        rrname = pkt.getlayer(DNSRR).rrname
        rdata = pkt.getlayer(DNSRR).rdata
        if dns_records.has_key(rrname):
            dns_records[rrname].append(rdata)
        else:
            dns_records[rrname] = []
            dns_records[rrname].append(rdata)


def main():
    pkts = rdpcap('fastFlux.pcap')
    for pkt in pkts:
        handle_pkt(pkt)
    for item in dns_records:
        print('[+] %s item has %s unique IPs' % (item, str(len(dns_records[item]))))

if __name__ == '__main__':
    main()