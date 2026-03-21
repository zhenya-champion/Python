import cv2
import logging
import glob
import os
import time
from datetime import datetime

#Распознавание лиц

#настройка лога
LogFile = f'face_200_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
logging.basicConfig(
    filename=LogFile,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def LoadImage(filename):
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

def main():
    image_files = sorted(glob.glob('images/*.jpg') + glob.glob('images/*.png'))
    #проверка на наличие фото
    if not image_files:
        print("Нет фото")
        return

    total_count = len(image_files)
    print(f"Обработка {total_count} фото!")
    start_time = time.time()
    total_faces = 0
    logging.info(f"Старт: {total_count} фото")

    for i, filename in enumerate(image_files, 1):
        filename_short = os.path.basename(filename)
        filename_result, num_faces, coords = LoadImage(filename)
        total_faces += num_faces
        progress = i / total_count * 100
        print(f"\r {i}/{total_count} ({progress:.1f}%) | Лиц: {total_faces} | {filename_short}", end="")
        logging.info(f"{i:3d}. {filename_short}: {num_faces} лиц")
        for j, (x, y, w, h) in enumerate(coords):
            logging.info(f"Лицо {j + 1}: x={x}, y={y}, w={w}, h={h}")

    elapsed = time.time() - start_time
    print(f"\nГотово за {elapsed:.1f}с ({elapsed / 60:.1f}мин)")
    print(f"Всего: {total_faces} из {total_count} файлов")
    print(f"Результат: папка output/")
    print(f"Лог: {LogFile}")

if __name__ == "__main__":
    main()
