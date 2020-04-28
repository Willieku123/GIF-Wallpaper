import os
from PIL import Image
import ctypes
import time

global nframes
nframes = 0

def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    while frame:
        global nframes
        frame.convert('RGB').save( '%s\\%s.jpg' % (outFolder, nframes ) , quality=100 )
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True



print("Do not kil this console")
os.system("del tmp_files\*.jpg")
extractFrames('tenor.gif', 'tmp_files')


while True:
    for i in range(nframes):
        ctypes.windll.user32.SystemParametersInfoA(20, 0, "tmp_files\\"+str(i)+".jpg" , 3)
        time.sleep(1/30) # FPS
