import dlib
import cv2

im=cv2.imread('data/test2.jpg')

rects=[]
dlib.find_candidate_object_locations(im,rects,min_size=100)

print rects
for k,d in enumerate(rects):
    im2=im.copy()
    if d.area()>400:
        continue
    cv2.rectangle(im2,(d.left(),d.top()),(d.right(),d.bottom()),(0,0,255),1)
    cv2.imshow("ss",im2)
    cv2.waitKey(100)