def mp4Generate(targetPath, frameRate):
    import cv2
    from PIL import Image
    import glob

    PATH = "AA_resource2/"

    top_img = Image.open(PATH + "_0.jpg")
    size = top_img.size
    jpgNum = len(glob.glob(PATH + "*.jpg"))

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')#保存形式
    video = cv2.VideoWriter(targetPath ,fourcc, float(frameRate), (size[0] // 2, size[1] // 2))

    for i in range(0, jpgNum):
        img = cv2.imread("{}_{}.jpg".format(PATH, i))

        img = cv2.resize(img, (size[0] // 2, size[1] // 2))
        if img is None:
            print("NONE")

        video.write(img)

    video.release()
