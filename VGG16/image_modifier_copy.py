# reference - http://datahacker.rs/how-to-access-and-edit-pixel-values-in-opencv-with-python/

import cv2
import matplotlib.pyplot as plt
import numpy as np

#display image
img = cv2.imread('mug.jpg',1)
img = cv2.resize(img,(224,224))
cv2.imshow(' ',img)
cv2.waitKey(0)


def find_mask(x, p=2/32):
    sp=x.shape
    print(sp)
    print(p)
    h=int(sp[0]*p)
    print(h)
    if h<1: h=1
    tmp_x=x.copy()
    bg_x=x.copy()

    for iindex, _ in np.ndenumerate(x):
        i0=iindex[0]
        i1=iindex[1]
        region=tmp_x[ np.max([i0-h,0]) : np.min([i0+h, sp[0]]), np.max([i1-h,0]):np.min([i1+h,sp[1]])]
        v=np.min(region)
        for j in range(0, (sp[2])):
            #bg_x[i0][i1][j]=v
            bg_x[i0][i1][j]=np.mean(region[:,:,j])
    print('line # 34')
    return bg_x

print(img.shape)
p=(2.0/32)
print()
modified_img = find_mask(img,p)
cv2.imshow(' ',modified_img)
cv2.waitKey(0)

# #modify a part of image -- gray out a specific area
# img[40:80, 140:340] = [0,0,0]
# cv2.imwrite('modified8_masked.jpg',img)
# img[60:250, 80:120] = [0,0,0]  # length, width
# cv2.imwrite('modified10_masked.jpg',img)
# cv2.imshow('Modified Image',img)
# cv2.waitKey(0)