import dpkt
import socket
import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat-2')


def ret_geo_str(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_name']
        if city != '':
            geoloc = city + ',' + country
        else:
            geoloc = country
        return geoloc
    except:
        return 'Unregistered'


def print_pcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('[+] Src: %s --> Dst: %s' % (src, dst))
            print('[+] Src: %s --> Dst: %s' % (ret_geo_str(src), ret_geo_str(dst)))
        except:
            pass


def main():
    with open('geotest.pcap', 'r') as f:
        pcap = dpkt.pcap.Reader(f)
        print_pcap(pcap)


if __name__ == '__main__':
    main()