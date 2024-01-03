import CameraFeed as Cam
from Server import DataBase as DB


def runSRAR():
    print("Program started!")
    print()
    DB.startDB()
    Cam.startCamFeed()