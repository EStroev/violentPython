import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat-2')


def print_record(target):
    rec = gi.record_by_name(target)
    city = rec['city']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']

    print('[*] Target: %s Geo-located' % target)
    print('[+] City: %s Country: %s' % (str(city), str(country)))
    print('[+] Latitude: %s Longitude: %s' % (str(lat), str(long)))

target = '79.164.25.138'
print_record(target)
