#https://hackerrank-challenge-pdfs.s3.amazonaws.com/1957-cut-the-sticks-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1655394174&Signature=x6xswEmZw%2FD34Rh5HXw27wvYguI%3D&response-content-disposition=inline%3B%20filename%3Dcut-the-sticks-English.pdf&response-content-type=application%2Fpdf


def cutTheSticks(arr):
    m=sorted(arr)
    e=[]
    try:
        for i in range(0, len(m)):
                    e.append(len(m))
                    x=m.count(m[0])
                    while x>=1:
                        del m[0]
                        x-=1
                    l=m[0]
                    x=0
    except:
        IndexError
    return e
