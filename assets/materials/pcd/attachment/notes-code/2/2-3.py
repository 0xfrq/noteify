import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os

#img = cv2.imread("contoh.jpg", cv2.IMREAD_GRAYSCALE)
base_dir = os.path.dirname(__file__)
img_path = os.path.join(base_dir, "contoh.jpg")

img = np.array(Image.open(img_path).convert("L"))
M, N = img.shape

#opencv
# pusat = (N // 2, M // 2)
# A_rot = cv2.getRotationMatrix2D(pusat, angle=30, scale=1.0)
# img_rot = cv2.warpAffine(img, A_rot, (N,M))


#image rotation
img_rot = np.zeros_like(img)
angle = 30
theta = np.radians(angle)
cx, cy = N//2, M//2

cos_t = np.cos(theta)
sin_t = np.sin(theta)

for y_dst in range(M):
    for x_dst in range(N):
        x_src = (x_dst -cx) * cos_t + (y_dst-cy)*sin_t+cx
        y_src =-(x_dst-cx) * sin_t + (y_dst-cy)*cos_t+cy

        x_src_int = int(round(x_src))
        y_src_int = int(round(y_src))

        if 0 <= x_src_int < N and 0 <= y_src_int < M:
            img_rot[y_dst, x_dst] = img[y_src_int, x_src_int]

Image.fromarray(img_rot).show()

#not yet done