#https://hackerrank-challenge-pdfs.s3.amazonaws.com/29526-picking-numbers-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1650308803&Signature=JWP5hubu4WIbnTJ4KDXOuJ4uadI%3D&response-content-disposition=inline%3B%20filename%3Dpicking-numbers-English.pdf&response-content-type=application%2Fpdf

def pickingNumbers(a):
    c=0
    a.sort()
    new=[]
    for i in range(0, len(a)-1):
        for j in range(i, len(a)):
            if a[i]==a[j]+1 or a[i]==a[j]:
                c+=1
        new.append(c)
        c=0
    return max(new)
