import numpy as np
import matplotlib.pyplot as plt

def euclidean(p, q):
    return np.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

def city_block(p, q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])

def chessboard(p, q):
    return max(abs(p[0]-q[0]), abs(p[1]-q[1]))

p = (0,0)
q = (3,4)

print(f"Pixel p = {p}, pixel q = {q}")
print(f"D_euclidean     = {euclidean(p, q):.4f}")
print(f"D_4             = {city_block(p, q)}")
print(f"D_8             = {chessboard(p, q)}")

center = (5,5)
radius = 2
size = 11

fig, axes = plt.subplots(1,2, figsize=(10,5))
titles = ["D4 (City-block) <= 2", "D8 (Chessboard) <= 2"]

for ax, dist_fn, title in zip(axes, [city_block, chessboard], titles):
    grid = np.zeros((size, size))
    for r in range(size):
        for c in range(size):
            if dist_fn(center, (r,c)) <= radius:
                grid[r,c] = 1
    ax.imshow(grid, cmap="Blues", vmin=0, vmax=1.5)
    ax.plot(center[1], center[0], "ro", markersize=8, label="Pusat")
    ax.set_title(title)
    ax.legend()

plt.tight_layout()
plt.show()