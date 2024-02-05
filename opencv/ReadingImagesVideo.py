#READING IMAGES AND VIDEO- FOTOGRAF VE VIDEOLARI OKUMA
#Daha kolay çalışmak için kullanılacak resim ve videolar kaynak kodun oldugu dizine taşınabilir.
import cv2 as cv 
#imread ile belirtilen resim okunur.
img = cv.imread('Photos/manzara.jpg')
#imshow ile resim gösterilir.Parantez içindeki ilk parametre açılan pencerenin adı olur, ikincisi de hangi resmin açılacağını belirtir.
cv.imshow('Manzara', img)
#waitKey(0) ile sıfıra basana kadar pencere açık kalır. Aksi takdirde hemen kapanır.Örn:  500 yazarsak da yarım sn açık kalır
#VideoCapture ile video okunur.
capture = cv.VideoCapture('Videos/WIN_20240203_14_49_01_Pro.mp4')
#while true ile videonun okundugundan emin oluruz. Eğer video açılmazsa direkt döngüye girmeyecektir.
while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)
#0xFF binary sistemle alakalı bir şey
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
#video dosyasının kaynaklarını serbest bırakır ve VideoCapture nesnesini kapatır. 
#Bu şekilde, bellek sızıntısını önler ve sistem kaynaklarını düzgün bir şekilde yönetir.
capture.release()
cv.waitKey(0)
#destroyAllWindows ile bütün pencereler kapanır.
cv.destroyAllWindows
