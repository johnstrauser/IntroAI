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
    num_y_regions = 7
    total_regions = num_x_regions*num_y_regions
    x_region_size = int(data_width/num_x_regions)
    y_region_size = int(length_per_image/num_y_regions)

    output = [[0 for i in range(num_images)] for j in range(total_regions)]
    
    file = open(data_path,"r")
    for n in range(num_images):
        #print("image "+str(n))
        for i in range((int(length_per_image))):
            line = file.readline()
            for j in range(len(line)):
                index = (int(j/y_region_size) * num_x_regions) + int(i/x_region_size)
                #print("i:"+str(i)+" j:"+str(j)+" is region:"+str(index))
                if index > total_regions:
                    index = total_regions
                if line[j] != ' ':
                    #print("index="+str(index)+" total_regions="+str(total_regions))
                    output[index-1][n] += 1
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
'''
# load the file, store the first image into the 'image' list
#image = []
#file1 = open("facedatatrain.txt","r")
data_folder = Path("./all_data_needed/facedata")
trainingName = "facedatatrain"
labelsName = "facedatatrainlabels"
trainingPath = data_folder / trainingName
labelPath = data_folder / labelsName

trainingLength = file_length(trainingPath)
labelLength = file_length(labelPath)

lengthPerImage = trainingLength/labelLength

#This is the percent of images we want to g
percentImages = 0.01
numImages = int(labelLength*percentImages)
print("numImages = "+str(numImages))

num_x_regions = 6
num_y_regions = 7
total_regions = num_x_regions*num_y_regions
x_region_size = int(60/num_x_regions)
y_region_size = int(70/num_y_regions)

output = [[0 for i in range(numImages)] for j in range(total_regions)]

for i in range(total_regions):
    for j in range(numImages):
        print(output[i][j], end=" ")
    print("")
    
trainingFile = open(trainingPath,"r")
for n in range(numImages):
    #print("image "+str(n))
    for i in range((int(lengthPerImage))):
        line = trainingFile.readline()
        for j in range(len(line)):
            index = (int(j/y_region_size) * num_x_regions) + int(i/x_region_size)
            print("i:"+str(i)+" j:"+str(j)+" is region:"+str(index))
            if line[j] != ' ':
                print("index="+str(index)+" total_regions="+str(total_regions))
                output[index-1][n] += 1

for i in range(total_regions):
    for j in range(numImages):
        print(output[i][j], end=" ")
    print("")
'''