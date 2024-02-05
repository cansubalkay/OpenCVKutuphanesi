#HISTOGRAM COMPUTATION
import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np

img = cv.imread ('Photos/manzara.jpg')
cv.imshow('Manzara', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255,-1)

#cv.circle() ile, görüntünün merkezine yerleştirilmiş bir dairenin maskesi oluşturulur ve "Mask" adı altında gösterilir.
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2),100, 255,-1)
cv.imshow('Mask', mask)

#Grayscale histogram
#cv.calcHist() ile gri tonlu görüntü üzerinde histogram hesaplanır.Sonra, hesaplanan histogram matplotlib kütüphanesi kullanılarak görselleştirilir.
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256] )

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


#Colour Histogram-Renkli Histogramın Hesaplanması ve Görselleştirilmesi: 
#Her bir renk kanalı için ayrı histogramlar hesaplanır ve matplotlib kütüphanesi kullanılarak görselleştirilir.
plt.figure() #yeni bir çizim alanı oluşturulur.

# başlık ve eksen isimleri belirlenir.
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

#colors adında bir renk listesi tanımlanır. Sonra bir döngü yardımıyla her bir renk kanalı için histogram hesaplanır. 
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256]) #plt.xlim() ile x ekseninin limitleri belirlenir. Bu, histogramın sınırlarının 0 ve 256 arasında olduğunu gösterir.

plt.show()
cv.waitKey(0)