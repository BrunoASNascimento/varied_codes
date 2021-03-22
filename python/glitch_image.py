from glitch_this import ImageGlitcher
from PIL import Image
from numba import njit


PATH = 'data/High_resolution_wallpaper_background_ID_77701907367.jpg'

glitcher = ImageGlitcher()

img = Image.open(PATH)
glitch_img = glitcher.glitch_image(
    img, 8, color_offset=True, gif=False, scan_lines=True, frames=60)

glitch_img.save('data/443580_test.jpg')


# DURATION = 10     # Set this to however many centiseconds each frame should be visible for
# LOOP = 0            # Set this to how many times the gif should loop
# # LOOP = 0 means infinite loop
# glitch_img[0].save('data/glitched_test.gif',
#                    format='GIF',
#                    append_images=glitch_img[1:],
#                    save_all=True,
#                    duration=DURATION,
#                    loop=LOOP)
