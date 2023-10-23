from math import log2, ceil


def patrat_perfect(n):
    return (n & (not (n & (n-1))))


n = int(input("n="))

# Metoda cu log
print("Metoda 1: ")
if patrat_perfect(n):
    print(n)
else:
    print(2**ceil(log2(n)))

# Metoda cu shiftare
print("Metoda 2: ")
if patrat_perfect(n):
    print(n)
else:
    t = 1
    while t < n:
        t = t << 1

    print(t)
