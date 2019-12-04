from pathlib import Path

#Utility function
#Takes a file path in and returns how many lines are in the file
def file_length(file_name):
    num_lines = sum(1 for line in open(file_name))
    return num_lines;

#Utility function
#Takes a file path in and returns the length of the widest line in the file
def file_width(file_name):
    width = 0
    file = open(file_name,"r")
    lines = file.readlines()
    for i in range(len(lines)):
        length = len(lines[i])
        if width < length:
            width = length
    file.close()
    return width-1;

#Main function
#inputs: type ('f'ace or 'i'mage), percent (percentage of training data to collect)
#output: 2d list containing region counts for each image collected from training data
def training_data(type,percent):
    #determine which training file to open
    file_name = ""
    labels_name = ""
    if type == 'f':
        file_name = "facedatatrain"
        labels_name = "facedatatrainlabels"
    elif type == 'i':
        file_name = "trainingimages"
        labels_name = "traininglabels"
    else:
        print("input type must be 'f' or 'i'.")
        return []
    #calculate length and width of training file
    data_folder = Path("./data")
    data_path = data_folder / file_name
    labels_path = data_folder / labels_name
    data_length = file_length(data_path)
    data_width = file_width(data_path)
    labels_length = file_length(labels_path)
    
    length_per_image = int(data_length/labels_length)
    num_images = int(labels_length*percent)
    
    num_x_regions = 6
    num_y_regions = 6
    total_regions = num_x_regions*num_y_regions
    x_region_size = int(data_width/num_x_regions)
    y_region_size = int(length_per_image/num_y_regions)

    output = [[0 for i in range(total_regions)] for j in range(num_images)]
    
    file = open(data_path,"r")
    for n in range(num_images):
        #print("image "+str(n))
        for j in range((int(length_per_image))):
            line = file.readline()
            calc_j = j
            if calc_j >= (num_y_regions * y_region_size):
                calc_j = (num_y_regions * y_region_size)-1
            for i in range(len(line)):
                calc_i = i
                if calc_i >= (num_x_regions * x_region_size):
                    calc_i = (num_x_regions * x_region_size)-1
                index = (int(calc_j/y_region_size) * num_x_regions) + int(calc_i/x_region_size)
                '''
                print("i:"+str(i)+" j:"+str(j)+" is region:"+str(index))
                if index == (num_x_regions * num_y_regions):
                    print("calc_i = "+str(calc_i)+" calc_j = "+str(calc_j))
                    print("y size = "+str(y_region_size)+" x size = "+str(x_region_size))
                '''
                if line[i] != ' ':
                    #print("index="+str(index)+" total_regions="+str(total_regions))
                    output[n][index] += 1
    file.close()
    #print(total_regions)
    #print(num_images)
    return output

#Main function
#inputs: type ('f'ace or 'i'mage), percent (percentage of training labels to collect)
#output: list containing the training labels as ints
def training_labels(type,percent):
    #determine which training file to open
    file_name = ""
    if type == 'f':
        file_name = "facedatatrainlabels"
    elif type == 'i':
        file_name = "traininglabels"
    else:
        print("input type must be 'f' or 'i'.")
        return []
    #calculate length of training file
    data_folder = Path("./data")
    path = data_folder / file_name
    length = file_length(path)
    #apply percentage to length
    output_size = int(length*percent)
    #open file
    file = open(path,"r")
    output = []
    #for [0,length*percent] read line
        #append line as int to output list
    for i in range(output_size):
        line = file.readline()
        output.append(int(line))
    #close file and return
    file.close()
    return output
