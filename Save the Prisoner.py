#https://hackerrank-challenge-pdfs.s3.amazonaws.com/13489-save-the-prisoner-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654899575&Signature=aHBAkpkvHxxijyAsoJgb4GTNdok%3D&response-content-disposition=inline%3B%20filename%3Dsave-the-prisoner-English.pdf&response-content-type=application%2Fpdf

def saveThePrisoner(n, m, s):
            if m%n+(s-1)==0:
                return n
            elif m%n+(s-1)<=n:
                    return m%n+(s-1)
            else:
                return (m%n+(s-1))-n
