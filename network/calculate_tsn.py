from scapy.all import *


def cat_tsn(tgt):
    seq_num = 0
    pre_num = 0
    dif_seq = 0
    for x in range(1, 5):
        if pre_num != 0:
            pre_num = seq_num
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        print(1)
        seq_num = ans.getlayer(TCP).seq
        dif_seq = seq_num - pre_num
        print('[+] TCP Seq Difference: %s' % dif_seq)
    return dif_seq + seq_num

tgt = '192.168.1.1'
seq_num = cat_tsn(tgt)
print('[!] Next Seq Number to ACK is %s' % str(seq_num + 1))