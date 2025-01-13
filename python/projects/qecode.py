import qrcode

qr = qrcode.QRCode()
data = input("please add data: ")
qr.add_data(data)
qr.make()
img = qr.make_image()
img.save("b.png")