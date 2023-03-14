# import module
import os
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
print("Enter the file name:")
filename = input()
print("File name is: " + filename)
print("Folder Created !!!")
print("started to convert!!!")
images = convert_from_path(filename+'.pdf')

# Folder creation
if not os.path.isdir(filename):
    os.mkdir(filename)


for i in range(len(images)):

    # Save pages as images in the pdf
    # images[i].save('page' + str(i) + '.jpg', 'JPEG')
    images[i].save(filename + '/' + 'page' + str(i) + '.jpg', 'JPEG')

print("Done")
