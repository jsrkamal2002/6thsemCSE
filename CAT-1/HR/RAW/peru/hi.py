import os
from pdf2image import convert_from_path

# specify the path of the directory you want to print the files from
path = "."

# get a list of all the files in the directory
files = os.listdir(path)

# loop through each file in the directory and print its name
for file in files:
    if file.endswith(".pdf"):
        # print(file)
        filename = os.path.splitext(file)[0]
        print("File name is: " + filename)
        print("Folder Created !!!")
        print("started to convert!!!")
        images = convert_from_path(filename+'.pdf')

        if not os.path.isdir(filename):
            os.mkdir(filename)

        for i in range(len(images)):
            images[i].save(filename + '/' + 'page' + str(i) + '.jpg', 'JPEG')

        print("Done !!!" + filename)
