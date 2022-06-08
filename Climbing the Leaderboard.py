#https://hackerrank-challenge-pdfs.s3.amazonaws.com/29530-climbing-the-leaderboard-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654689074&Signature=e9uJR%2FKDIY2v%2FFU6XsE3C0uTOcw%3D&response-content-disposition=inline%3B%20filename%3Dclimbing-the-leaderboard-English.pdf&response-content-type=application%2Fpdf


import bisect
def climbingLeaderboard(ranked, player):
            root=[]
            ranked = sorted(list(set(ranked)), reverse=False)
            avg=sum(ranked)//2
            for y in range(0, len(player)):
                        if player[y]>avg and player[y]!=ranked[0]:
                            root.append(len(ranked)-bisect.bisect_left(ranked,player[y])+1)
                        else:
                            root.append(len(ranked)-bisect.bisect_right(ranked,player[y])+1)
            return sorted(root, reverse=True)
