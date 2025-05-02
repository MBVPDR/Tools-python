from PIL import Image
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image_path, output_width=100):
    image = Image.open(image_path)
    image = image.convert("L")  # سیاه و سفید
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio)
    image = image.resize((output_width, new_height))
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

print(image_to_ascii("cat.jpg"))