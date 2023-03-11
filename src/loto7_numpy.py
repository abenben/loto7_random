import numpy as np

patterns = []
for i in range(10):
    pattern = np.random.choice(np.arange(1, 38), size=7, replace=False)
    pattern.sort()
    patterns.append(pattern)

print("ランダムなロト7のパターンは以下の通りです:")
for pattern in patterns:
    print(pattern)