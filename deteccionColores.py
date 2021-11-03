import cv2
import numpy as np
captura=cv2.VideoCapture(0)

rojobajo1=np.array([0,100,20],np.uint8)
rojoalto1=np.array([0,255,255],np.uint8)
rojobajo2=np.array([175,100,20],np.uint8)
rojoalto2=np.array([179,255,255],np.uint8)

while True:
    ret,frame=captura.read()
    if ret==True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskrojo1=cv2.inRange(frameHSV,rojobajo1,rojoalto1)
        maskrojo2 = cv2.inRange(frameHSV, rojobajo2, rojoalto2)
        maskrojo=cv2.add(maskrojo1,maskrojo2)
        maskrojoview=cv2.bitwise_and(frame,frame,mask=maskrojo)
        cv2.imshow("maskrojoview",maskrojoview)
        cv2.imshow("maskrojo",maskrojo)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
captura.release()
cv2.destroyAllWindows()