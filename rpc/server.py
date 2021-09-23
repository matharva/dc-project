from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os
import string
import random
from datetime import datetime
import cv2
import easyocr
import base64

server = SimpleXMLRPCServer(('localhost', 3000), allow_none=True)
print("Inside server")
reader = easyocr.Reader(['en'])

def main_ocr(byte_array): 
    # print(type(byte_array),byte_array)
    text = reader.readtext(byte_array.data)
    ans = ""
    for i in text:
        ans+= i[1]+" "
    print(ans)
    return ans

server.register_function(main_ocr)

# if __name__ == '__main__':
#     try:
#         print('Serving...')
#         server.serve_forever()
#     except KeyboardInterrupt:
#         print('Exiting')

try:
    print('Serving...')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
