from pickletools import uint8

import cv2
import numpy as np

#создаем матрицу(изображение) со значениями 0
photo = np.zeros((300, 300, 3), dtype='uint8')

# #показываем изображение (photo[0::100, 0::150] - обрезать изображение)
cv2.imshow('Photo', photo)
#время показа изображения
cv2.waitKey(0)


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