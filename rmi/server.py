import Pyro4
import random
import io
import datetime
import subprocess
import base64


import cv2
import easyocr
from IPython.display import Image as IMager

now = datetime.datetime.now()
print('date: '+now.strftime('%d-%m-%y')+' Time: '+now.strftime('%H:%M:%S'))
reader = easyocr.Reader(['en'])

@Pyro4.expose
class Server(object):
    def main_ocr(self, byte_array): 
        # print(byte_array)
        byte_array = byte_array['data']
        byte_array = base64.b64decode(bytes(byte_array, 'utf-8'))
        # print("\n\n****************************************************************************\n\n")
        # print(byte_array)
        # print(type(byte_array))
        # img = IMager(byte_array)
        # print("\n\nHelooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n\n")
        text = reader.readtext(byte_array)
        ans = ""
        for i in text:
            ans+= i[1]+" "
        # print("Hello")
        # return "Hello"
        # print("\n\n****************************************************************************\n\n")
        print(ans)
        # print("\n\n****************************************************************************\n\n")
        return ans


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
url = daemon.register(Server)
ns.register("RMI.calculator", url)
print("The Server is now active., please request your calculations or start file transfer")
daemon.requestLoop()
