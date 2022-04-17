#https://hackerrank-challenge-pdfs.s3.amazonaws.com/22937-magic-square-forming-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1650210950&Signature=F7odKPABOiJb7a49y9grXaPY4zw%3D&response-content-disposition=inline%3B%20filename%3Dmagic-square-forming-English.pdf&response-content-type=application%2Fpdf

squares = [(2, 7, 6, 9, 5, 1, 4, 3, 8),
(2, 9, 4, 7, 5, 3, 6, 1, 8),
(4, 3, 8, 9, 5, 1, 2, 7, 6),
(4, 9, 2, 3, 5, 7, 8, 1, 6),
(6, 1, 8, 7, 5, 3, 2, 9, 4),
(6, 7, 2, 1, 5, 9, 8, 3, 4),
(8, 1, 6, 3, 5, 7, 4, 9, 2),
(8, 3, 4, 1, 5, 9, 6, 7, 2)]
u_squares=[]
for i in squares:
    u_squares.append((list(i)))
def formingMagicSquare(s):
    s_=[]
    for i in s:
        for j in i:
            s_.append(j)
    diff=0
    cost=[]
    for x in u_squares:
        for n in range(len(s_)):
                diff=abs(s_[n]-x[n])+diff
        cost.append(diff)
        diff=0
    return min(cost)
