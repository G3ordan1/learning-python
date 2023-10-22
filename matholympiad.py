# Given a +ve integer n, let s(n) denote the sum of the digits of n. Compute the
# largest +ve integer n such that n = s(n)^2 + 2s(n) - 2.
# Solution:

# Let d denote the number of digits of n. Then, 10^(d-1) <= n <= (9d)^2 + 2(9d) - 2
d = 1
while 10 ** (d - 1) <= (9 * d + 1)**2 - 3:
    print(f"{d} falls in the range")
    d += 1
print(f"{d} falls out of the range")

# d <= 4 but d != 4 as
d = 4
n = (9 * d + 1)**2 - 3
print(n)
# n < 1400 we have s(n) <= 1 + 3 + 9 + 9 = 22
n = 22**2 + 2 * 22 - 2
print(n)
# n < 1000
# therefore n has at most 3 digits. max s(n) = 9 * 3 = 27
# n = s(n)^2 + 2s(n) - 2 is equivalent to n^2-n+1 (mod 3)
# so n^2-2n+1 == 0 (mod 3) and (n-1)^2 == 0 (mod 3) and n == 1 (mod 3)
sn_list = []
for i in range(1, 1000):
    if i % 3 == 1:
        sum1 = 0
        for j in str(i):
            sum1 += int(j)
    if sum1 not in sn_list:
        sn_list.append(sum1)
print(sn_list)
sn_list.reverse()

for i in sn_list:
    n = (i + 1)**2 - 3
    sum1 = 0
    for j in str(n):
            sum1 += int(j)
    if i != sum1:
        print(f"If s(n) = {i}, then n = {n} which gives s(n) = {sum1}, so contradiction")
    else: 
        print(f"If s(n) = {i}, then n = {n} which gives s(n) = {sum1}, possible solution")

# for s(n) < 19, n < 397 so largest is 397.
