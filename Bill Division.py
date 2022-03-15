#https://hackerrank-challenge-pdfs.s3.amazonaws.com/24060-bon-appetit-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1647364584&Signature=MHL8VshYpR2%2Bi9Mf49HQfYz4LKE%3D&response-content-disposition=inline%3B%20filename%3Dbon-appetit-English.pdf&response-content-type=application%2Fpdf

def bonAppetit(bill, k, b):
    if sum(bill)//2==b:
        print(b-(sum(bill)-bill[k])//2)
    else:
        print('Bon Appetit')
