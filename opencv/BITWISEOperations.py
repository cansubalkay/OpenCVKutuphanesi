#BITWISE OPERATIONS- Bit Düzeyinde İşlemler
import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

#cv.rectangle() ve cv.circle() fonksiyonları kullanılarak blank üzerine birer dikdörtgen ve daire çizilir.
# Dikdörtgenin içi dolu olacak şekilde çizilmesi için kalınlık parametresi -1 olarak belirlenir.
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#Bitwise AND -- intersecting regions-kesişen bölgeler-cv.bitwise_and() fonksiyonu, dikdörtgen ve dairenin kesişen bölgelerini bulur.
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

#Bitwise OR-- non-intersecting and intersecting regions-kesişmeyen ve kesişen bölgeler
#cv.bitwise_or() fonksiyonu, dikdörtgen ve dairenin birleşen (kesişen ve kesilmeyen) bölgelerini bulur.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#Bitwise XOR  -- non-intersecting regions-kesişmeyen bölgeler
#cv.bitwise_xor() fonksiyonu, dikdörtgen ve dairenin kesişmeyen bölgelerini bulur.
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#Bitwise NOT-- cv.bitwise_not() fonksiyonu, dikdörtgenin tersini alır. Yani, siyah pikseller beyaza, beyaz pikseller ise siyaha dönüştürülür.
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle NOT', rectangle)




cv.waitKey(0)