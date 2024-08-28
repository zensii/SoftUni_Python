import pyqrcode            # pip install pyqrcode
                           # pip install pypng


address = "https://pypi.org/project/phonenumbers/"
url = pyqrcode.create(address)
url.png("PyLib.png", scale=8)


# генерира QR код по url