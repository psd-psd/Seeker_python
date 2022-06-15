#https://hackerrank-challenge-pdfs.s3.amazonaws.com/2040-sherlock-and-squares-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1655328923&Signature=SBCiIoDZqDBd5WRE6dIXdzWjqzQ%3D&response-content-disposition=inline%3B%20filename%3Dsherlock-and-squares-English.pdf&response-content-type=application%2Fpdf


def squares(a, b):
    return math.floor(math.sqrt(b)) + 1 - math.ceil(math.sqrt(a))
  
  
  
  
def squares(a, b):
  c=0
  for n in range(a,b+1):
          y=str(math.sqrt(n))[(str(math.sqrt(n)).index('.'))+1:]
          if len(y)==1:
              c+=1
  return c
