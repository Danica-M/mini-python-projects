import pyqrcode
import png
from pyqrcode import QRCode

def generateCode(link):
    
    url = pyqrcode.create(link)
    #saves the qr code image  with the file name inclosed in ""
    url.png("qr.png", scale=8)



link = input("Enter url: ")
generateCode(link)
    
