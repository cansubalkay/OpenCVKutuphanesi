#EDGE DETECTION
import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Laplacian--> cv.Laplacian() fonku kullanılarak görüntünün Laplacian kenar tespiti gerçekleştirilir. Sonuç olarak, bir kenar haritası elde edilir.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel-->cv.Sobel() fonksiyonu kullanılarak görüntünün Sobel kenar tespiti gerçekleştirilir.
#Hem dikey (sobelx) hem de yatay (sobely) kenarlar ayrı hesaplanır.
#Sonra, bu sonuçlar birleştirilerek (cv.bitwise_or()) kombinasyonlu bir Sobel kenar haritası elde edilir.
sobelx= cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)
 
#cv.Canny() fonksiyonu kullanılarak Canny kenar tespiti gerçekleştirilir.
#Bu yöntem, gürültülü çevrelerde iyi sonuçlar verir ve aynı zamanda birden çok kenarı tespit etmek için daha hassas olabilir.
canny = cv.Canny(gray,150,175)
cv.imshow('Canny', canny)

cv.waitKey(0)
#Her bir kenar tespiti yöntemi, farklı koşullar altında farklı sonuçlar verebilir. 
#Hangi yöntemin kullanılacağı, belirli bir uygulamanın gereksinimlerine ve veri setinin özelliklerine bağlı olabilir.