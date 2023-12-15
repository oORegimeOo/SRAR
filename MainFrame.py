import CameraFeed as Cam
import HelperFunctions as Hlp
import PersonIdentifikation as PI
import cv2
import DataBase as DB

def runSRAR():
    print("Program started!")
    print()
    DB.startDB()


#    feed = Cam.openCamFeed()
#    xOld = 0
#    yOld = 0
#    wOld = 0
#    hOld = 0

#    while True:
#        ret, frame = feed.read()
#        face = Hlp.faceDetection(frame)
#        if len(face) > 0:
#            for (x, y, w, h) in Hlp.faceDetection(frame):
#                if abs(xOld - x) > 20:
#                    xOld = x
#                    wOld = w
#                if abs(yOld - y) > 20:
#                    yOld = y
#                    hOld = h
#        cv2.rectangle(frame, (xOld, yOld), (xOld + wOld, yOld + hOld), (0, 255, 0), 2)
#        font = cv2.FONT_HERSHEY_SIMPLEX
#        fontScale = .75
#        fontColor = (255, 255, 0)
#        cv2.putText(frame, "Name: " + "Gerd", (xOld, yOld), font, fontScale, fontColor)
#        cv2.imshow('frame', frame)
#        qrcode = PI.detectionOfQRCodeInPicture(frame)
#
#        if qrcode is not None:
#            if "SRAR_id_" in qrcode:
#                print(qrcode[8:])
#        if cv2.waitKey(1) == ord('q'):
#            break

