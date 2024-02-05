#RESIZING AND RESCALLING FRAMES- Çerçeveleri yeniden boyutlandırma ve yeniden ölçeklendirme
import cv2 as cv
#rescaleFrame adında bir fonksiyon tanımlanır. Bu fonksiyon, bir çerçevenin boyutunu yeniden boyutlandırmak için kullanılır. 
img = cv.imread('Photos/manzara.jpg')
cv.imshow('Manzara', img)

#Boyutların değişikliği için bir fonksiyon oluşturulur.
def rescaleFrame(frame, scale=0.75): #scale=ölçek
    #bu fonk resimlerde, videolarda ve canlı videolarda kullanılabilir.
    width = int(frame.shape[1] * scale) #Yeniden boyutlandırılmış genişliği hesaplar
    height = int(frame.shape[0]* scale) #Yeniden boyutlandırılmış yüksekliği hesaplar
    dimensions = (width, height) #dimensions=boyutlar
#cv.resize fonksiyonu çerçeveyi yeni boyutlara yeniden boyutlandırır
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

def changeRes(width,height):
    #canlı videolarda kullanılabilir.
    capture.set(3,width)
    capture.set(4,height)
    
    #Aşağıdaki iki satırla boyut için oluşturduğumuz fonksiyonu kullanarak resmi yeni boyutuyla Image penceresinde açtırırız.
img_resized = rescaleFrame(img)
cv.imshow('Image', img_resized)
#video okuyucu
capture = cv.VideoCapture('Videos/WIN_20240203_14_49_01_Pro.mp4')
#while true ile videonun okundugundan emin oluruz. Eğer video açılmazsa direkt döngüye girmeyecektir.
while True:
    isTrue, frame = capture.read()
    #burada önceden oluşturduğumuz rescaleFrame fonksiyonu kullanılır.
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame) #orjinal boyutlardaki videoyu gösterir
    cv.imshow('Video Resized', frame_resized)  #Yeniden boyutlandırılmış çerçeveyi gösterir
    if cv.waitKey(20) & 0xFF==ord('d'): #Klavyeden 'd' tuşuna basılıp basılmadığını kontrol eder. Eğer 'd' tuşuna basılmışsa döngüyü sonlandırır.
        break
capture.release()
# release() ;video dosyasının kaynaklarını serbest bırakır ve VideoCapture nesnesini kapatır. 
#Bu şekilde, bellek sızıntısını önler ve sistem kaynaklarını düzgün bir şekilde yönetir.

cv.destroyAllWindows
cv.waitKey(0)
#BU KOD CALISTIGINDA BİR FOTO VE VİDEOYU FARKLI BOYUTLARLA FARKLI PENCERELERDE VERİR.
