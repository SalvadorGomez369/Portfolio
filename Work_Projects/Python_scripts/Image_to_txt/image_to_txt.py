#pip install pytesseract,pillow
#install AI for windows from https://github.com/UB-Mannheim/tesseract/wiki: (tesseract-ocr-w64-setup-5.3.0.20221222.exe (64 bit) resp.)

from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

#prints abalibles lenguages 
#print(pytesseract.get_languages(config=''))

print(pytesseract.image_to_string(Image.open('Inventory-Report.png'), lang='eng'))

