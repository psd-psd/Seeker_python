#https://hackerrank-challenge-pdfs.s3.amazonaws.com/27191-beautiful-days-at-the-movies-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654850283&Signature=%2FfshEdRMeNYGwL2ffJypEbWjYa8%3D&response-content-disposition=inline%3B%20filename%3Dbeautiful-days-at-the-movies-English.pdf&response-content-type=application%2Fpdf

def beautifulDays(i, j, k):
    c=0
    while i<=j:
        if (i-int(str(i)[::-1]))%k==0:
            c+=1
        i+=1
    return c
