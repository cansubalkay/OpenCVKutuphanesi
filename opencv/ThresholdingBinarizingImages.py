#THRESHOLDING / BINARIZING IMAGES-EŞİKLEME / İKİLİ GÖRÜNTÜLEME
import cv2 as cv 

img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding-Basit Eşikleme-cv.threshold() fonksiyonu kullanılarak, gri tonlamalı görüntüye basit eşikleme uygulanır.
# İkinci parametre eşik değeri, üçüncü parametre maksimum değer ve dördüncü parametre ise eşikleme yöntemini belirtir. 
threshold, thresh = cv.threshold(gray,150,255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

#Ters Basit Eşikleme-Inverse Simple Thresholding-Aynı eşikleme işlemi, ancak ters eşikleme için yapılır
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

#Adaptive Thresholding-uyarlanabilir Eşikleme- cv.adaptiveThreshold() fonku ile uyarlanabilir eşikleme uygulanır.Görüntünün farklı bölgelerine farklı eşik değerleri uygulanır.
#Aşağıda cv.ADAPTIVE_THRESH_MEAN_C parametresi ile ortalama değer kullandık, cv.THRESH_BINARY parametresi ile eşikleme yöntemi belirtilir
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
