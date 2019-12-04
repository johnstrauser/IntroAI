#import numpy as np
import random
from training import training_labels,training_data
'''
def perceptron(a, f, identifier, g, w):
    if identifier == 0:
        # only 1 f(x) needed. Face is 60*74, digit is 28*28
        # let's say, for face image, we divide the whole image into 6*7 small matrix with
        # 10*10 each, while the last one of each column has 6*14 (because of the remainder)
        # and extract one of them each time

        # the range for the for loop depends on numbers of image we want to divide into
        for...
            k = random.uniform(-1, 1)
            w.append(k)

        # extract the wanted region in a, need to be implemented
        for ...

            region = ...

            # number of #(refer to the file facedatatrain.txt) in the region we just extracted at line 20
            num_non_empty = ...
            g.append(num_non_empty)

        # note the length of g should be the same as the length of w (without bias)
        # now we just multiply, i.e. w[0]*g[0] + w[1]*g[1] ... to get the f value
        for ...
            f += w[i]*g[j]
    return
'''
def perceptron(labels, regions, type):
    #init important values
    num_images = len(labels)
    num_regions = len(regions[0])
    print("num_images="+str(num_images))
    
    bias = random.choice([-1,0,1])
    #create array of w values
    w = []
    print("w before training")
    for i in range(num_regions):
        w.append(random.choice([-1,0,1]))
        print("w["+str(i)+"] = "+str(w[i]))
    print("bias = "+str(bias))
    
    #for each image n
        #calculate f = sum(w[i]*regions[n][i])
        #if f doesn't match labels[n], perform w adjustment
    steps = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    for step in steps:
        num_images_step = int(step * num_images)
        print(str(step)+" of "+str(num_images)+" is "+str(num_images_step))
        for n in range(num_images_step):
            f = 0
            for i in range(num_regions):
                f += (w[i]*regions[n][i])
            f += bias
            if f > labels[n]:
                #for each region
                    #w[i] -= regions[n][i]
                for i in range(num_regions):
                    w[i] -= regions[n][i]
                    bias -= 1
            elif f < labels[n]:
                #for each region
                    #w[i] += regions[n][i]
                for i in range(num_regions):
                    w[i] += regions[n][i]
                    bias += 1
    
        
    print("w after training")
    for i in range(num_regions):
        print("w["+str(i)+"] = "+str(w[i]))
    print("bias = "+str(bias))
    return

def naive_bayes():

    return


type = input("Enter the type of data to run ('f' for faces or 'i' for images): ")
percent = 1.0
algorithm = input("Enter the algorithm to use ('p' for perceptron, 'n' for naive bayes, 'o' other algortihm TBD): ")

labels = training_labels(type,percent)
data_regions = training_data(type,percent)

print("Labels:")
for label in labels:
    print(str(label), end=" ")
print("")

print("Data Regions:")
for j in range(len(data_regions[0])):
    for i in range(len(data_regions)):
        print(data_regions[i][j], end=" ")
    print("")
    
#use if statements to call functions for algorithms
if algorithm == 'p':
    perceptron(labels, data_regions, type)
'''
elif algorithm == 'n':
    #naive_bayes()
else:
    #other algorithm
    print("other")
'''
'''
# main starts here
# g is a list holds number of # in the given region
g = []

# w is the weight for corresponding g value, initially it is a random number between -1 and 1
# note: i am not sure about the bias value therefore have not added it here
w = []

# f(x), < 0 means not face >= 0 means is face
f = 0

# load the data, have not got it right though
# ideally, a should be a 2d matrix contains a single image. b should be a 1d array
# to store the label(face or not face) corresponding to each image
for ...

    a = np.loadtxt('facedatatrain.txt')
    b = np.loadtxt('facedatatestlabels.txt')

    # identifier to know we are predicting face or digit. 0 represents face and 1 represents digit
    identifier = 0
    perceptron(a, f, identifier, g, w)

    # if we predict it right, move on. Otherwise we do the penalty
    # again, bias is not included
    if f >= 0 and b == 0:
        for...
            w[i] = w[i] - g[i]

    elif f < 0 and b == 1:
        for...
            w[i] = w[i] + g[i]
'''