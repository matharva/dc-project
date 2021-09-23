from xmlrpc.client import ServerProxy
#from prettytable import PrettyTable
from tkinter import Tk, filedialog
from io import BytesIO
from PIL import Image
proxy = ServerProxy('http://localhost:3000')

if __name__ == '__main__':
    root = Tk()
    root.title("Image Viewer")
    root.filename = filedialog.askopenfilename(title="Select an image", filetypes=(
    ("jpg files", "*.JPG"), ("png files", "*.png"), ("jpeg,→ files", "*.jpeg")))
    image_object = Image.open(root.filename)
    # Get image bytes
    image_file = BytesIO()
    image_object.save(image_file, format="JPEG")
    image_bytes = image_file.getvalue()
    print(proxy.main_ocr(image_bytes))

