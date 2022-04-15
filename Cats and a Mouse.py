#https://hackerrank-challenge-pdfs.s3.amazonaws.com/29054-cats-and-a-mouse-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1650047972&Signature=pVCj4od6aE39xrnjMjAv4YVPIew%3D&response-content-disposition=inline%3B%20filename%3Dcats-and-a-mouse-English.pdf&response-content-type=application%2Fpdf

def catAndMouse(x, y, z):
    if z-x==y-z:
        return 'Mouse C'
    elif x==y:
        return 'Mouse C'
    if y>x:
        if z-x<y-z or z<x<y:
            return 'Cat A'
        elif y-z<z-x or z>y>x:
            return 'Cat B'
    elif x>y:
        if z-y<x-z or z<y<x:
            return 'Cat B'
        elif x-z<z-y or z>x>y:
            return 'Cat A'
