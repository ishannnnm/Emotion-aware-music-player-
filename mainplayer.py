import cv2
import os
import random
import vlc
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np
import pandas as pd
import song
er=load_model('_mini_XCEPTION.106-0.65.hdf5')
fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
em=['angry','disgust','scared','happy','sad','surprised','neutral']
v=cv2.VideoCapture(0)


while True:
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j)
    cv2.imshow('img',i)
    k=cv2.waitKey(1)

    if(k==ord('c')):
        
        if(len(f)>=1):
            for (x,y,w,h) in f:
                
                g=j[y:y+h,x:x+h]
                g=cv2.resize(g,(48,48))
                
                g=g.astype('float')/255
                g=img_to_array(g)
                g=np.expand_dims(g,axis=0)
                p=er.predict(g)[0]
                print(p)
                ind=np.argmax(p)
                mood=em[ind]
                print(mood)
                song.playsong(mood)
    
    if(k==ord('q')):
        
        cv2.destroyAllWindows()
        v.release()
        break   
    
