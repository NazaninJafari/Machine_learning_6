import cv2
import webbrowser

cap = cv2.VideoCapture(0)
qrCodeDetector = cv2.QRCodeDetector()

while True:
    
    ret, frame = cap.read()

    if not ret:
        break
    
    #Detecting and Decoding a QRCode
    decodedText, points, _ = qrCodeDetector.detectAndDecode(frame)

    #If there are no points, it means no QR Code was not found in the image.
    if decodedText:
        x, y, w, h = cv2.boundingRect(points[0])
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 6)
        cv2.putText(frame, decodedText, (x+30, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)

        
        if key != 27: #esc
            webbrowser.open(str(decodedText))

    key = cv2.waitKey(1)
    if key == 27: #Esc
        break

    cv2.imshow('QR code Reader', frame)


cap.release()
cv2.destroyAllWindows()