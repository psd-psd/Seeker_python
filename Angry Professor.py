#https://hackerrank-challenge-pdfs.s3.amazonaws.com/6024-angry-professor-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654794519&Signature=8B1tNQtvzYjxQKg2lM13JLvyAd8%3D&response-content-disposition=inline%3B%20filename%3Dangry-professor-English.pdf&response-content-type=application%2Fpdf


def angryProfessor(k, a):
    a.sort(reverse=False)
    sum=0
    for i in range(0,len(a)):
        if a[i]<=0:
            sum+=1
            if sum==k:
                return 'NO'
    if sum<k:
        return 'YES'
