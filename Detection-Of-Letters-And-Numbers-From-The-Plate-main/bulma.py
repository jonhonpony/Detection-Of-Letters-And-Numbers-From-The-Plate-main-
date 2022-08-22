import cv2
from glob import glob
import os
import pyautogui
import numpy as np



MIN_PIXEL_WIDTH = 5
MIN_PIXEL_HEIGHT = 15

MIN_ASPECT_RATIO = 0.25
MAX_ASPECT_RATIO = 1.0

MIN_PIXEL_AREA = 80
s=0
e=0
imgs=glob("image\*.jpg")
for imga in imgs:
    img=cv2.imread(imga)
    h = img.shape[0]
    w = img.shape[1]
    siyah = []
    j=0
    for x in range(0,h):#siyah noktaları buldum
        for y in range(0,w):
            #renk=img[x,y]
            a=img[x,y,0]
            b=img[x,y,1]
            c=img[x,y,2]
            if a<120 and b<120 and c<120:
                siyah.append((x,y))
                j=j+1
    imgyeni=np.zeros((h, w, 1), np.uint8)
    for i in range(j):#Okuma yaparken beyaz noktalara baktığı için beyazlatma yaptım
        imgyeni[siyah[i][0],siyah[i][1]]=[255]
    kernel = np.ones((4,4),np.uint8)
    cv2.imshow("ad",imgyeni)

    sonuc=cv2.morphologyEx(imgyeni,cv2.MORPH_OPEN,kernel)#Open morfolojik işlemini yaptım


    contours, npaHierarchy = cv2.findContours(sonuc, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)   # find all contours

    for contour in contours:

        boundingRect = cv2.boundingRect(contour)
        [intX, intY, intWidth, intHeight] = boundingRect
        intBoundingRectArea=intWidth*intHeight
        AspectRatio=intWidth/intHeight

        if (intBoundingRectArea > MIN_PIXEL_AREA and
            intWidth > MIN_PIXEL_WIDTH and intHeight > MIN_PIXEL_HEIGHT and
            MIN_ASPECT_RATIO < AspectRatio and AspectRatio < MAX_ASPECT_RATIO):
            print(boundingRect)
            pt1 = (intX, intY)
            pt2 = ((intX + intWidth), (intY + intHeight))
            showimg=img[(intY-2) : (intY+intHeight+4),(intX) : (intX + intWidth)]
            cv2.imshow("nedir",showimg)

            result =pyautogui.prompt(text='Nedir'+str(s), title='Bul')
            if result=="a":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("A/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="b":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("B/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="c":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("C/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="d":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("D/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="e":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("E/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="f":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("F/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="g":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("g/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="ğ":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("ğ/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="h":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("H/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="ı":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("I/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="i":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("İ/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="j":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("J/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="k":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("K/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="l":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("L/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="m":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("M/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="n":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("N/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="o":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("O/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="ö":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("Ö/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="p":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("P/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="r":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("R/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="s":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("S/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="ş":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("Ş/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="t":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("T/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="u":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("U/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="ü":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("Ü/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="v":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("V/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="y":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("Y/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="z":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("z/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="0":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("0/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="1":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("1/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="2":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("2/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="3":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("3/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="4":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("4/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="5":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("5/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="6":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("6/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="7":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("7/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="8":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("8/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="9":
                showimg=cv2.resize(showimg,(24,24))
                cv2.imwrite("9/"+str(s)+".jpg",showimg)
                s=s+1
            if result=="exit":
                e=1
                break

    os.remove(imga)
    if e==1:
        break



