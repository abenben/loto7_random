import random

patterns = []
for i in range(10):
    pattern = []
    while len(pattern) < 7:
        num = int(random.gauss(19, 10))
        if num > 0 and num < 38 and num not in pattern:
            pattern.append(num)
    pattern.sort()
    patterns.append(pattern)

print("ランダムなロト7のパターンは以下の通りです:")
for pattern in patterns:
    print(pattern)