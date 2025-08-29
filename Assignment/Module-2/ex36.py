import qrcode

url = "https://github.com/Vadodariyavivek03/09July_Vivek_Python"

qr = qrcode.make(url)

qr.save("github.png")

