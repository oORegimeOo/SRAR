import cv2


def findOnlineCamera():
    allCameraIDXAvailable = []
    print("Searching for webcams.")
    for cameraIDX in range(10):
        cap = cv2.VideoCapture(cameraIDX)
        if cap.isOpened():
            allCameraIDXAvailable.append(cameraIDX)
            cap.release()
    return allCameraIDXAvailable


def chooseCamera(allCameraIDXAvailable):
    print("You will see all available webcam streams successively. There are " + str(len(allCameraIDXAvailable))
          + " webcams detected. Choose the one you need to use.")
    print("""Press "n" if you not see the right camera feed. Press "y" if you see the right one.""")
    cam = None
    for IDX in allCameraIDXAvailable:
        cap = cv2.VideoCapture(IDX)
        print("Camera feed of cam " + str(IDX) + ".")
        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            res = cv2.waitKey(1)
            if res == ord('n'):
                print("Next camera feed.")
                break
            if res == ord('y'):
                cam = IDX
                break
        cap.release()
        cv2.destroyWindow('frame')
        if cam is not None:
            break
    if cam is not None:
        print("Camera feed " + str(cam) + " was chosen.")
    else:
        print("No camera feed was selected.")
    return cam


def openCamFeed():
    return cv2.VideoCapture(chooseCamera(findOnlineCamera()))
