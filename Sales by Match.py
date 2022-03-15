#https://hackerrank-challenge-pdfs.s3.amazonaws.com/25168-sock-merchant-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1647364379&Signature=c3i%2Bfg8OXX4jN2hmUubzC2Ff%2B4Y%3D&response-content-disposition=inline%3B%20filename%3Dsock-merchant-English.pdf&response-content-type=application%2Fpdf

from collections import Counter
def sockMerchant(n, ar):
    p=[]
    x=Counter(ar)
    t=list(x.values())
    for i in range(0,len(t)):
        if t[i]>1 and (t[i]%2)!=0:
            p.append((t[i]-1)//2)
        elif t[i]>1 and (t[i]%2)==0:
            p.append((t[i])//2)
    return sum(p)
