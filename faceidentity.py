import cv2

from cv2 import VideoCapture

VideoCapture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml')

while True:

    success, img = VideoCapture.read()
    print(success)

    if success:
        face_loc = face_cascade.detectMultiScale(img, 1.1, 4)
        print(face_loc)

        for x, y, w, h in face_loc:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

            cv2.imshow("My image", img)
            key = cv2.waitKey(2)
            if key == 32:
                print("stopping")
                break

VideoCapture.release()
cv2.destroyAllWindows()