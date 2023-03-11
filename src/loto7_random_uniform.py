import random

patterns = []
for i in range(10):
    pattern = []
    while len(pattern) < 7:
        num = int(random.uniform(1, 38))
        if num not in pattern:
            pattern.append(num)
    patterns.append(sorted(pattern))

print("ランダムなロト7のパターンは以下の通りです:")
for pattern in patterns:
    print(pattern)