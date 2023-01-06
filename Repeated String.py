#https://hackerrank-challenge-pdfs.s3.amazonaws.com/24548-repeated-string-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1673011285&Signature=iIL3AMhFuwtY4%2FyXWsLv0QLCxXk%3D&response-content-disposition=inline%3B%20filename%3Drepeated-string-English.pdf&response-content-type=application%2Fpdf

def repeatedString(s, n):
    c=0
    g=0
    for i in range(0, len(s)):
        if s[i]=='a':
            c+=1
    if n%len(s)==0:
        return (n//len(s))*c
    else:
        rem=n%len(s)
        for i in range(0, rem):
            if s[i]=='a':
                g+=1
        return (n//len(s))*c+g
