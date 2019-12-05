#import numpy as np
import random
from training import training_labels,training_data
from test import test_labels,test_data
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
def perceptron_f(labels, regions, type, percent, test_labels, test_data_regions):
    #init important values
    num_images = len(labels)
    num_regions = len(regions[0])
    #print("num_images="+str(num_images))
    
    bias = random.choice([-1,0,1])
    #create array of w values
    w = []
    #print("w before training")
    for i in range(num_regions):
        w.append(random.choice([-1,0,1]))
        #print("w["+str(i)+"] = "+str(w[i]))
    #print("bias = "+str(bias))
    
    #for each image n
        #calculate f = sum(w[i]*regions[n][i])
        #if f doesn't match labels[n], perform w adjustment
    steps = [x*0.1 for x in range(1,int((percent*10)+1))]
    #print(steps)
    #num_penalties = 0
    for step in steps:
        num_images_step = int(step * num_images)
        #print(str(step)+" of "+str(num_images)+" is "+str(num_images_step))
        for n in range(num_images_step):
            f = 0
            for i in range(num_regions):
                f += (w[i]*regions[n][i])
            f += bias
            if f >= 0 and labels[n] != 1:
                #for each region
                    #w[i] -= regions[n][i]
                for i in range(num_regions):
                    w[i] -= regions[n][i]
                    bias -= 1
                #num_penalties+=1
            elif f < 0 and labels[n] == 1:
                #for each region
                    #w[i] += regions[n][i]
                for i in range(num_regions):
                    w[i] += regions[n][i]
                    bias += 1
                #num_penalties+=1
    #print("num penalties = "+str(num_penalties))
    '''    
    print("w after training")
    for i in range(num_regions):
        print("w["+str(i)+"] = "+str(w[i]))
    print("bias = "+str(bias))
    '''
    #data to test against
    #test_labels ad test_data_regions
    
    #Perform tests for get f value for each image
    correct = 0
    num_test_images = len(test_labels)
    for n in range(num_test_images):
        f = 0
        for i in range(num_regions):
            f += (w[i]*test_data_regions[n][i])
        f += bias
        if f >= 0 and test_labels[n]==1:
            correct += 1
        elif f < 0 and test_labels[n] == 0:
            correct += 1
    
    #Output results somehow
    percent_correct = float(correct)/float(num_test_images)
    print(" correct "+str(percent_correct*100)+"% of the time")
    return percent_correct

def perceptron_d(labels, regions, type, percent, test_labels, test_data_regions):
    #init important values
    num_images = len(labels)
    num_regions = len(regions[0])
    #init bias
    bias = [random.choice([-1,0,1]) for i in range(10)]
    #init w
    w = [[random.choice([-1,0,1]) for i in range(num_regions)] for j in range(10)]
    #list to train over growing amount of training data
    steps = [x*0.1 for x in range(1,int((percent*10)+1))]
    for step in steps:
        num_images_step = int(step * num_images)
        #print("num images step= "+str(num_images_step))
        penalties = 0
        for n in range(num_images_step):
            f = [0 for i in range(10)]
            for i in range(len(f)):
                for j in range(num_regions):
                    f[i] += (w[i][j]*regions[n][j])
                    #print("")
                f[i] += bias[i]
                
                #input("cont")
                #print("f["+str(i)+"] = "+str(f[i]))
            max_index = get_max_index(f)
            #print("max x = f["+str(max_index)+"] = "+str(f[max_index]))
            #print("label = "+str(labels[n]))
            if max_index != labels[n]:
                penalties += 1
                #decrease w of max_index and increase w of labels[n]
                for i in range(num_regions):
                    w[max_index][i] -= regions[n][i]
                    w[labels[n]][i] += regions[n][i]
                #decrease bias of max_index
                bias[max_index] -= 1
                #increase bias of labels[n]
                bias[labels[n]] += 1
        #print("penalties = "+str(penalties))
    #data to test against
    #test_labels ad test_data_regions
    #Perform tests for get f value for each image
    correct = 0
    num_test_images = len(test_labels)
    print(num_test_images)
    #print("num test images = "+str(num_test_images))
    for n in range(num_test_images):
        f = [0 for i in range(10)]
        for i in range(len(f)):
            for j in range(num_regions):
                f[i] += (w[i][j]*test_data_regions[n][j])
                
            f[i] += bias[i]
        max_index = get_max_index(f)
        if max_index == test_labels[n]:
            correct += 1
            
    percent_correct = float(correct)/float(num_test_images)
    print(" correct "+str(percent_correct*100)+"% of the time")
    return percent_correct

def naive_bayes():

    return

def get_max_index(list):
    out = 0
    for i in range(1,len(list)):
        if list[i] > list[out]:
            out = i
    return out
#type = input("Enter the type of data to run ('f' for faces or 'd' for digits): ")
#percent = input("Enter the percentage of images to train against (0.5 for 50%): ")
#algorithm = input("Enter the algorithm to use ('p' for perceptron, 'n' for naive bayes, 'o' other algortihm TBD): ")

type = 'd'
percent = 1.0
algorithm = 'p'

num_x_regions = 10
num_y_regions = 10

labels = training_labels(type,1.0)
data_regions = training_data(type,1.0, num_x_regions, num_y_regions)

test_labels = test_labels(type,1.0)
test_data_regions = test_data(type,1.0, num_x_regions, num_y_regions)

sum = 0
runs = 10
for i in range(runs):
    sum += perceptron_d(labels, data_regions, type, percent, test_labels, test_data_regions)
print("average correctness = "+str((sum/runs)*100))
'''
#use if statements to call functions for algorithms
if algorithm == 'p':
    perceptron(labels, data_regions, type, percent, test_labels, test_data_regions)
    '''
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