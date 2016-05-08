from scipy.misc import imread, imsave, imresize

img = imread('assets/cat.jpg')
print(img.dtype, img.shape)

img_tinted = img * [1, 0.95, 0.9]

img_tinted_resized = imresize(img_tinted, (300, 300))

imsave('assets/cat_tinted_and_resized.jpg', img_tinted_resized)

import numpy as np
from scipy.spatial.distance import pdist, squareform

x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

d = squareform(pdist(x, 'euclidean'))
print(d)

import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')

plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

plt.show()

img = imread('assets/cat.jpg')
img_tinted = img * [1, 0.95, 0.9]

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
# plt.imshow(img_tinted)
plt.imshow(np.uint8(img_tinted))

plt.show()