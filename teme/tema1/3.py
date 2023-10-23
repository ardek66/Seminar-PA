x = int(input("x="))
y = int(input("y="))
t = x ^ y
cnt = 0

print("{0:07b}\n{1:07b}\n{2:07b}".format(x, y, t))

while t:
    cnt += t & 1
    t = t >> 1

print(cnt)
