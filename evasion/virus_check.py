import re
import httplib
import time
import os
import optparse
from urlparse import urlparse


def print_result(url):
    status = 200
    host = urlparse(url)[1]
    path = urlparse(url)[2]
    if 'analysis' not in path:
        while status != 302:
            conn = httplib.HTTPConnection(host)
            conn.request('GET', path)
            resp = conn.getresponse()
            status = resp.status
            print('[+] Scanning file...')
            conn.close()
            time.sleep(15)
    print('[+] Scan Complete!')
    path = path.replace('file', 'analysis')
    conn = httplib.HTTPConnection(host)
    conn.request('GET', path)
    resp = conn.getresponse()
    data = resp.read()
    conn.close()

    re_results = re.findall(r'Detection rate:.*\) ', data)
    html_strip_res = re_results[1].replace('&lt;font color=\'red\'&qt;', '').replace('&lt;/font&qt;', '')
    print('[+] ' + str(html_strip_res))


def upload_file(file_name):
    print('[+] Uploading file to NoVirusThanks...')
    file_contents = open(file_name, 'rb').read()

    header = {'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundaryF17rwCZdGuPNPT9U'}
    params = "------WebKitFormBoundaryF17rwCZdGuPNPT9U"
    params += "\r\nContent-Disposition: form-data; "+"name=\"upfile\"; " "filename=\""+str(file_name)+"\""
    params += "\r\nContent-Type: "+"application/octet stream\r\n\r\n"
    params += file_contents
    params += "\r\n------WebKitFormBoundaryF17rwCZdGuPNPT9U"
    params += "\r\nContent-Disposition: form-data; "+"name=\"submitfile\"\r\n"
    params += "\r\nSubmit File\r\n"
    params +="------WebKitFormBoundaryF17rwCZdGuPNPT9U--\r\n"

    conn = httplib.HTTPConnection('vscan.novirusthanks.org')
    conn.request('POST', '/', params, header)
    response = conn.getresponse()
    location = response.getheader('location')
    conn.close()
    return location


def main():
    parser = optparse.OptionParser('usage%prog -f <filename>')
    parser.add_option('-f', dest='fileName', type='string', help='specify filename')

    (options, args) = parser.parse_args()

    file_name = options.fileName
    if file_name is None:
        print parser.usage
        exit(0)
    elif os.path.isfile(file_name) is False:
        print '[+] ' + file_name + ' does not exist.'
        exit(0)
    else:
        loc = upload_file(file_name)
        print_result(loc)

if __name__ == '__main__':
    main()


