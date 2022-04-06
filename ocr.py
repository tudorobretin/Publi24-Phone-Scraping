import pytesseract
import argparse
import cv2
from PIL import Image
import base64


class OCR:
    def __init__(self):
        self.init = 0

    def image_to_text(self, encoded_image):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        #img_data_str = "iVBORw0KGgoAAAANSUhEUgAAANwAAABkCAYAAADtw16ZAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAL/SURBVHhe7dhRYqowEAVQl+eCXI57YSvuhKctwiQkEGI/St85nwVhEu8ksRcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgD7iO98eYGG6Xcbr47TZMVzYMt/Qz1/uYPXZ9T3DNi3jcx+slqyOx1P24Xyv33ca08sd4v/7A2KIwzmIdLfPwaQ2cRR7IRdJ0RwOxdf+qkdYNP6s2XfqZ5qBPPhpbYqeO1nnQcP+HZVdZVv7lux/G2+YOE++NO0cMYXhGCFUMfKmGuNu17LalhluPIy4uvWNL5btyWsexeShpqYHTCIGIq2fYGTYDEYKTBK16xAqBn99XqaFideycrBtueVe8ttnIUW1sUWEH7Z+HgpYaOJNyKOt/j0Kj7P7WeisFLb7rFnaE8rvnhnm9sxrop9qi0RTitrG9H/UYhnodRS0N1zO//G61ULYEIgR371j0FneXOZiFXSKRvf/1jNJnexruo7HN3bbT+AXFech1zC+/XXfDday+MejPt86/R7KGe9ex3L7x26Wx4ZJrsY7usb3nZ6rtSMPV5iFhd/ubehvuSMBekpBlnwnPSsLV8o7Ne0Jon6P5/odF/NtT59jew5mvt87H1jxErc/jZMIXe6ThliPR/n/68pCtnhdqSK81HGv3ghmfXdIztqXbji0Oe/MQHJpfTqQalCXs6wAdOO7kgS+GrNZYP9BwL1kNw+2zseV9U5YdFZvm4c1x8g8LX24MQQjI6gd7S8i/hIZ5qYYsHvPiir7VGJPmWoIPx3a84VrnYdIzJs5jOb4sIVlCVTjShMStAhskwdxZqUv/tSvVtbIZzvJOMddVqqlxbCsbdRyZhy+9NXAW2QocFL/wJbFNjVCVrPRxl0ttrvI7u0Fs5FSl9paxldTqODwPT701cCbrwNdW15adpx70oHC0SnaDp90VfqfhvuQPLe3ak6ZdtaRSR888dNcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/D6Xyz+KgA8z9a1TTQAAAABJRU5ErkJggg=="
        img_data_bytes = str.encode(encoded_image)

        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.decodebytes(img_data_bytes))

        fill_color = (0, 0, 0)
        im = Image.open("imageToSave.png")
        im = im.convert("RGBA")

        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1], im.size, fill_color)
            background.paste(im, im.split()[-1])
            im = background

        im.convert("RGB").save(r"C:\Users\MAXMEDIA\PycharmProjects\phone scraping publi24\result.jpg")
        img = im.convert("RGB")

        img = r"C:\Users\MAXMEDIA\PycharmProjects\phone scraping publi24\result.jpg"
        phone_number = pytesseract.image_to_string(Image.open(img))
        phone_number = phone_number.rstrip()

        return phone_number
