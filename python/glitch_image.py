from glitch_this import ImageGlitcher
from PIL import Image


PATH = 'C:/Users/bruno/OneDrive/Imagens/Wallpapers/1933524.jpg'

glitcher = ImageGlitcher()

img = Image.open(PATH)
glitch_img = glitcher.glitch_image(
    img, 8, color_offset=True, gif=True, scan_lines=False, frames=60)

# glitch_img.save('data/test.jpg')


DURATION = 10     # Set this to however many centiseconds each frame should be visible for
LOOP = 0            # Set this to how many times the gif should loop
# LOOP = 0 means infinite loop
glitch_img[0].save('data/glitched_test.gif',
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=DURATION,
                   loop=LOOP)
