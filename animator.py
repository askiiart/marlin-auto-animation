from subprocess import getoutput
import os
import random

output = '/home/ben/Documents/bad_apple_Bootscreen.h'
video = '/home/ben/Videos/bad_apple_5fps.mp4'

# Make video into xbm files
os.mkdir('temp')
os.mkdir('temp/pngs')
os.mkdir('temp/xbms')

# Convert video to pngs
getoutput(f'ffmpeg -i {video} temp/pngs/%d.png')

# Convert pngs to xbms
pngs = os.listdir('temp/pngs')
filenames = [os.path.splitext(os.path.basename(filename))[0] for filename in pngs]

for filename in filenames:
    getoutput(f'convert temp/pngs/{filename}.png temp/xbms/{filename}.xbm')

# make some pngs for debugging
debug = True
if debug:
    os.mkdir('temp/debug_pngs')
    for filename in filenames:
        if random.random() < 0.01:
            getoutput(f'convert temp/xbms/{filename}.xbm temp/debug_pngs/{filename}.png')

'''
for filename in filenames:
    f = open(f'temp/xbms/{filename}.xbm', 'r')
    lines = [line.strip() for line in f.readlines()[3:]]
    os.touch(f'{output}')
    f.close()
    exit()
'''
#os.rmdir('temp')