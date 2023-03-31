import png

width = 40
height = 40
img = []
for y in range(height):
    # row = ()
    row = ()
    for x in range(width):
        # row = row + (x, max(0, 255 - x - y), y)
        if y == height // 2 and row == width // 2:
            row = row + (0, 0, 0)
        else:
            row = row + (255, 255, 255)
        # row.append((255, 255, 255))
    img.append(row)
# img[250][250] = (0, 0, 0)
with open('nothing.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)