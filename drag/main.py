import cv2
from cvzone.HandTrackingModule import HandDetector
 import cvzone
import os
 cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 720)
detector = HandDetector (detectionCon=0.65)
 class DragImg():
     def _init__ (self, path, posOrigin, imgType):
        self.pos0rigin = pos0rigin
        self.imgType = ingType
        self.path = path
         if self.imgType == "png":
            self.img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
         elif self.imgType == 'jpg':
            self.img = cv2.imread(self.path)
         else:
             pass # go for 3d
         self.size = self.img.shape[:2]
     def update (self, cursor):
        ох, oy = self.posOrigin
        h, W = self.size
     if OX < cursor[] < OX + W and oy < cursor[1] < oy + h:
         self.posOrigin = cursor[e] - w // 2, cursor[1] ] - h / / 2
path = 'Images' # folder from where image is extracted
myList = os.listdir(path)
print(myList)
listImg = []]
for X, pathImg in enumerate(myList):
 if *png in pathImg:
    imgType = 'png
 else:
     imgType = 'jpg
     listImg append(DragImg(f' (path)/ [58+x*308, 50], imgType))
                                         
while True:
 success, img g = cap.read()
 img g = cv2.flip(img, 1)
 hands, img g = detector. findHands (img, flipType=False)
 if hands:
    lmList = hands [@][*1mList']
    cursor = LnList[8]
     length, info, lmList[12], img)
     if length L 30:
         cursor lmList[8]
         for imgObject in listImg:
            imgObject.update (cursor)
                       
  try:
     for imgObject in listImg:
         h, W, = imgObject. size
         ох, oy = img0bject. .posOrigin
         if imgObject. imgType == 'png':
              img = cvzone. overlayPNG(img, imgObject.img, [ох, oy])
         else:
              img[oy:oy + h, ox:ox + w] = imgObject. img
except:
     pass
cv2. imshow("Image", img)
cv2.waitKey(1)
  
