import cv2
import numpy as np
rgb= cv2.imread("resources/lena.png")
c1=rgb[:,:,0]
c2=rgb[:,:,1]
c3=rgb[:,:,2]
cv2.imshow("RGB",np.hstack([c1,c2,c3]))
cv2.waitKey(0)
cv2.destroyAllWindows()