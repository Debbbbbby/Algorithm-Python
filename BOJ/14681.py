x, y = int(input()), int(input())
if (0 < x) and (0 < y):     # x : 양수, y : 양수
    print(1)
elif (0 > x) and (0 < y):   # x : 음수, y : 양수
    print(2)
elif (0 > x) and (0 > y):   # x : 음수, y : 음수
    print(3)
else:                       # x : 양수, y : 음수
    print(4)