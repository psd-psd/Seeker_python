#https://hackerrank-challenge-pdfs.s3.amazonaws.com/26066-append-and-delete-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1655320435&Signature=E0VFv%2FppaZApVc20FijiraQ%2B68I%3D&response-content-disposition=inline%3B%20filename%3Dappend-and-delete-English.pdf&response-content-type=application%2Fpdf


def appendAndDelete(s, t, k):
    c=0
    i=0
    while s[i]==t[i]:
        c+=1
        i+=1
        if i>len(t)-1 or i>len(s)-1:
            break
    x=len(s)+len(t)-2*c
    if x==k or x==0:
        return 'Yes'
    elif x<k:
        if (k-x)%2==0 or (k-x)>2*c:
            return 'Yes'
        else:
            return 'No'
    elif x>k:
        return 'No'
