import numpy as np
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
    #print(num_test_images)
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
    region_max = int((60*70) / num_regions)+1
    face_tables = Table(num_regions, region_max)
    
    face_tables.pos_count = count_value(training_labels, 1)
    face_tables.pos_value = float(face_tables.pos_count / num_training_images)
    face_tables.neg_count = num_training_images - face_tables.pos_count
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

def naive_bayes_d(training_labels, training_regions, percent, test_labels, test_data_regions):
    #init needed value
    num_training_images = int(len(training_labels) * percent)
    num_regions = len(training_regions[0])
    
    #init table class
    #since type is f, image is 28x28
    region_max = int((28*28) / num_regions)+1
    face_tables = []
    for i in range(10):
        face_tables.append(Table(num_regions, region_max))
    
    for i in range(len(face_tables)):
        face_tables[i].pos_count = count_value(training_labels, i)
        face_tables[i].pos_value = float(face_tables[i].pos_count / num_training_images)
        face_tables[i].neg_count = num_training_images - face_tables[i].pos_count
        face_tables[i].neg_value = float(face_tables[i].neg_count / num_training_images)
    
    #fill face tables
    for i in range(num_regions):
        for j in range(num_training_images):
            count = training_regions[j][i]
            label = training_labels[j]
            for k in range(len(face_tables)):
                if label == k:
                    #print("k="+str(k)+" max k="+str(len(face_tables)))
                    #print("i="+str(i)+" max i="+str(len(face_tables[k].pos_table)))
                    #print("count="+str(count)+" max count="+str(len(face_tables[k].pos_table[i])))
                    face_tables[k].pos_table[i][count] += 1
                else:
                    face_tables[k].neg_table[i][count] += 1
    
    for k in range(len(face_tables)):
        for i in range(len(face_tables[k].pos_table)):
            for j in range(len(face_tables[k].pos_table[0])):
                if face_tables[k].pos_table[i][j] == 0:
                    face_tables[k].pos_table[i][j] = 0.0001
                else:
                    face_tables[k].pos_table[i][j] /= face_tables[k].pos_count
            
                if face_tables[k].neg_table[i][j] == 0:
                    face_tables[k].neg_table[i][j] = 0.001
                else:
                    face_tables[k].neg_table[i][j] /= face_tables[k].neg_count
                    
    num_test_images = len(test_labels)
    correct = 0
    for n in range(num_test_images):
        prob_pos = [1.0 for x in range(10)]
        prob_neg = [1.0 for x in range(10)]
        for i in range(num_regions):
            region_count = test_data_regions[n][i]
            for k in range(10):
                prob_pos[k] *= face_tables[k].pos_table[i][region_count]
                prob_neg[k] *= face_tables[k].neg_table[i][region_count]
        total_prob = []
        for i in range(10):
            total_prob.append((prob_pos[i] * face_tables[i].pos_value)/(prob_neg[i] * face_tables[i].neg_value))
        max_index = get_max_index(total_prob)
        if max_index == test_labels[n]:
            correct += 1
    
    percent_correct = float(correct)/float(num_test_images)
    return percent_correct*100

def mira_f(labels, regions, percent, test_labels, test_data_regions):
    #init important values
    num_images = len(labels)
    num_regions = len(regions[0])
    #print("num_images="+str(num_images))
    
    bias_f = random.choice([-1,0,1])
    bias_nf = random.choice([-1,0,1])
    #create array of w values
    w_f = []
    w_nf = []
    #print("w before training")
    for i in range(num_regions):
        w_f.append(random.choice([-1,0,1]))
        w_nf.append(random.choice([-1,0,1]))
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
            f_f = 0
            f_nf = 0
            for i in range(num_regions):
                f_f += (w_f[i]*regions[n][i])
                f_nf += (w_nf[i]*regions[n][i])
            f_f += bias_f
            f_nf += bias_nf
            if np.all(f_f >= f_nf) and labels[n] != 1:
                sub = np.subtract(w_f, w_nf)
                up = np.dot(sub, regions[n]) + 1
                den = np.dot(regions[n], regions[n]) * 2
                t = up / den
                #print(t)
                c = 0.0013
                t = min(t, c)
                tf = np.multiply(t, regions[n])
                w_f = np.subtract(w_f, tf)
                w_nf = np.add(w_nf, tf)
                bias_f -= tf
                bias_nf += tf
            elif np.all(f_f < f_nf) and labels[n] == 1:
                sub = np.subtract(w_nf, w_f)
                up = np.dot(sub, regions[n]) + 1
                den = np.dot(regions[n], regions[n]) * 2
                t = up / den
                #print(t)
                c = 0.0013
                t = min(t, c)
                tf = np.multiply(t, regions[n])
                w_f = np.add(w_f, tf)
                w_nf = np.subtract(w_nf, tf)
                bias_f += tf
                bias_nf -= tf
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
        f_f_t = 0
        f_nf_t = 0
        for i in range(num_regions):
            f_f_t += (w_f[i]*test_data_regions[n][i])
            f_nf_t += (w_nf[i]*test_data_regions[n][i])
        f_f_t += bias_f
        f_nf_t += bias_nf
        if np.all(f_f_t >= f_nf_t) and test_labels[n]==1:
            correct += 1
        elif np.all(f_f_t < f_nf_t) and test_labels[n] == 0:
            correct += 1
    
    #Output results somehow
    percent_correct = float(correct)/float(num_test_images)
    print(" correct "+str(percent_correct*100)+"% of the time")
    return percent_correct

def mira_d(labels, regions, percent, test_labels, test_data_regions):
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
            max_index = np_get_max_index(f)
            #print("max x = f["+str(max_index)+"] = "+str(f[max_index]))
            #print("label = "+str(labels[n]))
            if max_index != labels[n]:
                penalties += 1
                # wy = w[max_index]
                # wy* = w[labels[n]]
                # f = region[n]
                #decrease w of max_index and increase w of labels[n]
                sub = np.subtract(w[max_index], w[labels[n]])
                up = np.dot(sub, regions[n]) + 1
                den = np.dot(regions[n], regions[n]) * 2
                t = up / den
                #print(t)
                c = 0.005
                t = min(t, c)
                # print(t)
                tf = np.multiply(t, regions[n])
                w[max_index] = np.subtract(w[max_index], tf)
                w[labels[n]] = np.add(w[labels[n]], tf)
                '''
                for i in range(num_regions):
                    w[max_index][i] -= regions[n][i]
                    w[labels[n]][i] += regions[n][i]
                '''
                #decrease bias of max_index
                bias[max_index] -= tf
                #increase bias of labels[n]
                bias[labels[n]] += tf
        #print("penalties = "+str(penalties))
    #data to test against
    #test_labels ad test_data_regions
    #Perform tests for get f value for each image
    correct = 0
    num_test_images = len(test_labels)
    #print(num_test_images)
    #print("num test images = "+str(num_test_images))
    for n in range(num_test_images):
        f = [0 for i in range(10)]
        for i in range(len(f)):
            for j in range(num_regions):
                f[i] += (w[i][j]*test_data_regions[n][j])
                
            f[i] += bias[i]
        max_index = np_get_max_index(f)
        if max_index == test_labels[n]:
            correct += 1
            
    percent_correct = float(correct)/float(num_test_images)
    print(" correct "+str(percent_correct*100)+"% of the time")
    return percent_correct

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

def np_get_max_index(list):
    out = 0
    for i in range(1,len(list)):
        if np.all(list[i] > list[out]):
            out = i
    return out
#type = input("Enter the type of data to run ('f' for faces or 'd' for digits): ")
#percent = input("Enter the percentage of images to train against (0.5 for 50%): ")
#algorithm = input("Enter the algorithm to use ('p' for perceptron, 'n' for naive bayes, 'o' other algortihm TBD): ")

type = 'd'
percent = 1.0
algorithm = 'o'

num_x_regions = 7
num_y_regions = 7

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
            print(str(int(step*100))+"% of training data was correct "+str(val)+"% of the time")
            sum += val
        else:
            val = naive_bayes_d(labels, data_regions, step, test_labels, test_data_regions)
            print(str(int(step*100))+"% of training data was correct "+str(val)+"% of the time")
            sum += val
    print("average correctness = "+str((sum/len(steps))))
elif algorithm == 'p':
    for i in range(runs):
        if type == 'f':
            sum += perceptron_d(labels, data_regions, percent, test_labels, test_data_regions)
        else:
            sum += perceptron_f(labels, data_regions, percent, test_labels, test_data_regions)
    print("average correctness = "+str((sum/runs)*100))
else:
    for i in range(runs):
        if type == 'f':
            sum += mira_f(labels, data_regions, percent, test_labels, test_data_regions)
        else:
            sum += mira_d(labels, data_regions, percent, test_labels, test_data_regions)
    print("average correctness = "+str((sum/runs)*100))