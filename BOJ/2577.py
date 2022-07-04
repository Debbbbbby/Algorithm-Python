a, b, c = int(input()), int(input()), int(input())
total = list(str(a * b * c))
for i in range(10):
    print(total.count(str(i)))