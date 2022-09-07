def toImg(path, i):
    from convertaa import doConvert
    from PIL import Image, ImageFont, ImageDraw

    file = path

    text, x, y = doConvert(file)

    img = Image.new("L", (x, y))

    SIZE = 25
    FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
    FONT = ImageFont.truetype(FONT_PATH, SIZE)
    draw_text = ImageDraw.Draw(img)

    oneLine = ""
    yPos = 0
    for char in text:
        if char == "\n":
            draw_text.text((0, yPos), oneLine, fill=255)
            oneLine = ""
            yPos += 7
        else:
            oneLine += char

    img.save("AA_resource2/{}.jpg".format(i))