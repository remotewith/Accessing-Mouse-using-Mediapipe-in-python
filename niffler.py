from turtle import left
import mediapipe as mp
import cv2
import thesius_module as the
import time
import autopy
import numpy as np

wCam,hCam=640,480
frameR=100
smooth=2
plocx,plocy=0,0
clocx,clocx=0,0

cap=cv2.VideoCapture(0)

detector=the.handDetector(maxHands=1)
wScr,hScr=autopy.screen.size()

cap.set(3,wCam)
cap.set(4,hCam)

while True:
    _,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img)

    if len(lmList)!=0:
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(255,0,0))
        x1,y1=lmList[8][1],lmList[8][2]
        x2,y2=lmList[12][1],lmList[12][2]

        '''if(y1 < lmList[7][2]) and (y2 < lmList[11][2]) and (lmList[16][2]<lmList[15][2]):
            autopy.mouse.move((2*wCam)+50,5)
            autopy.mouse.click()'''


        if(y1 < lmList[7][2]) and (y2 < lmList[11][2] and abs(x1-x2) <= 30):
            time.sleep(0.05)
            autopy.mouse.click()


        elif (y1< lmList[6][2] and y2>lmList[11][2]):
            cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(255,0,0))
            x3=np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3=np.interp(y1,(frameR,hCam-frameR),(0,hScr))
            clocx=plocx+(x3-plocx)/smooth
            clocy=plocy+(y3-plocy)/smooth

            autopy.mouse.move(clocx,clocy)#Wscr-clocx
            cv2.circle(img,(x1,y1),15,(0,0,0),cv2.FILLED)

            plocx,plocy=clocx,clocy


    cv2.imshow("Image",img)
    key=cv2.waitKey(1)
    if key==ord('e'):
        break

cap.release()
cv2.destroyAllWindows()