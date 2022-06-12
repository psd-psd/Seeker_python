#https://hackerrank-challenge-pdfs.s3.amazonaws.com/127-find-digits-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1655065534&Signature=2Wca2Ox8j%2ByGzA2r6mcypGbr5gk%3D&response-content-disposition=inline%3B%20filename%3Dfind-digits-English.pdf&response-content-type=application%2Fpdf

def findDigits(n):
    x=str(n)
    c=0
    for i in x:
        try:
            if n%int(i)==0 and int(i)!=0:
                                        c+=1
        except:
            ZeroDivisionError
    return c
  
  
  if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
