https://hackerrank-challenge-pdfs.s3.amazonaws.com/33294-migratory-birds-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1639431444&Signature=XXrAbHwCrQBR1eca5o9RbPLaIW8%3D&response-content-disposition=inline%3B%20filename%3Dmigratory-birds-English.pdf&response-content-type=application%2Fpdf
  
  def migratoryBirds(arr):
    for i in range(0,4):
            a=arr.count(1)
            b=arr.count(2)
            c=arr.count(3)
            d=arr.count(4)
            e=arr.count(5)
    if a>=b and a>=c and a>=d and a>=e:
        return 1
    elif b>=a and b>=c and b>=d and b>=e:
        return 2
    elif c>=a and c>=b and c>=d and c>=e:
        return 3
    elif d>=a and d>=b and d>=c and d>=e:
        return 4
    elif e>=a and e>=b and e>=c and e>=d:
        return 5
