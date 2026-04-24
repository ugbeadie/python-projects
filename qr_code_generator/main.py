import qrcode

data = input("Enter the URL or text: ").strip()
filename = input("Enter filename (e.g. qrcode.png): ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

try:
    image.save(filename)
    print(f"Saved as '{filename}'")
except Exception as e:
    print(f"Error: {e}")