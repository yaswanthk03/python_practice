'''
    Extract text data from a pdf.
'''

import pymupdf

TXT_FILE = 'pdf_text.txt'
FILE_NAME = 'mypdf.pdf'

def extract():
    doc = pymupdf.open(FILE_NAME)  
    with open(TXT_FILE, 'w', encoding='utf-8') as f:
        for page in range(len(doc)):
            f.write(doc[page].get_text())
            f.write('-' * 80 + '\n')

def main():
    extract()

main()