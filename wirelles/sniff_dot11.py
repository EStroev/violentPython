from scapy.all import *
import sys

interface = 'mon0'
hidden_nets = []
unhidden_nets = []


def sniff_dot11(p):
    if p.haslayer(Dot11ProbeResp):
        addr2 = p.getlayer(Dot11).addr2
        if (addr2 in hidden_nets) & (addr2 not in unhidden_nets):
            net_name = p.getlayer(Dot11ProbeResp).info
            print('[+] Decloaked Hidden SSID: %s from MAC: %s' % (net_name, addr2))
            unhidden_nets.append(addr2)

    if p.haslayer(Dot11Beacon):
        if p.getlayer(Dot11Beacon).info == '':
            addr2 = p.getlayer(Dot11).addr2
            if addr2 not in hidden_nets:
                print('[-] Detected Hidden SSID with MAC: ' + addr2)
                hidden_nets.append(addr2)


sniff(iface=interface, prn=sniff_dot11)