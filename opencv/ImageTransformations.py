import cv2 as cv
import numpy as np

img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)
 #Translation-Çevirme
#görüntüyü belirli bir mesafede dikey ve yatay olarak kaydırmak için translate adında bir fonk oluşturduk.
def translate(img, x,y):
#transMat, kaydırma matrisini oluşturur. 'x' ve 'y' parametreleri, yatay ve dikey kaydırma miktarını gösterir.
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
#cv.warpAffine fonku,görüntüyü afin dönüşüm matrisiyle dönüştürmeye yarar.
#Afin dönüşüm, görüntüyü kaydırma, döndürme, ölçeklendirme ve yansıtma gibi işlemleri içerir
    return cv.warpAffine(img, transMat, dimensions)
#-x=Left, -y = Up, x=Right, y=Down
translated =translate(img, -100,100) #translate fonksiyonunu çağırarak görüntüyü (-100, 100) koordinatlarına göre kaydırır.
cv.imshow('Translated', translated)
#Rotation
# rotate adında bir fonk tanımladık. Bu fonk bir görüntüyü belirli bir açıda döndürmek için kullanılır.
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint= (width//2,height//2)
#cv.getRotationMatrix2D fonksiyonu, bir 2D dönüş matrisi oluşturmak için kullanılır. 
#bu fonktaki parantez içindeki parametrelerden ilki dönüşümün merkezinin koordinatları, ikincisi açıyı, üçüncüsü ölçeği verir.
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45) # 'rotate' fonksiyonunu çağırarak görüntüyü -45 derece açıyla döndürür.
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img,-90) #'rotate' fonksiyonunu çağırarak görüntüyü -90 derece açıyla döndürür.
cv.imshow('Rotated Rotated', rotated_rotated)
#Resizing-cv.resize fonku; Görüntüyü yeniden boyutlandırır. İlk parametre olarak işlenecek görüntüyü alırken, ikinci olarak hedef boyutları alır.
#interpolation,işlem sırasında kullanılacak yöntemini belirtir. Burada, INTER_CUBIC yöntemi kullanıldı.
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
#Flipping; cv.flip fonku, görüntüyü yatay ve dikey olarak çevirir. İlk parametre işlenecek görüntüyü alırken,2. çevirme yöntemini belirtir.1,0,-1 vb.
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)
#Cropping- kırpma
cropped = img[200:400,300:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)