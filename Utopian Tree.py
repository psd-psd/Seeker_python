#https://hackerrank-challenge-pdfs.s3.amazonaws.com/1308-utopian-tree-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654793452&Signature=%2FKQP3MMjkJcEE4aUEgBiILPwhF0%3D&response-content-disposition=inline%3B%20filename%3Dutopian-tree-English.pdf&response-content-type=application%2Fpdf

def utopianTree(n):
    sum=0
    res=[]
    for i in range(1,n+2):
        if i%2==0:
            sum=2*sum
        else:
            sum=sum+1
        res.append(sum)
    return max(res)
