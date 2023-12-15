import cv2


def faceDetection(image):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    return faces
