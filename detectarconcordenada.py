import cv2
import numpy as np

captura=cv2.VideoCapture(0)

azulBajo= np.array([100,100,20],np.uint8)
azulAlto= np.array([125,255,255],np.uint8)
while True:
    ret,frame=captura.read()
    if ret==True:
        frameHSV= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask= cv2.inRange(frameHSV,azulBajo,azulAlto)
        contornos,_= cv2.findContours(mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            area=cv2.contourArea(c)
            if area > 3000:
                nuevoContorno=cv2.convexHull(c)
                cv2.drawContours(frame,[c], 0 ,(255,0,0),3)

        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
cap.release()
cv2.destroyAllWindows()