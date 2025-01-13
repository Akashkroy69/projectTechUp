# we need to import or connect the module the qrcode module developers have created
import qrcode
qrVar = qrcode.QRCode()
data = input("Enter data to create the QR code: ")
qrVar.add_data(data)
qrVar.make()
img =  qrVar.make_image()
img.save("c.png")