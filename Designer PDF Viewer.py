#https://hackerrank-challenge-pdfs.s3.amazonaws.com/22869-designer-pdf-viewer-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654710479&Signature=gXwU66pTXC%2FJgqMlGJJNa0TaMwM%3D&response-content-disposition=inline%3B%20filename%3Ddesigner-pdf-viewer-English.pdf&response-content-type=application%2Fpdf

import string
def designerPdfViewer(h, word):
    d=[]
    reep=list(string.ascii_lowercase)
    for i in word:
        d.append(h[reep.index(i)])
    area=max(d)*len(d)
    return area
