#CONTOUR DETECTION- 
import cv2 as cv
import numpy as np 
 
img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

#resim ile aynı boyuta ve veri tipine sahip siyah bir görüntü oluşturur. Bu, kontur çizme işlemi için bir arka plan oluşturur.
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Gri tonlamalı resme Gauss bulanıklığı uygular
blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Gri tonlamalı görüntüyü ikili bir eşikleme yöntemi kullanarak ikili bir görüntüye dönüştürür. Eşik değeri 125 olarak belirlenmiştir.
#cv.threshold gri tonlamalı görüntüyü eşik değerine göre ikili bir görüntüye dönüştürmek için kullanılır.
ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

#Kenarlar bulunur ve kontur bilgileri 'contours' değişkenine atanır.
#cv.findContours fonku ikili görüntü üzerindeki nesnelerin konturlarını(sınırlarını)bulmak için kullanılır.Bu,nesneleri algılamak,tanımak,izlemek vb. uygulamada kullanılabilir.
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

#Siyah arka plan üzerine tüm konturları çizer. Çizgi rengi kırmızı, kalınlık 1 olarak belirlenmiştir.
cv.drawContours(blank, contours, -1,(0,0,255),1)
cv.imshow('ContoursDrawn', blank)



cv.waitKey(0)