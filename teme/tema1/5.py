from math import ceil, log2

n = int(input("n="))
mb = (1 << ceil(log2(n))) - 1
m = n ^ mb

cnt = 0
while m:
    cnt += m & 1
    m = m >> 1

print(cnt)
