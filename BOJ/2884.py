h, m = map(int, input().split())
if m > 44: # 45분 이상 : 시간 그대로, -45분
    print(h, m - 45)
elif (m < 45) and (h > 0): # 1시~23시 라면 h-1, 45분 미만이라면 +15분
    print(h - 1, m + 15)
else:
    print(23, m + 15) # 0시라면 h-1은 23시로 표기, 45분 미만이기 때문에 + 15분