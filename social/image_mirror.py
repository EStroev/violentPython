from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os

def mirror_images(url, dir):
    ab = anonBrowser()
    ab.anonymize()
    html = ab.open(url)
    soup = BeautifulSoup(html)
    image_tags = soup.findAll('img')
    for image in image_tags:
        file_name = image['src'].lstrip('http://')
        file_name = os.path.join(dir, file_name.replace('/', '_'))
        print('[+] Saving: ' + str(file_name))
        data = ab.open(image['src']).read()
        ab.back()
        save = open(file_name, 'wb')
        save.write(data)
        save.close()


def main():
    url = 'http://xkcd.com'
    dir = 'images'

    try:
        mirror_images(url, dir)
    except Exception as e:
        print('[-] Error Mirroring Images')
        print('[-] ' + str(e))

if __name__ == '__main__':
    main()
