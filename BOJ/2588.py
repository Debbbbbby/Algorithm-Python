a, b = int(input()), list(input())
res, ret = 0, []
for i in range(len(b)):
    res = a * int(b[i])
    print(res)
    if i == 0:
        ret.append(res)
    else:
        ret.append(res * (10 * i))
print(i for i in ret)
print(sum(ret))