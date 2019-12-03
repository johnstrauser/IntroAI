# load the file, store the first image into the 'image' list
image = []
f = open("facedatatrain")
for x, line in enumerate(f):
    if x >= 0 and x <= 69:
        image.append(line)
f.close()

# print(image)

# check number of '#' in a specific region
#length = len(image[0])
# for i in range(length):
# if image[0][i] == '#':
#print(length)
#print(image[2])
#print(image[2][30])

# count number of '#' for a single image, spliting by each o
# o is the small region
num_of_x = 6
num_of_y = 7
x = 10
y = 10
num_of_o = num_of_x * num_of_y
g = []
index = 0


for k in range(num_of_o - 1): # initial all value in the list to be zero
    g.append(0)

print(len(g))

# range(5): 0-4; range(6,10): 6-9
for i in range(60):
    for j in range(70):
        index = ((j/y) * num_of_x) + (i/x)
        print(index)
        print(j, i)
        if image[j][i] == '#':
            g[index] = g[index] + 1





# we want input[the ith ][]