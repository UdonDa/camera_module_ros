# coding:utf-8

import cv2
import os

# カスケードファイル
cascade_path = "haarcascade_frontalface_alt.xml"

cascade = cv2.CascadeClassifier(cascade_path)


# カメラセット
cap = cv2.VideoCapture(0)

color = (255, 255, 255)

counter = True

while(counter):

    # フレーム取得
    ret, frame = cap.read()

    # 物体認識
    face_detect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))

    for rect in face_detect:
        cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

    # 表示
    cv2.imshow("Face Detection", frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

