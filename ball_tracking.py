from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2

# citim imaginea

begin=time.time()

img = cv2.imread('ball on black background.png')
# Afisam imaginea originala
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap= 'gray')
begin=time.time()

h, w = gray.shape
print(h)
print(w)
sum2 = 0;
sum1 = 0
a = np.empty(h, dtype=int)
for i in range(h):
    for j in range(w):
        sum1 += gray[i,j]
    a[i] = sum1  
    sum1 = 0
   
y_pos = np.argmax(a)


b = np.empty(w, dtype=int)
for i in range(w):
    for j in range(h):
        sum2 += gray[j,i]
    b[i] = sum2  
    sum2 = 0
    
x_pos = np.argmax(b)

end=time.time()    

for j in range(5):
    for i in range(h):
        img[i,x_pos + j] = [0,255,0]
  
for j in range(5):
    for i in range(w):
        img[y_pos + j,i] = [0,255,0]

      
plt.imshow(img)    


        

# printeaza timpul de executie al prelucrarii efective
end=time.time()

print('timp executie: ',end-begin)