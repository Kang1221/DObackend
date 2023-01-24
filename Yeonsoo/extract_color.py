import extcolors
from PIL import Image

colors, pixel_count = extcolors.extract_from_path("carrot.jpg")
print(colors)

pixel_output = 0
for c in colors:
    pixel_output += c[1]
    print(f'{c[0]} : {round((c[1] / pixel_count) * 100, 2)}% ({c[1]})')
print(f'Pixels in output: {pixel_output} of {pixel_count}')