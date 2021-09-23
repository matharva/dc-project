from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os
import string
import random
from datetime import datetime
import cv2
import easyocr
from IPython.display import Image as IMager
import base64

server = SimpleXMLRPCServer(('localhost', 3000), allow_none=True)

now = datetime.datetime.now()
print('date: '+now.strftime('%d-%m-%y')+' Time: '+now.strftime('%H:%M:%S'))
reader = easyocr.Reader(['en'])

def main_ocr(byte_array): 
    byte_array = byte_array['data']
    byte_array = base64.b64decode(bytes(byte_array, 'utf-8'))
    text = reader.readtext(byte_array)
    ans = ""
    for i in text:
        ans+= i[1]+" "
    print(ans)
    return ans

server.register_function(main_ocr)

if __name__ == '__main__':
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
