import cv2

#Распознавание лиц
img = cv2.imread('images/013933.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier('face.xml')
result = face.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=5) #координаты найденых объектов

for(x, y, w, h) in result:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow('Result', img)
cv2.waitKey(0)