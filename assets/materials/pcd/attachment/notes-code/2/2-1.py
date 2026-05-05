import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

base_dir = os.path.dirname(__file__)
img_path = os.path.join(base_dir, "contoh.jpg")

img = Image.open(img_path).convert("L")
A = np.array(img)

M,N = A.shape
k = 8
L = 2**k

print(f"Ukuran citra    : {M} x {N} pixel")
print(f"Bit-depth   : {k} bit => L = {L} tingkat keabuan")
print(f"Kebutuhan bit : {M*N*k:,} bit ({M*N*k/8/1024:.1f} KB)")
print(f"Nilai min   : {A.min()}")
print(f"Nilai max   : {A.max()}")

fig, axes = plt.subplots(1,2,figsize=(10, 4))

axes[0].imshow(A, cmap="gray", vmin=0, vmax=255)
axes[0].set_title("Citra Grayscale")
axes[0].axis("off")

axes[1].hist(A.ravel(), bins=256, range=(0, 255), color="steelblue", edgecolor="none")
axes[1].set_title("Histogram Intensitas")
axes[1].set_xlabel("Nilai Pixel")
axes[1].set_ylabel("Frekuensi")

plt.tight_layout()
plt.show()