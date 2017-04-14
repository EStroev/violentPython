from scapy.all import *

interface = 'mon0'
probe_reqs = []

def sniff_probes(p):
    if p.haslayer(Dot11ProbeReq):
        net_name = p.getlayer(Dot11ProbeReq).info
        if net_name not in probe_reqs:
            probe_reqs.append(net_name)
            print('[+] Detected New Probe Request: ' + net_name)

sniff(iface=interface, prn=sniff_probes)