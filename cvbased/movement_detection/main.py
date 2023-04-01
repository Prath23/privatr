import cv2
import time
import imutils

cam= cv2.VideoCapture(0)
time.sleep(1)
firstFrame=None
area=500

while True:

    _,img=cam.read()
    img=imutils.resize(img,width=500,height=500)
    if firstFrame is None:
        firstFrame=img
        continue
    imgDiff= cv2.absdiff(firstFrame,img)
    threshold_img = cv2.threshold(imgDiff, 20, 250, cv2.THRESH_BINARY)[1]
    threshold_img= cv2.dilate(threshold_img,None,iteration=2)
    cv2.imshow("cam",img)
    key= cv2.waitKey(2) & 0xFF
    if key == "a":
        break
cam.release()
cv2.destroyAllWindows()



