import Pyro4
import os
import datetime
from tkinter import Tk, filedialog
from io import BytesIO
from PIL import Image


# name = input("What is your name? ").strip()
# now = datetime.datetime.now()
# print('date: '+now.strftime('%d-%m-%y') + ' Time:'+now.strftime(' %H: %M: %S'))
# print(Client.get_usid(name))


# print("Enter the number of calculations to be done")
# n = int(input("Enter n: "))
# while (n > 0):
# n = n-1
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("Enter number for desired calculations: \n" + '1.ADD \n' +
#         '2.SUBTRACT \n' + '3.MULTIPLY \n' + '4.DIVISION \n'+'5.EXPONENTIATION \n')
# c = int(input('Enter your choice: '))
# if (c == 1):
#     print(Client.add(a, b))
# elif (c == 2):
#     print(Client.subtract(a, b))
# elif (c == 3):
#     print(Client.multiply(a, b))
# elif (c == 4):
#     print(Client.division(a, b))
# elif (c == 5):
#     print(Client.exp(a))
# else:
#     print('invalid input')

def main(): 
    print("Inside main")
    Client = Pyro4.Proxy("PYRONAME:RMI.calculator")
    print(Client)
    root = Tk()
    root.title("Image Viewer")
    root.filename = filedialog.askopenfilename(title="Select an image", filetypes=(
    ("jpg files", "*.JPG"), ("png files", "*.png"), ("jpeg,→ files", "*.jpeg")))
    image_object = Image.open(root.filename)
    # Get image bytes
    image_file = BytesIO()
    image_object.save(image_file, format="JPEG")
    image_bytes = image_file.getvalue()
    print(image_bytes)
    # print(Client.division(6, 2))
    print(Client.main_ocr(image_bytes))

if __name__ == "__main__":
    main()
