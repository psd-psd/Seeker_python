# https://hackerrank-challenge-pdfs.s3.amazonaws.com/32335-breaking-best-and-worst-records-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1638148204&Signature=QxQVSaOL0eGQJFm6fx%2FSBEsSsW4%3D&response-content-disposition=inline%3B%20filename%3Dbreaking-best-and-worst-records-English.pdf&response-content-type=application%2Fpdf

def breakingRecords(scores):
    h=0
    l=0
    i=0
    currentmax=[0]
    currentmin=[]
    if len(scores)==1:
        return 0,0
    elif scores[i+1]<scores[i]:
        currentmin.append(scores[i+1])
        l+=1
        currentmax.append(scores[i])
    elif scores[i+1]==scores[i]:
        currentmin.append(scores[i+1])
        currentmax.append(scores[i])
    for i in range(0, len(scores)-1):
        if scores[i+1]>scores[i] and scores[i+1]>max(currentmax):
            h+=1
            currentmax.append(scores[i+1])
            currentmin.append(scores[i])
        elif scores[i+1]<scores[i] and scores[i+1]<min(currentmin):
                l+=1
                currentmin.append(scores[i+1])
                currentmax.append(scores[i])
    return h, l
