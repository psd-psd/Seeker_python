#https://hackerrank-challenge-pdfs.s3.amazonaws.com/22564-drawing-book-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1647619301&Signature=UOmI5Q3SrpiYy%2FIn2iptuYbevAc%3D&response-content-disposition=inline%3B%20filename%3Ddrawing-book-English.pdf&response-content-type=application%2Fpdf

def pageCount(n, p):
    if n-p>=p:
        if p-1>=2:
            return (p)//2
        elif p-1==0:
            return (0)
        else:
            return (1)
    else:
        if n-p<=p:
            if n-p>=2:
                return ((n-p)//2)
            elif n-p==1:
                return (1)
            else:
                return (0)

            
            
  #another method

def pageCount(n, p):
    if n==2*p:
        if n%2==0 and n-p==1 and p==1:
            return 0
        if n%2==0 and n-p==1:
            return 1
        elif n%2!=0 and n-p==1:
            return 0
        else:
            return (p)//2 
    if p>n/2:
        if n%2==0 and n-p==1:
            return 1
        elif n%2!=0 and n-p==1:
            return 0
        else:
            return ((n-p)//2)
    elif p<n/2:
        if n%2==0 and n-p==1:
            return 1
        elif n%2!=0 and n-p==1:
            return 0
        else:
            return (p)//2
