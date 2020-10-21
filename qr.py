import qrcode
from PIL import Image
import os


def mkqr_link(user_link, img_name):
    input_data = str(user_link)

    qr = qrcode.QRCode(version=2, box_size=15, border=1)

    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(str(img_name) + ".png")
    return img


def resize(img, new_width=150):
    width, height = img.size
    aspect_ratio = float(width)/float(height)
    new_height = int(new_width/aspect_ratio)
    new_dim = (new_width, new_height)
    new_img = img.resize(new_dim)
    return new_img


def greyscale(img):
    return img.convert('L')


def replace_pixels_with_ascii(img, buckets=25):
    start_pixels = list(img.getdata())
    new_pixels = [ASCII_CHARS[pixels_value//buckets]
                  for pixels_value in start_pixels]
    return ''.join(new_pixels)


def make_final_img(img, new_width=150):
    img = resize(img)
    img = greyscale(img)

    pixels = replace_pixels_with_ascii(img)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+new_width]
                 for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)


ASCII_CHARS = ['.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']
ASCII_CHARS = ASCII_CHARS[::-1]

os.system("cls||clear")

usr_qr_link = input("What link?\n:")
img_name = input("\nWhat to call image?\n:")

qr_img = mkqr_link(usr_qr_link, img_name)
ascii_img = make_final_img(qr_img)
print(ascii_img)
