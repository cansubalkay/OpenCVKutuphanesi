import cv2 as cv

img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)
#1 griye dönüştürme, cvtColor ile yanındaki paranteze istenilen renk parametresi yazılarak görselin renkleriyle oynanabilir
gray= cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow('Gray', gray)
#2Bulanıklaştırma -blur. cv.GaussianBlur ile yapılır. parantez içiyle blur yoğunluğu ve şekli değiştirilebilir.
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)
#3 cv.Canny fonksiyonu; resimdeki yoğunluk değişikliklerini belirler ve bu değişikliklerin büyük ve keskin olanlarını kenar olarak tanımlar
#parantez içindeki değerler arttırıp azaltılarak daha ayrıntılı sonuçlar elde edilebilir.
canny = cv.Canny(img, 5, 175)
cv.imshow('Canny Edges', canny)
#4Görüntüyü genişletme-Dİlating the image- cv.dilate ile yapılır
#Genellikle kenar tespiti sonrası(canny) görüntü işleme işlemlerinde kullanılır.
#Bir görüntüdeki foreground(beyaz) genişlemesini sağlar,background(siyah) küçülmesine yol açar.
#parantez içinde işlem yapılacak görüntü ve işlemin hassaslıgı yer alır. iterasyon arttıkca beyazlık da artar. 
dilated = cv.dilate(canny, (300,300), iterations=1)
cv.imshow('Dilated', dilated)
#Eroding-Aşınma, cv.erode ile yapılır. genellikle kenar tespiti sonrası görüntü işleme işlemlerinde kullanılır.
#beyaz nesnelerin (foreground) küçülmesini sağlar ve siyah nesnelerin (background) genişlemesine yol açar.
#görüntünün düzensiz kenarlarını sertleştirmek, ince detayları ortadan kaldırmak veya nesneleri ayırmak gibi birçok farklı amaçla kullanılabilir
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)
#Resize-yeniden boyutlandırma-cv.resize ile yapılır
resized = cv.resize(img, (960,740))
cv.imshow('Resized', resized)
#Cropping-Kırpma. Resmi belirtilen yerlerinden kırpar. Kapalı parantez olmalı!
cropped = img[50:550, 20:400]#Burada 50 ile 550 satırları arasını ve 20 ile 400 sütunları arasını alır.
cv.imshow('Cropped', cropped)


cv.waitKey(0)