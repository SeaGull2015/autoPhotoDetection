from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"D:\Software\tesseractOCR\tesseract"
todo = os.listdir(os.path.abspath("")+"\input")
resPath = os.path.abspath("")+"\output\\"

for file in todo:
    path = os.path.abspath("")+"\input\\"+file
    try:
        pdf = pytesseract.image_to_pdf_or_hocr(path, extension='pdf', lang='rus')
        with open(resPath + file + '.pdf', 'w+b') as f:
            f.write(pdf)  # pdf type is bytes by default
    except:
        print("error")
        exit(1)

