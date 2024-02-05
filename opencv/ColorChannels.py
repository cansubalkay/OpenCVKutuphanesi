#COLOR CHANNELS- RENK KANALLARI
import cv2 as cv
import numpy as np

img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

#img ile aynı boyutlarda siyah bir görüntü oluşturduk. 
blank = np.zeros(img.shape[:2], dtype='uint8')

#görüntüyü BGR renk kanallarına ayırır ve bunları b, g, r adlı değişkenlere atadık.
#cv.split() fonku bir görüntüyü BGR renk kanallarına ayırmak için kullanılır
b,g,r = cv.split(img)

#cv.merge() fonku,ayrı alınan renkleri birleştirmek için kullanılır.Örn, BGR renk uzayında ayrı alınan mavi, yeşil ve kırmızıyı birleştirmek için kullanılabilir.
#aşağıdaki satırda Mavi kanalını alır ve diğer renkleri siyah bir görüntü ile birleştirir, böylece sadece mavi renk kanalı görünür hale gelir.
blue= cv.merge([b,blank,blank])
#aşağıdaki satırda yeşil kanalını alır ve diğer renkleri siyah bir görüntü ile birleştirir, böylece sadece yeşil renk kanalı görünür hale gelir.
green = cv.merge([blank,g,blank])
#aşağıdaki satırda kırmızı kanalını alır ve diğer renkleri siyah bir görüntü ile birleştirir böylece sadece kırmızı renk kanalı görünür hale gelir.
red = cv.merge([blank,blank,r])
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

#print(img.shape)görüntünün boyutunu (yükseklik, genişlik, kanal sayısı) ekrana yazdırır.
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#Ayrılmış renk kanallarını tekrar birleştirerek orijinal görüntüyü elde ederiz.
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)