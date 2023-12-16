import CameraFeed as Cam
import DataBase as DB

def runSRAR():
    print("Program started!")
    print()
    DB.startDB()
    Cam.startCamFeed()