import Pyro4
import random
import os
import datetime
import subprocess


import cv2
import easyocr
from IPython.display import Image as IMager

now = datetime.datetime.now()
print('date: '+now.strftime('%d-%m-%y')+' Time: '+now.strftime('%H:%M:%S'))


@Pyro4.expose
class Server(object):
    def main_ocr(self, byte_array): 
        reader = easyocr.Reader(['en'])
        img = IMager(byte_array)
        text = reader.readtext(img)
        image = cv2.imread(img)
        ans = ""
        for i in text:
            topleft = tuple(i[0][0])
            botright = tuple(i[0][2])
            print(topleft)
            print(botright)
            cv2.rectangle(image, (int(topleft[0]),int(topleft[1])), (int(botright[0]),int(botright[1])),(0,0,255),2)
            ans+= i[1]+" "
        # print("Hello")
        # return "Hello"
        return ans


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
url = daemon.register(Server)
ns.register("RMI.calculator", url)
print("The Server is now active., please request your calculations or start file transfer")
daemon.requestLoop()
