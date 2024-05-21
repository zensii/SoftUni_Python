import pyqrcode

address = "https://pypi.org/project/phonenumbers/"
url = pyqrcode.create(address)
url.png("PyLib.png", scale=8)
