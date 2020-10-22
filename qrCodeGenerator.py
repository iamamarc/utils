import qrcode

# Link for website
input_data = "https://www.dailymail.co.uk/home/index.html"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=3,
        border=1)

'''
Default Values
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
'''

qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode002.jpeg')
