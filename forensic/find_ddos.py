import dpkt
import socket

TRESH = 10000


def find_attack(pcap):
    pkt_count = {}
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = ip.src
            dst = ip.dst
            tcp = ip.data
            dport = tcp.dport
            if dport == '80':
                stream = src + ':' + dst
                if pkt_count.has_key(stream):
                    pkt_count[stream] += 1
                else:
                    pkt_count[stream] = 1
        except:
            pass

    for stream in pkt_count:
        pkt_sent = pkt_count[stream]
        if pkt_sent > TRESH:
            src, dst = stream.split(':')
            print('[+] %s attacked %s with %s pkts' % (src, dst, str(pkt_sent)))


def main():
    with open('test.pcap') as f:
        pcap = dpkt.pcap.Reader(f)

    find_attack(pcap)


if __name__ == '__main__':
    main()

