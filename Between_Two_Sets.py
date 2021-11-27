https://hackerrank-challenge-pdfs.s3.amazonaws.com/26081-between-two-sets-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1638047041&Signature=PMqFbLf2Q3LY8ZxoJJgToyIJIcw%3D&response-content-disposition=inline%3B%20filename%3Dbetween-two-sets-English.pdf&response-content-type=application%2Fpdf



def getTotalX(a, b):
        c=0
        for i in range(1,101):
            for n in range(0,len(a)):
                if i%a[n]!=0:
                    break
            else:
                for m in range(0,len(b)):
                    if b[m]%i!=0:
                        break
                else:
                     c+=1
        return c
      
      
      
