#BLURRING
import cv2 as cv
 
img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

#Averaging-Ortalama Bulanıklık;cv.blur() fonku kullanılarak görüntüye ortalama bulanıklık uygulanır
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#Gaussian Blur-Gaussian Bulanıklık; cv.GaussianBlur() fonku kullanılarak görüntüye Gauss (normal) dağılımını kullanarak bulanıklık uygulanır.
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur-Medyan Bulanıklığı;cv.medianBlur() fonku ile görüntüye medyan bulanıklığı uygulanır. 
#Bu, bir pikselin değerinin, etrafındaki bir bölgedeki diğer piksellerin medyanı ile değiştirilmesiyle gerçekleştirilir.
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#Bilateral-Bilateral Filtreleme;cv.bilateralFilter() fonku ile görüntüye bilateral filtre uygulanır.Netlik korunurken gürültü azaltılır.
bilateral = cv.bilateralFilter(img, 10,35,25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)