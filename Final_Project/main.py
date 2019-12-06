#import numpy as np
import random
from training import training_labels,training_data
from test import test_labels,test_data

class Table():
    def __init__(self, num_regions=None, region_size=None):
        self.pos_table = [[0 for j in range(region_size)] for i in range(num_regions)]
        self.neg_table = [[0 for j in range(region_size)] for i in range(num_regions)]
        self.pos_count = 0
        self.neg_count = 0
        self.pos_value = 0.0
        self.neg_value = 0.0

def perceptron_f(labels, regions, percent, test_labels, test_data_regions):
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

def perceptron_d(labels, regions, percent, test_labels, test_data_regions):
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

def naive_bayes_f(training_labels, training_regions, percent, test_labels, test_data_regions):
    #init needed value
    num_training_images = int(len(training_labels) * percent)
    num_regions = len(training_regions[0])
    
    #init table class
    #since type is f, image is 60x70
    region_max = int((60*70) / num_regions)
    face_tables = Table(num_regions, region_max)
    
    face_tables.pos_count = count_value(training_labels, 1)
    face_tables.pos_value = float(face_tables.pos_count / num_training_images)
    face_tables.neg_count = count_value(training_labels, 0)
    face_tables.neg_value = float(face_tables.neg_count / num_training_images)
    
    #fill face tables
    for i in range(num_regions):
        for j in range(num_training_images):
            count = training_regions[j][i]
            if training_labels[j] == 1:
                face_tables.pos_table[i][count] += 1
            else:
                face_tables.neg_table[i][count] += 1
    
    for i in range(len(face_tables.pos_table)):
        for j in range(len(face_tables.pos_table[0])):
            if face_tables.pos_table[i][j] == 0:
                face_tables.pos_table[i][j] = 0.0001
            else:
                face_tables.pos_table[i][j] /= face_tables.pos_count
            
            if face_tables.neg_table[i][j] == 0:
                face_tables.neg_table[i][j] = 0.001
            else:
                face_tables.neg_table[i][j] /= face_tables.neg_count
    
    
    #calculate against the test data
    num_test_images = len(test_labels)
    correct = 0
    for n in range(num_test_images):
        prob_pos = 1.0
        prob_neg = 1.0
        for i in range(num_regions):
            region_count = test_data_regions[n][i]
            prob_pos *= face_tables.pos_table[i][region_count]
            prob_neg *= face_tables.neg_table[i][region_count]
        total_prob = (prob_pos * face_tables.pos_value)/(prob_neg * face_tables.neg_value)
        if total_prob >= 1 and test_labels[n] == 1:
            correct += 1
        elif total_prob < 1 and test_labels[n] == 0:
            correct += 1
    #calculate correctness
    percent_correct = float(correct)/float(num_test_images)
    #print(" correct "+str(percent_correct*100)+"% of the time")
    return percent_correct*100

def naive_bayes_d():
    return

def count_value(list, val):
    count = 0
    for entry in list:
        if entry == val:
            count += 1
    return count
    
def get_max_index(list):
    out = 0
    for i in range(1,len(list)):
        if list[i] > list[out]:
            out = i
    return out
#type = input("Enter the type of data to run ('f' for faces or 'd' for digits): ")
#percent = input("Enter the percentage of images to train against (0.5 for 50%): ")
#algorithm = input("Enter the algorithm to use ('p' for perceptron, 'n' for naive bayes, 'o' other algortihm TBD): ")

type = 'f'
percent = 1.0
algorithm = 'n'

num_x_regions = 10
num_y_regions = 10

labels = training_labels(type,1.0)
data_regions = training_data(type,1.0, num_x_regions, num_y_regions)

test_labels = test_labels(type,1.0)
test_data_regions = test_data(type,1.0, num_x_regions, num_y_regions)

sum = 0
runs = 10
if algorithm == 'n':
    steps = [x*0.1 for x in range(1,int((percent*10)+1))]
    for step in steps:
        if type == 'f':
            val = naive_bayes_f(labels, data_regions, step, test_labels, test_data_regions)
            print(str(step)+"% of training data was correct "+str(val)+"% of the time")
            sum += val
        else:
            naive_bayes_d()
    print("average correctness = "+str((sum/len(steps))))
elif algorithm == 'p':
    for i in range(runs):
        if type == 'f':
            sum += perceptron_d(labels, data_regions, percent, test_labels, test_data_regions)
        else:
            sum += perceptron_f(labels, data_regions, percent, test_labels, test_data_regions)
    print("average correctness = "+str((sum/runs)*100))
#TODO MIRA