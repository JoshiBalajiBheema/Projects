import pyqrcode
import png
username = input("Enter INSTAGRAM username: ") # Enter Instagram username
link = f"https://www.instagram.com/{username}/" # link is generated
qr_code = pyqrcode.create(link) # QRcode is generated 
qr_code.png(f"{username}.png", scale=10) # generated QRcode is saved
