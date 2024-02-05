#FACE DETECTION-Yüz Tanıma
import cv2 as cv 

img = cv.imread('Photos/cate.jpg')
cv.imshow('Person', img)
 
#Gri tonlamalı görüntü, yüz tespiti gibi işlemlerde kolaylık sağlar
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

#cv.CascadeClassifier fonku ile önceden yüz tespiti için oluşturulan haar_face.xml dosyası yüklenir
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#Gri tonlamalı görüntüde yüzleri tespit eder. detectMultiScale metodu bir nesnenin görüntü üzerinde farklı boyutlardaki konumlarını tespit eder
#scaleFactor ve minNeighbors parametreleri, yüz tespiti algoritmasının hassasiyetini ve doğruluğunu etkiler.
#Karışık fotolarda yüzlerin daha iyi algılanması açısından minNeighbors değeri küçültülebilir.
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

#tanınan yüzlerin sayısını yazdırır
print(f'Number of faces found ={len(faces_rect)}')

#Tespit edilen her yüz için for döngüsü oluşturduk. (x,y) koordinatlarında başlayan ve w genişliğinde, h yüksekliğinde bir dikdörtgen belirtir
for (x,y,w,h) in faces_rect:
    #Tespit edilen yüzün etrafına bir dikdörtgen çizer. (0,255,0) parametresi burada yeşili ifade eder.
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)