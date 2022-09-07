def split(path):
    import os
    import shutil
    import cv2

    shutil.rmtree("AA_resource")
    os.makedirs("AA_resource")

    shutil.rmtree("AA_resource2")
    os.makedirs("AA_resource2")

    cap = cv2.VideoCapture(path)
    frameRate = int(cap.get(cv2.CAP_PROP_FPS))

    cnt = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("AA_resource/_{}.jpg".format(cnt), frame)
            cnt += 1
        else:
            return frameRate

