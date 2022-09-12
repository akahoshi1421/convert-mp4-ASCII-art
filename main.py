from toAAImg import toImg
from splitVideo import split
from tomp4 import mp4Generate
import sys
import glob

if len(sys.argv) != 3:
    raise Exception("\"python main.py 挿入ファイル名 書き出しファイル名\"と入力してください")

print("動画分割中...")
frameRate = split(sys.argv[1])

PATH = "AA_resource/"

jpgNum = len(glob.glob(PATH + "*.jpg"))

print("画像をAAに変換中...")
for i in range(0, jpgNum):
    toImg("{}_{}.jpg".format(PATH, i), "_{}".format(i))

print("動画を生成中...")
mp4Generate(sys.argv[2], frameRate)