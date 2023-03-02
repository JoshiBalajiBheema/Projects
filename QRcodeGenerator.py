import pyqrcode
import png
username = input("Enter INSTAGRAM username: ")
link = f"https://www.instagram.com/{username}/"
qr_code = pyqrcode.create(link)
print()
# name=input("Enter File name :")
qr_code.png(f"{username}.png", scale=10)
