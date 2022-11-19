#https://hackerrank-challenge-pdfs.s3.amazonaws.com/17610-non-divisible-subset-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1668869287&Signature=vLEgq%2Bh1%2B9RXIzATkI%2FionT3HI4%3D&response-content-disposition=inline%3B%20filename%3Dnon-divisible-subset-English.pdf&response-content-type=application%2Fpdf

def nonDivisibleSubset(k, s):
    val=[]
    freq=[]
    res=[]
    for i in range(0,len(s)):
        val.append(s[i]%k)
    for i in range(0,k):
        freq.append(val.count(i))
    y=len(freq)//2
    for i in range(0,y):
            res.append(max(freq[i+1],freq[len(freq)-i-1]))
    if k%2==0:
        if freq[k//2]!=0:
            if freq[0]==0:
                return sum(res)-freq[k//2]
            else:
                return sum(res)+1-freq[k//2]+1
    else:
        if freq[0]==0:
                return sum(res)
        else:
            return sum(res)+1
