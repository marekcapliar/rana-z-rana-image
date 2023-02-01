# napis program ktory vygeneruje obrazok 100x100 pixelov a na miesta kde sucet suradnic je parny je cierny pixel, tam kde je neparny tak je zlty

from PIL import Image

img = Image.new("RGB", (100, 100), 'yellow')
pixels = img.load()

for i in range(img.size[1]):
    for j in range(img.size[0]):
        if (i + j) % 2 == 0:
            pixels[i, j] = (0, 0, 0)

img.save('img.jpg')
