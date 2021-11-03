import cv2

imagen = cv2.imread("resources/lena.png",0)
cv2.imshow("Output",imagen)
cv2.imwrite("lenagris.png",imagen)
cv2.waitKey(0)
#Leer una imagen y ponerla en gris


