#Drawing Shapes & Putting Text- Şekil Çizme ve Metin Koyma
import cv2 as cv
import numpy as np
#alttaki 2 satırla; 500x500 boyutunda üç renkli bir görüntü oluşturur. 
blank = np.zeros((500,500,3),dtype = 'uint8') #blank= boşluk
cv.imshow('Blank', blank)

#Resmi belirli bir renge boyamak
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green', blank)
#Dikdörtgen Çizimi cv.rectangle ile yapılır.Parantez içindeki değerlerle oynanarak dikdörtegnin boyutu değiştirlebilir.
#thickness'a 2,5,15 gibi değerler vererek kalınlığı ayarlayabilir ya da cv.FILLED(ya da -1) yazarak şeklin içini full boyayabiliriz
#(0,255,0) renkle alakalı parametreler içindir. blank.shape'li ifadeler koordinatları temsil eder.
#blank.shape[1]//2,resmin genişliğinin yarısını temsil eder.blank.shape[0]//2 resmin yüksekliğinin yarısını temsil eder. yani şekil resmin ortasından başlar
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=-1) #thickness=kalınlık
#dikdörtgenin sol üst köşesi (0,0), sağ üst köşesi ekranın yarısında olacak şekilde belirlendi.
cv.imshow('Rectangle', blank)

#Çember çizimi,cv.circle ile yapılır.
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,(0,0,255), thickness=-1)
cv.imshow('Circle', blank)
#çizgi çizimi, cv.line ile yapılır.
cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,255), thickness=3)
cv.imshow('Line', blank)
#metin yazımı, cv.putText ile yapılır. ilk tırnakta ekrana yazılacak şey ondan sonra da koordinatlar yazılır örn(0,225)
cv.putText(blank, 'Hello', (400,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2) #font; hershey_complex seçilmiş,font büyüklüğü de 1 seçilmiş.
cv.imshow('Text', blank)
cv.waitKey(0)
