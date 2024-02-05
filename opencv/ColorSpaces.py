#COLOR SPACES-
import cv2 as cv
import matplotlib.pyplot as plt

img= cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV; BGR görüntüyü HSV (Ton, Doyma, Parlaklık)ye dönüştürür 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*a*b; BGR görüntüyü LAB (Açıklık, Yeşil-Mavi, Kırmızı-Yeşil)e dönüştürür
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB) 
cv.imshow('LAB',lab)

#BGR to RGB; BGR görüntüyü RGB (Kırmızı, Yeşil, Mavi)ye dönüştürür
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV to BGR;HSV'ye dönüştürülen görüntüyü tekrar BGR' a dönüştürür
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR', hsv)


#plt.imshowu rgb parametresiyle kullandık çünkü Matplotlib RGB (Kırmızı, Yeşil, Mavi) renk uzayını kullanır.
#OpenCV BGR(Mavi,Yeşil,Kırmızı) renk uzayını kullanır.Bu yüzden bgr ı rgb ye çevirdiğimiz değişkeni kullanırız. Yoksa grafikte farklı renk resim çıkar
plt.imshow(rgb)
plt.show()


cv.waitKey(0)