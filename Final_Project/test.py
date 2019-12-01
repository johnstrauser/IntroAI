# load the file, store the first image into the 'image' list
image = []
f = open("facedatatrain.txt")
for x, line in enumerate(f):
    if x >= 2 and x <= 68:
        image.append(line)
f.close()

# check number of '#' in a specific region
length = len(image[0])
for i in range(length):
    if image[0][i] == '#':
        print("yes")
