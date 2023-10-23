sir = input("Tastati sirul cu spatii intre numere:").split(" ")
n = len(sir)

count = {}

for x in sir:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

for k, v in count.items():
    if v & 1:
        print(k)
        break
