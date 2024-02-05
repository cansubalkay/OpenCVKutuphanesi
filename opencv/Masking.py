#MASKING
import cv2 as cv
import numpy as np 

img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

blank =np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank Image', blank)

#cv.circle() ve cv.rectangle() ile iki farklı şekil oluşturulur. cv.bitwise_and() ile bu iki şeklin kesişimini bulanak bir maske oluşturulur
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
#cv.imshow('Mask', mask)
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

#mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100,255,-1)
#cv.imshow('Mask', mask)


#orijinal görüntü ile oluşturulan maske arasındaki kesişim elde edilir ve bu maskeleme işlemi sonucu elde edilen görüntü gösterilir.
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow ('Masked Image', masked)



cv.waitKey(0)