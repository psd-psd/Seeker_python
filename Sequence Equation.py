#https://hackerrank-challenge-pdfs.s3.amazonaws.com/32362-permutation-equation-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654943775&Signature=Ft7ggkNnC32g4rWtmdQms1W6P2A%3D&response-content-disposition=inline%3B%20filename%3Dpermutation-equation-English.pdf&response-content-type=application%2Fpdf

def permutationEquation(p):
    b=[]
    for i in range(0,len(p)):
        b.append(p.index((p.index(i+1)+1))+1)
    return b
