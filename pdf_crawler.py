#!/usr/bin/python
import urllib3
from pyPdf import PdfFileWriter, PdfFileReader
from StringIO import StringIO

http = urllib3.PoolManager()

def download_pdf(pdf_url, i):
    output_file_name = "cloud-" + str(i) + ".pdf"
    print pdf_url, output_file_name
    resp = http.request('GET', pdf_url)
    with open(output_file_name, 'wb') as f:
        f.write(resp.data)
    resp.release_conn()
    print "The " + str(i) + " file completed."


i = 16
while i <= 25 :
    download_pdf("http://farmer.iyard.org/jwj/paper/cloud-" + str(i) + ".pdf", i)
    i += 1
