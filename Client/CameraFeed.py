import cv2
import Client.Client as Client
import Client.SeenPeople as SP
import Client.Style as Style

def startCamFeed():
    person = SP.Person()
    feed = openCamFeed()
    while True:
        ret, frame = feed.read()
        face = faceDetection(frame)
        if len(face) > 0:
            for (x, y, w, h) in face:
                if abs(person.getX() - x) > 20:
                    person.setX(x)
                    person.setW(w)
                if abs(person.getY() - y) > 20:
                    person.setY(y)
                    person.setH(h)
        #cv2.rectangle(frame, (faceRec[0], faceRec[1]), (faceRec[0] + faceRec[2], faceRec[1] + faceRec[3]), (0, 255, 0), 2)
        qrcode = detectionOfQRCodeInPicture(frame)
        if qrcode is not None:
            if "SRAR_id_" in qrcode:
                person.proofNewPerson(Client.client_program(qrcode[8:]))
            if "SRAR_end" in qrcode:
                print("")
                print("Termination send!")
                print("")
                print(Client.client_program(qrcode[5:]))
                break
        if person.getIdx() is not None:
            cv2.putText(frame, person.getUpperText(), (person.getX()+int(person.getW()/2)-(14*int(len(person.getUpperText())/2)), person.getY()), Style.getFont(), Style.getScale(), Style.getColor())
            cv2.putText(frame, person.getLowerText(), (person.getX()+int(person.getW()/2)-(14*int(len(person.getLowerText())/2)), person.getY()+person.getH()), Style.getFont(), Style.getScale(), Style.getColor())
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    print("")
    print("Client closed.")

def openCamFeed():
    return cv2.VideoCapture(chooseCamera(findOnlineCamera()))

def chooseCamera(allCameraIDXAvailable):
    print("You will see all available webcam streams successively. There are " + str(len(allCameraIDXAvailable))
          + " webcams detected. Choose the one you need to use.")
    print("""Press "n" if you not see the right camera feed. Press "y" if you see the right one.""")
    cam = None
    for IDX in allCameraIDXAvailable:
        cap = cv2.VideoCapture(IDX)
        #print("Camera feed of cam " + str(IDX) + ".")
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

def findOnlineCamera():
    allCameraIDXAvailable = []
    print("Searching for webcams.")
    for cameraIDX in range(10):
        cap = cv2.VideoCapture(cameraIDX)
        if cap.isOpened():
            allCameraIDXAvailable.append(cameraIDX)
            cap.release()
    return allCameraIDXAvailable

def faceDetection(image):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    return faces

def detectionOfQRCodeInPicture(image):
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    if points is not None:
        return decodedText
    else:
        return None