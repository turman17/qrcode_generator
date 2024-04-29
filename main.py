import qrcode
from PIL import ImageColor

def qr_code_create(data, fill_color, back_color):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    try:
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
    except Exception as e:
        print("Error: Colors", e)
        img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR code created successfully!")



if __name__ == '__main__':
    print("Lets create a QR code!\n"
          "please provide the data you want to encode in the QR code\n"
            "Example: https://google.com")
    data = input("Enter the data: ")
    print("Please provide the fill color for the QR code\n"
            "Example: yellow")
    fill_color = input("Enter the fill color: ")
    print("Please provide the back color for the QR code\n"
            "Example: blue")
    back_color = input("Enter the back color: ")
    qr_code_create(data, fill_color, back_color)
