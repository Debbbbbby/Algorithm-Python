n = int(input())
scores = list(map(int, input().split()))
M = max(scores)
new_scores = []
for x in scores:
    new_scores.append((x/M)*100)
print(sum(new_scores)/len(new_scores))