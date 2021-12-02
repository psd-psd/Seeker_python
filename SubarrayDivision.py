https://hackerrank-challenge-pdfs.s3.amazonaws.com/35155-the-birthday-bar-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1638481535&Signature=KQrJZXERM4SvSUqOQUU9hX1HA80%3D&response-content-disposition=inline%3B%20filename%3Dthe-birthday-bar-English.pdf&response-content-type=application%2Fpdf

def birthday(s, d, m):
    sum=0
    if len(s)==1 and m==1:
        if s[0]==d:
            return 1
    else:
        for i in range(0, (len(s)-m)+1):
            c=0
            for x in range(i,i+m):
                c=s[x]+c
            if c==d:
                sum+=1
    return sum 
