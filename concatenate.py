import glob
from PIL import Image

image_files = glob.glob('imgs/*')
width, height = Image.open(image_files[0]).size

gap = 20
cols = 4
total_width = cols * (width + gap) + gap
total_height = ((len(image_files) - 1) // cols + 1) * (height + gap) + gap

result_image = Image.new('RGB', (total_width, total_height), color='white')
x = y = 0
for index, image_file in enumerate(image_files):
    img = Image.open(image_file).convert('RGBA').resize((width, height))
    result_image.paste(img, (x + gap, y + gap), mask=img.split()[-1])
    x += width + gap
    if (index + 1) % cols == 0:
        x = 0
        y += height + gap

result_image.save('concatenate.png')
