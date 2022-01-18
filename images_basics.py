import cv2
import os
import matplotlib.pyplot as plt

os.system('cls')

#################### Read image ####################
img_path = os.path.join('data', 'images')
print('image path : ', img_path)

img = cv2.imread(f'{img_path}/rem.jpg')
print('image shape : ', img.shape)
heigth, width, channels = img.shape

img2 = cv2.imread(f'{img_path}/lily.jpg')
print('image2 shape : ', img2.shape)
heigth2, width2, channels2 = img2.shape

################### Render image ###################
save_path = os.path.join('data', 'output', 'Lesson_1')

plt.figure()
plt.imshow(img)
plt.savefig(f'{save_path}/imshow1.jpg')

recolor = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(recolor)
plt.savefig(f'{save_path}/imshow1_recolored.jpg')

plt.figure()
plt.imshow(img2)
plt.savefig(f'{save_path}/imshow2.jpg')

recolor2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(recolor2)
plt.savefig(f'{save_path}/imshow2_recolored.jpg')

cv2.imwrite(f'{save_path}/grayscaled.jpg', recolor2)