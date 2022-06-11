#https://hackerrank-challenge-pdfs.s3.amazonaws.com/1884-circular-array-rotation-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654941306&Signature=upauOs4z0Np%2BRsXFC5hFo3VIVGo%3D&response-content-disposition=inline%3B%20filename%3Dcircular-array-rotation-English.pdf&response-content-type=application%2Fpdf

def circularArrayRotation(a, k, queries):
    while k!=0:
        a.insert(0,a[len(a)-1])
        del a[len(a)-1]
        k-=1
    i=0
    b=[]
    while i<len(queries):
        b.append(a[queries[i]])
        i+=1
    return b
