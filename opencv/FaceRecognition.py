#FACE RECOGNITION WITH OPENCV's BUILT-in RECOGNIZER-
import os
import cv2 as cv 
import numpy as np 

# insanların adlarını içeren bir liste oluşturduk.
people = ['Ben Afflek', 'Elton John','Jerry Seinfield', 'Madonna', 'Mindy Kaling']

#verilerinin bulunduğu dizinin yolu verilir.
DIR = r'C:\Users\cansu\Desktop\Faces\train' 

#Yüz tespiti için önceden yazılan haar_face.xml dosyası yüklenir.
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#Yüz görüntülerinin özelliklerini ve etiketlerini depolamak için boş listeler oluşturduk.
features = []
labels = []

#veri setini oluşturmak için create_train adında bir fonksiyon tanımladık
def create_train():
    # Her bir kişi için eğitim verileri oluşturulur.
    for person in people:
        path = os.path.join(DIR, person) #Her kişinin eğitim verilerinin bulunduğu dizinin yolu belirlenir.
        label = people.index(person) # Kişinin etiketi, 'people' listesindeki konumu olarak belirlenir.

        for img in os.listdir(path): # Kişinin eğitim verilerinin bulunduğu dizindeki her bir görüntü dosyası için bir döngü oluşturulur.
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path) #Görüntü dosyası okunur ve bir diziye dönüştürülür.
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

#scaleFactor ve minNeighbors parametreleri, yüz tespitinde kullanılan ölçek faktörü ve minimum komşu sayısıdır.
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4 )

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] #Görüntüden yüz bölgesi (ROI - Region of Interest) çıkarılır.
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------')

#features ve labels listeleri NumPy dizilerine dönüştürülür
features = np.array(features, dtype='object')
labels = np.array(labels)

#Yüz tanıma algoritması olan LBPH (Local Binary Patterns Histograms) kullanılarak bir yüz tanıma nesnesi oluşturulur.
#!!!EĞER cv.face.LBPHFaceRecognizer_create() fonku hata verirse, opencv contrib i silip baştan yüklemeyi deneyebilirsiniz.
face_recognizer = cv.face.LBPHFaceRecognizer_create()


face_recognizer.save('face_trained.yml') # Eğitilmiş yüz tanıma modeli 'face_trained.yml' adıyla kaydedilir.

#Eğitim verileri NumPy dizileri olarak 'features.npy' ve 'labels.npy' dosyalarına kaydedilir.
np.save('features.npy', features)
np.save('labels.npy', labels)
