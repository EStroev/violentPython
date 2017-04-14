from PIL import Image
from PIL.ExifTags import TAGS
from optparse import OptionParser
import os


def test_for_exif(image_file_name):
    try:
        exif_data = {}
        image_file = Image.open(image_file_name)
        info = image_file._getexif()
        if info:
            for (tag, value) in info.items():
                decoded_tag = TAGS.get(tag, tag)
                exif_data[decoded_tag] = value
                # print('%s: %s' % (decoded_tag, exif_data[decoded_tag]))
            try:
                exif_gps = exif_data['GPSInfo']
                if exif_gps:
                    print('[*] %s contains GPS MetaData' % image_file_name)
            except:
                pass
    except:
        pass


def main():
    parser = OptionParser('usage %prog -f <image file>')
    parser.add_option('-f', dest='image_file', type='string', help='specify image file')

    options, args = parser.parse_args()
    image_file = options.image_file

    if image_file is None:
        print(parser.usage)
        exit(0)

    test_for_exif(image_file)
    
if __name__ == '__main__':
    main()