#https://hackerrank-challenge-pdfs.s3.amazonaws.com/32958-the-hurdle-race-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654707433&Signature=nRLdbmUocfSRmFOKBgPjfVQCNSg%3D&response-content-disposition=inline%3B%20filename%3Dthe-hurdle-race-English.pdf&response-content-type=application%2Fpdf

def hurdleRace(k, height):
        d=max(height)-k
        if d<1:
            return 0
        else:
            return d
