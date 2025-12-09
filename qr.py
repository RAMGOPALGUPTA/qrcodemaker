import qrcode

url = input("Enter the URL:").strip()
file_path = "D:\\sample projects\\qrcode.png"

Qr = qrcode.QRCode()
Qr.add_data(url)

img = Qr.make_image()

img.save(file_path)
