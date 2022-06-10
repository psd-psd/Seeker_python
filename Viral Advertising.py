#https://hackerrank-challenge-pdfs.s3.amazonaws.com/26216-strange-advertising-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654875154&Signature=eOAC8az9YMQL%2BuhiMF4qtRuTlcE%3D&response-content-disposition=inline%3B%20filename%3Dstrange-advertising-English.pdf&response-content-type=application%2Fpdf

def viralAdvertising(n):
    liked=5
    x=1
    get=[]
    while x<=n:
        day=liked//2
        get.append(day)
        liked=day*3
        x+=1
    return sum(get)
