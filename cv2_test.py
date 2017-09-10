import cv2
import numpy as np

# for i in range(1):
#     im=np.random.randint(0,255,64*64*3,np.uint8)
#     im=im.reshape([64,64,3])
#     cv2.imshow("windows1",im)
#     cv2.waitKey()

im=cv2.imread('data/test1.jpg')
im=cv2.resize(im,(im.shape[1]/10,im.shape[0]/10))
cv2.imshow('windows2',im)
cv2.waitKey()
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,120)
cv2.imshow('windows2',edges)
# cv2.waitKey()
minL=150
maxLGap=15
lines=cv2.HoughLinesP(edges,1,np.pi/90,100,minL,maxLGap)
# circles=cv2.HoughCircles(edges,cv2.cv.CV_HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=5,maxRadius=0)
# circles=np.uint16(np.around(circles))
show_im=cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(show_im,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.imshow("windows2",show_im)
# cv2.waitKey()
# cv2.destroyAllWindows()

# for i in circles[0]:
#     cv2.circle(show_im,(i[0],i[1]),i[2],(0,0,255),2)

cv2.imshow("windows2",show_im)
cv2.waitKey()