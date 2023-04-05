import imutils
import cv2

black_low= (0,0,0)
black_high=(300,260,20)

cam = cv2.VideoCapture(0)

while 1:
    (grabbed,frame)=cam.read()
    frame=imutils.resize(frame,width=700)
    blur= cv2.GaussianBlur(frame,(1,1),0)
    hsv= cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,black_low,black_high)
    mask=cv2.erode(mask,None,iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    counters=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center= None
    if(len(counters)>0):
        c= max(counters,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center= (int(M["m10"]/M["m00"]),int (M["m01"]/M["m00"]))
        if(radius>8):
            cv2.circle(frame,(int (x),int (y)),int (radius),(255,100,30),3)
            cv2.circle(frame,center,5,(0,0,255),-1)
            if(radius>300):
                print("stop")
            else:
                if(center[0]<100):
                    print("left")
                elif(center[0]>200):
                    print("right")
                elif(radius>300):
                    print("front")
                else:
                    print("stop")
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if(key==27):
        break
cam.release()
cv2.destroyAllWindows()































