#https://hackerrank-challenge-pdfs.s3.amazonaws.com/28389-electronics-shop-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1649975335&Signature=eKfmRE868Q6vo3MiEPrCZ6Axbyc%3D&response-content-disposition=inline%3B%20filename%3Delectronics-shop-English.pdf&response-content-type=application%2Fpdf

def getMoneySpent(keyboards, drives, b):
    sum=[]
    if min(keyboards)>b:
        return -1
    elif min(drives)>b:
        return -1
    else:
        for i in range(0, len(keyboards)):
            for j in range(0, len(drives)):
                    sum.append(keyboards[i]+drives[j])
        sum.sort()
        if min(sum)>b:
                return -1
        else:
            for i in range(0,len(sum)):
                    if sum[i]>b:
                        return sum[i-1]
