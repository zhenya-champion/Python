import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

#Распознавание номерных знаков и их чтение
img = cv2.imread('images/car4.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray,11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
#сортируем, нужные нам контуры вверху, макс 8
cont = sorted(cont, key=cv2.contourArea, reverse=True)#[:8]

#найдём контур отображающий номер
pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True)

    if len(approx) == 4:
        pos = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

#вырезть номер
(x, y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
crop = gray[x1:x2, y1:y2]

#считать номер
text = easyocr.Reader(['en'])
text = text.readtext(crop)
#print(text)
#pl.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
#pl.show()

#выводим надпись на изображении
res = text[0][-2]
final_image = cv2.putText(img, res, (x1 - 200, y2 + 160), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
final_image = cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 2)

pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
pl.show()

#создаем матрицу(изображение) со значениями 0
#photo = np.zeros((300, 300, 3), dtype='uint8')

#photo[:] = 255, 0, 0
#Создание прямоугольника
#cv2.rectangle(photo, (50, 70), (100, 100), (119, 201, 105), thickness=cv2.FILLED)
#Создание линии
#cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)
#Создание круга
#cv2.circle(photo, (photo.shape[0] // 2, photo.shape[1] // 2), 50, (119, 201, 105), thickness=cv2.FILLED)
#Создание текста
#cv2.putText(photo, 'Evgeniy', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 3)

# #показываем изображение (photo[0::100, 0::150] - обрезать изображение)
#cv2.imshow('Photo', photo)
#время показа изображения
#cv2.waitKey(0)


# #читаем изображение
# img = cv2.imread('images/cat.jpg')
# #меняем размер изображения
# img = cv2.resize(img, (350, 500))
# #степень размытия (только нечетные числа)
# img = cv2.GaussianBlur(img, (9, 9),0)
# #конвертация изображения в черно-белый цвет
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #найти углы изображения (уменьшаем точность)
# img = cv2.Canny(img, 100, 100)
#
# #матрица избражения со значением 1
# kernel = np.ones((5, 5), np.uint8)
# #увеличение обводки
# img = cv2.dilate(img, kernel, iterations=1)
# #уменьшить жирность обводки
# img = cv2.erode(img, kernel, iterations=1)
#
# #показываем изображение (img[0::100, 0::150] - обрезать изображение)
# cv2.imshow('result', img)
# #вывести параметры изображения
# #print(img.shape)
#
# #время показа изображения
# cv2.waitKey(0)


# #читаем видео (0 - для обращения к видеокамере)
# cap = cv2.VideoCapture('videos/butterfly.mp4')
# #ширина (для видеокамеры)
# cap.set(3, 500)
# #высота (для видеокамеры)
# cap.set(4,300)

#цикл видео
# while True:
#     success, img = cap.read()
#     cv2.imshow('result', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#читаем изображение
#img = cv2.imread('images/cat.jpg')
#new_image = np.zeros(img.shape, dtype='uint8')
#отзеркаливание
#img = cv2.flip(img, -1)

#вращение
# def rotate(img_param, angle):
#     h, w = img_param.shape[:2]
#     point = (w // 2, h // 2)
#
#     mat = cv2.getRotationMatrix2D(point, angle,1)
#     return cv2.warpAffine(img_param, mat, (w, h))
#img = rotate(img, -90)

#смещение
# def transform(img_param ,x ,y):
#     mat = np.float32([[1, 0, x],[0, 1, y]])
#     return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))
# img = transform(img, 20, 30)

#контуры
#img = cv2.GaussianBlur(img, (5, 5),0) #размытие
#img = cv2.Canny(img, 100, 140) #углы изображения
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #конвертация

#con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #поиск контуров
#рисуемновое изображение
#cv2.drawContours(new_image, con, -1, (0, 200, 0), 1)

#print(con)

#цветовые форматы
#img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#разбить на слои
#r, g, b = cv2.split(img)
#объединить слои
#img = cv2.merge([b, g, r])

#показываем изображение (img[0::100, 0::150] - обрезать изображение)
#cv2.imshow('result', img)
#время показа изображения
#cv2.waitKey(0)

#Побитовые операции
#photo = cv2.imread('images/cat.jpg')
#img = np.zeros(photo.shape[:2], dtype='uint8')

#circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
#square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

#объединяем изображение
#img = cv2.bitwise_and(photo, photo, mask=circle)
#img = cv2.bitwise_or(circle, square)
#img = cv2.bitwise_xor(circle, square)
#img = cv2.bitwise_n(circle)

#показываем изображение (img[0::100, 0::150] - обрезать изображение)
#cv2.imshow('result', img)
#время показа изображения
#cv2.waitKey(0)