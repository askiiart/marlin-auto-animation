# askiiart/marlin-auto-animation

1. Make your video into images. Make it the right resolution and framerate using Handbrake (or ffmpeg), don't use RF=0. Then, make it into images using ffmpeg (`mkdir images; ffmpeg -i video.mp4 images/%05d.png`).
2. Adjust the variables near the start of `animator.py`
3. Run `python3 animator.py`
