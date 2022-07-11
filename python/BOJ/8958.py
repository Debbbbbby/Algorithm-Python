cases = int(input())

def get_score(inputStr):
    point_tracker = 0
    total_point = 0
    for i, c in enumerate(inputStr):
        if c == "O":
            point_tracker += 1
            # print(f"point_tracker : {point_tracker}, c : {c}")
        else:
            point_tracker = 0
        total_point += point_tracker
        # print(f"point_tracker : {point_tracker}, total_point : {total_point}")
    return total_point

for _ in range(cases):
    s = input()
    print(get_score(s))
