import random

seed = 42
random.seed(seed)

patterns = []
for i in range(10):
    pattern = []
    for j in range(7):
        number = random.randint(1, 37)
        while number in pattern:
            number = random.randint(1, 37)
        pattern.append(number)
    pattern.sort()
    patterns.append(pattern)

print("ランダムなロト7のパターンは以下の通りです:")
for pattern in patterns:
    print(pattern)