import cv2

__font = cv2.FONT_HERSHEY_SIMPLEX
__fontScale = .75
__fontColor = (255, 255, 0)

def getFont():
    return __font

def getScale():
    return __fontScale

def getColor():
    return __fontColor