import random

patterns = []
for i in range(10):
    pattern = random.sample(range(1, 38), 7)
    pattern.sort()
    patterns.append(pattern)

print("ランダムなロト7のパターンは以下の通りです:")
for pattern in patterns:
    print(pattern)