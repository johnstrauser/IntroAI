import numpy as np
import random

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


def naive_bayes():

    return


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