import zipfile
import sys
from optparse import OptionParser
from threading import Thread


def create_zip(zip_name, file_name):
    zf = zipfile.ZipFile(zip_name, 'w')
    zf.write(file_name)
    print('%s successful add to %s.zip' % (file_name, zip_name))
    zf.close()
    return


def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print('[+] Found password: %s' % password)
    except Exception as inst:
        pass
        # print(type(inst))
        # print(inst.args)is
def main():
    parser = OptionParser('usage%prog -f <zip file> -d <dictionary>')
    parser.add_option('-f', dest='z_name', type='string', help='specify zip file')
    parser.add_option('-d', dest='d_name', type='string', help='specify dictionary file')

    options, args = parser.parse_args()
    if (options.z_name is None) | (options.d_name is None):
        print(parser.usage)
        exit(0)
    else:
        dictionary_name = options.d_name
        zip_name = options.z_name

    try:
        zip_file = zipfile.ZipFile(zip_name)
    except IOError as err:
        print('I/O error ({0}): {1}'.format(err.errno, err.strerror))
    except:
        print('Unexpected error: ', sys.exc_info()[0])
        raise
    else:
        with open(dictionary_name, 'r') as dictionary_file:
            for line in dictionary_file.readlines():
                password = line.strip('\n')
                t = Thread(target=extract_zip, args=(zip_file, password))
                t.start()

if __name__ == '__main__':
    main()

