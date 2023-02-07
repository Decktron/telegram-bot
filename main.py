from PIL import Image
from pytesseract import image_to_string
from pytesseract import pytesseract
pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
from telegrambot import mesajat


def resimi_metine_cevir():
    resim=Image.open("image.png")
    resim = resim.convert("L")
    return image_to_string(resim)


if __name__ == '__main__':
    while(True):
        mesajat(resimi_metine_cevir())

