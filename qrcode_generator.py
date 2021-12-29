import qrcode

img = qrcode.make("https://raikwal-homepage.vercel.app/")

img.save("myQr.jpg")
