import cv2
import numpy as np

for i in range(100):
    im=np.random.randint(0,255,64*64*3,np.uint8)
    im=im.reshape([64,64,3])
    cv2.imshow("windows1",im)
    cv2.waitKey()