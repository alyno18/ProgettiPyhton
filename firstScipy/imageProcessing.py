from scipy import ndimage, misc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

f = misc.face()
f1 = misc.face(gray=True).astype(float)
print("Shape: ", f.shape)
print("Type: ", type(f))
plt.imshow(f)
plt.show()
# plt.imshow(f1, cmap=plt.cm.gray)
# plt.show()

plt.imshow(f[20:150, 30:300])
plt.show()

f_modified = f.copy()
f_modified[20:150, 30:300] = 255
plt.imshow(f_modified)
plt.show()

fig, ax = plt.subplots(5)
ax[0].imshow(f)
ax[0].set(title="Immagine originale")
ax[1].imshow(f[20:200, 40:400])
ax[1].set(title="Immagine croppata")
f_flipped = np.flip(f)
ax[2].imshow(f_flipped)
ax[2].set(title="Mirror rispetto all'asse x")
ax[3].imshow(ndimage.rotate(f, 45))
ax[3].set(title="Immagine ruotata di 45°")
ax[4].imshow(ndimage.rotate(f, 45, reshape=False))
ax[4].set(title="Immagine ruotata senza reshape")
plt.show()


istogramma = np.histogram(f1, bins=np.arange(256))
plt.bar(istogramma[1][:-1], istogramma[0])
plt.show()


fig2, ax2 = plt.subplots(4)
ax2[0].imshow(f1, cmap=plt.cm.gray)
ax2[0].set(title="Immagine originale")
f_light = f1.copy().astype("int32")
f_light += 40
np.clip(f_light, 0, 255, out=f_light)
f_light = f_light.astype("uint8")
ax2[1].imshow(f_light, cmap=plt.cm.gray)
ax2[1].set(title="Immagine con intensità +40")
f_dark = f1.copy().astype("int32")
f_dark -= 40
np.clip(f_dark, 0, 255, out=f_dark)
f_dark = f_dark.astype("uint8")
ax2[2].imshow(f_dark, cmap=plt.cm.gray)
ax2[2].set(title="Immagine con intensità -40")
f_higher_contrast = f1.copy().astype("float32")
f_higher_contrast *= 1.2
np.clip(f_higher_contrast, 0, 255, out=f_higher_contrast)
f_contrast = f_higher_contrast.astype("uint8")
ax2[3].imshow(f_contrast, cmap=plt.cm.gray)
ax2[3].set(title="Immagine con contrasto *1.2")
plt.show()

fig3, ax3 = plt.subplots(3)
ax3[0].imshow(f1, cmap=plt.cm.gray)
ax2[0].set(title="Immagine originale")
blur = ndimage.gaussian_filter(f1, 5)
ax2[1].imshow(blur, cmap=plt.cm.gray)
ax2[1].set(title="Immagine sfocata")
blur_G = ndimage.gaussian_filter(blur, 1)
alpha = 30
sharp = blur + alpha * (blur - blur_G)
ax2[2].imshow(sharp, cmap=plt.cm.gray)
ax2[2].set(title="Immagine sharpened")
plt.show()

fig4, ax4 = plt.subplots(3)
ax4[0].imshow(f1, cmap=plt.cm.gray)
ax4[0].set(title="Immagine originale")
f_with_noise = f1 + 0.9 * f1.std() * np.random.random(f1.shape)
ax4[1].imshow(f_with_noise, cmap=plt.cm.gray)
ax4[1].set(title="Immagine sfocata")
blur_G1 = ndimage.gaussian_filter(f_with_noise, 1)
ax4[2].imshow(blur_G1, cmap=plt.cm.gray)
ax4[2].set(title="Immagine filtrata")
plt.show()
