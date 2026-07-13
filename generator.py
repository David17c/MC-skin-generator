from PIL import Image
import random

def getRandomColor():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

image = Image.new("RGB", (64, 64), "white")
pixels = image.load()

width, height = image.size

for y in range(height):
    for x in range(width):
        color = getRandomColor()
        pixels[x, y] = color

image.save("random_skin.png")