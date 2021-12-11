https://hackerrank-challenge-pdfs.s3.amazonaws.com/21634-divisible-sum-pairs-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1639246544&Signature=ajkfTrYlMcij819y6qGO1%2FIsnio%3D&response-content-disposition=inline%3B%20filename%3Ddivisible-sum-pairs-English.pdf&response-content-type=application%2Fpdf
  
  
  def divisibleSumPairs(n, k, ar):
    c=0
    for x in range(0, n):
        for i in range(0,n):
            if x==i:
                continue
            elif (ar[x]+ar[i])%k==0 and x<i:
                    c+=1
    return c
