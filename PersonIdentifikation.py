import cv2


def detectionOfQRCodeInPicture(image):
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    if points is not None:
        return decodedText
    else:
        return None

