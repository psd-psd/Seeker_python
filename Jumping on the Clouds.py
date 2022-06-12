#https://hackerrank-challenge-pdfs.s3.amazonaws.com/21277-jumping-on-the-clouds-revisited-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1655037354&Signature=K3jH%2BRmXvYn4C5A96CIrqkRMPQc%3D&response-content-disposition=inline%3B%20filename%3Djumping-on-the-clouds-revisited-English.pdf&response-content-type=application%2Fpdf



def jumpingOnClouds(c, k):
    e=100
    i=k
    if k==len(c):
        i=0
        if c[i]==1:
                e=e-3
        else:
            e=e-1
    else:
        while 1:
            if c[i]==1:
                e=e-3
            else:
                e=e-1
            if i==len(c)-k:
                i=0
                if c[i]==1:
                    e=e-3
                else:
                    e=e-1
                break
            i=i+k
            if i>len(c):
                i=i-len(c)
    return e
