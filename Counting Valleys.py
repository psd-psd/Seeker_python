#https://hackerrank-challenge-pdfs.s3.amazonaws.com/22936-counting-valleys-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1649964251&Signature=GfCPLtQvaBMuhCw6cC1koHGQAXw%3D&response-content-disposition=inline%3B%20filename%3Dcounting-valleys-English.pdf&response-content-type=application%2Fpdf



def countingValleys(steps, path):
    u=0
    d=0
    s=0
    for i in range(0,steps):
        if path[i]=='U':
            u+=1
        elif path[i]=='D':
            d+=1
        if u==d and path[i]=='U':
            s+=1
        else:
            continue
    return(s) 
