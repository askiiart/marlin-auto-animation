import os

output = './_Bootscreen.h'
video = '/home/ben/Videos/bad_apple_5fps.mp4'

# Make video into xbm files
os.mkdir('temp')
os.mkdir('temp/pngs')
os.mkdir('temp/xbms')

# Convert video to pngs
os.system(f'ffmpeg -i {video} temp/pngs/%05d.png')

# Remove duplicates and rename files
files = sorted(os.listdir('temp/pngs'))
for item in files:
    i = files.index(item)
    if (i + 1) % 6 != 1:
        os.remove(f'temp/pngs/{item}')
files = sorted(os.listdir('temp/pngs'))
for item in files:
    os.rename(f'temp/pngs/{item}', f'temp/pngs/{files.index(item)+1}.png')

# Convert pngs to xbms
pngs = os.listdir('temp/pngs')
filenames = [os.path.splitext(os.path.basename(filename))[0] for filename in pngs]
for filename in filenames:
    os.system(f'convert temp/pngs/{filename}.png temp/xbms/{filename}.xbm')

# Make some pngs for debugging
debug = True
if debug:
    from random import random
    os.mkdir('temp/debug_pngs')
    for filename in filenames:
        if random() < 0.01:  # Takes a long time, so only convert 1% of the images
            os.system(f'convert temp/xbms/{filename}.xbm temp/debug_pngs/{filename}.png')


for filename in filenames:
    f = open(f'temp/xbms/{filename}.xbm', 'r')
    lines = f.readlines()
    for line in lines:
        line = '  ' + line.strip().replace(', }; ', ' };')
    if filename == '1':
        lines.insert(0, 'const unsigned char custom_start_bmp[] PROGMEM = {')
    else:
        lines.insert(0, f'const unsigned char custom_start_bmp{int(filename) - 2}[] PROGMEM = {{')
    f.close()
    f = open(output, 'a')
    f.write('\n')
    f.write('\n'.join(lines))
    f.write('\n')
    f.close()

start_of_ending = ['#ifdef CUSTOM_BOOTSCREEN_ANIMATED_FRAME_TIME', '', '  // Each frame has its own custom duration', '  const boot_frame_t custom_bootscreen_animation[] PROGMEM = {', '    { custom_start_bmp1, 2000 },  // 2.0s', '  { custom_start_bmp1,  100 },  // 0.1s x 5 frames', '  { custom_start_bmp2, 100 },', '  { custom_start_bmp3, 100 },', '  { custom_start_bmp4, 100 },', '  { custom_start_bmp5, 100 },', '  { custom_start_bmp6, 100 },', '  { custom_start_bmp, 500 },   // 0.5s', '  };', '', '#else', '', '  // Each frame shows for CUSTOM_BOOTSCREEN_FRAME_TIME', '  const unsigned char * const custom_bootscreen_animation[] PROGMEM = {']
middle_of_ending = '    custom_start_bmp, '
for i in range(len(filenames))[:-2]:
    middle_of_ending += f'custom_start_bmp{i}, '
end_of_ending = [' };', '', '#endif', '']

f = open(output, 'a')
f.write('\n')
for line in start_of_ending:
    f.write(line + '\n')
f.write(middle_of_ending)
for line in end_of_ending:
    f.write(line + '\n')
f.close()

#os.system('rm -r temp/')
