import cv2
import logging
import glob
import os
import time
from datetime import datetime

# #Распознавание лиц

# Настройка лога
log_filename = f'face_detection_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
def process_image(filename):
    img = cv2.imread(filename)
    if img is None:
        logging.error(f"Не найдено: {filename}")
        return filename, 0, []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(30, 30))

    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

    os.makedirs("output", exist_ok=True)
    output_path = f"output/{os.path.basename(filename)}"
    cv2.imwrite(output_path, img)

    return filename, len(faces), faces

img = cv2.imread('images/013933.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier('face.xml')
result = face.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=5) #координаты найденых объектов

cv2.imshow('Result', img)
cv2.waitKey(0)