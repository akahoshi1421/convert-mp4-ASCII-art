def doConvert(fileName):
    from PIL import Image
    import numpy as np

    #白黒画像に
    theImage = Image.open(fileName)
    theImage_wb = theImage.convert(mode="1")

    try:#もとは840
        theImage_wb = theImage_wb.resize((int(theImage_wb.width / (theImage_wb.width / 420)), int(theImage_wb.height / (theImage_wb.width / 420))))
    except:
        pass

    #theImage_wb.save("result.jpg")

    rgb_img = theImage_wb.convert("RGB")
    size = rgb_img.size

    x_l = []
    rgb_l = []

    for y in range(size[1]):
        for x in range(size[0]):
            r, g, b = rgb_img.getpixel((x,y))
            rgb_16 = '%02x%02x%02x' % (r, g, b)
            rgb_10 = int(rgb_16, 16)

            x_l.append(rgb_10)
        rgb_l.append(x_l)
        x_l = []

    result_text = ""

    wgb_lists=np.array([0,8421504,16777215])

    for y in range(0, size[1]):
        for x in range(0, size[0]):
            pixel = rgb_l[y][x]

            color = (np.abs(wgb_lists - pixel)).argmin()
            if color == 0:
                result_text += " "

            else:
                result_text += "#"
            
        result_text += "\n"

    return (result_text, size[0] * 6, round(size[1] * 7))

