a = []
for i in range(10**5):
     if i % 9 == 1:
         a.append(i)

listn = []
for i in a:
    sum = 0
    for j in str(i) :
        sum += int(j)
    listn.append(sum)

import pandas as pd

lisn = pd.DataFrame(listn)
print(lisn.tail())
b = pd.DataFrame(a)
print(b.tail())
print(lisn[0].value_counts())
sn = [19, 28, 10, 37, 1]

def check(k):
    sum = 0 
    for i in str(10**k - 1):
        sum += int(i)
    return sum <= 9 * k

for i in range(1, 10):
    print(check(i))

k = 1
while 10 ** (k - 1) <= (9 * k + 1)**2 - 3:
    k += 1
k
