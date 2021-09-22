import cv2
import easyocr
img_path = "./0_whatsappweb1_censored.jpg"
from IPython.display import Image as IMager
reader = easyocr.Reader(['en'])


img = IMager(img_path)
text = reader.readtext(img_path)
image = cv2.imread(img_path)
ans = ""
for i in text:
    ans+= i[1]+" "
print(ans)