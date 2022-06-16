#https://hackerrank-challenge-pdfs.s3.amazonaws.com/8656-library-fine-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1655376208&Signature=OuIJjso49QnjnGknD9qo3KgVC1Y%3D&response-content-disposition=inline%3B%20filename%3Dlibrary-fine-English.pdf&response-content-type=application%2Fpdf


def libraryFine(d1, m1, y1, d2, m2, y2):
    day=0
    month=0
    year=0
    if y2==y1:
        year=0
        if m2==m1:
            month=0
            day=d1-d2
        elif m1>m2:
            month=m1-m2
            day=0
    elif y1>y2:
        year=y1-y2
    x=day*15+month*500+year*10000
    if x<0:
        return 0
    else:
        return x
