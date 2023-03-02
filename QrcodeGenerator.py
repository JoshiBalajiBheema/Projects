import pyqrcode

website_name = input("Enter Website name : ")  # Follow the prompt
link = input("Enter the LINK :")  # Copy and paste the link
qr_code = pyqrcode.create(link)  # Qrcode is generated
print()  # prints empty space

qr_code.png(f"{website_name}.png", scale=10)  # saves the generated qrcode with the website name

print("QR code generated successfully.")  # simply prints the text
