N = int(input())
new = N
cycle = 0
while 1:
    a = new
    b = new % 10
    c = (a + b) % 10
    new = 10 * b + c
    cycle += 1
    if (N == new):
        break
print(cycle)