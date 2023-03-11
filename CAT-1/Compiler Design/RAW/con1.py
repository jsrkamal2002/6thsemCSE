# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
print("Enter the file name:")
filename = input()
print("File name is: " + filename)
print("started!!!")
images = convert_from_path(filename+'.pdf')
# print(images)

for i in range(len(images)):

    # Save pages as images in the pdf
    images[i].save('page' + str(i) + '.jpg', 'JPEG')

print("Done")
