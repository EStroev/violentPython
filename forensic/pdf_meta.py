from optparse import OptionParser
from pyPdf import PdfFileReader

def print_metadata(filename):
    pdf_file = PdfFileReader(open(filename, 'rb'))
    doc_info = pdf_file.getDocumentInfo()
    print('[*] PDF MetaData For: %s' % str(filename))
    for meta_item in doc_info:
        print('[+] %s: %s' % (meta_item, doc_info[meta_item]))


def main():
    parser = OptionParser('usage %prog -f <PDF file name>')
    parser.add_option('-f', dest='file_name', type='string', help='specify PDF file name')

    options, args = parser.parse_args()

    file_name = options.file_name

    if file_name is None:
        print(parser.usage)
        exit(0)
    else:
        print_metadata(file_name)

if __name__ == '__main__':
    main()