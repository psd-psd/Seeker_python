simulating a voting system where random votes are cast for three candidates ('a', 'b', and 'c'), and then determining the winner based on the total votes for each. It also plots the results in a bar chart.

import random
import matplotlib.pyplot as plt
candidates = ['a', 'b', 'c']
votes = []
for i in range(0,100):
    for j in range(0,3):
        votes.append(random.randint(1,3))
a = []
b = []
c = []
for i in range(0,len(votes),3):
    a.append(votes[i])
for i in range(1,len(votes),3):
    b.append(votes[i])
for i in range(2,len(votes),3):
    c.append(votes[i])


x=max(sum(a), sum(b), sum(c))
if x==sum(a):
    print("a is the winner")
if x==sum(b):
    print("b is the winner")
if x==sum(c):
    print("c is the winner")
plt.bar(candidates, [sum(a), sum(b), sum(c)], color=['blue', 'green', 'red'])
plt.show()
