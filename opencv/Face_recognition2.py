#Face Recognition with OpenVC's built-in recognizer bölümünün 2. dosyası
import numpy as np
import cv2 as cv

#Yüz tespiti için kullanılacak olan Haar kaskadını (Haar Cascade) yükler. Bu dosya önceden hazırlanmış bir dosyadır. opencv kütüphanesinden aldım.
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#yüzü tanınacak insanların adlarını içeren bir liste oluşturduk.
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

#bu fonk ile yüz tanıma oluşturulur. LBPH (Local Binary Patterns Histograms) algoritması kullanılarak eğitilmiş bir yüz tanıma algoritmasıdır.
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Daha önceden yazılmış dosyadır. Bu satır modelin yüklenmesini sağlar.
face_recognizer.read('face_trained.yml')

#Tanınacak olan yüzün bulunduğu görüntüyü okur. burada Elton John klaösründeki Elton1 görüntüsünü okur.
img = cv.imread(r'C:\Users\cansu\Desktop\opencv\Faces\train\Elton John\Elton1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#Görüntüde yüzleri tespit eder. Haar ı kullanarak belirli bir ölçekte yüzleri tespit eder.
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

#Tespit edilen her yüz için for döngüsü oluşturduk. (x,y) koordinatlarında başlayan ve w genişliğinde, h yüksekliğinde bir dikdörtgen olur
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

#Tanınan kişinin adını cv.putText fonku ile görüntüye yazar
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

    #Tanınan yüzün etrafına bir dikdörtgen çizer. burada dikdörtgenin kalınlıgı 2 olarak alınmış
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)