from matplotlib import image
from matplotlib import pyplot
import os
# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

filename2 = path + '/' + 'south-korea-flag-xs.jpeg'
data2 = image.imread(filename2)

# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

print('Image 2 type is: ', type(data2))
print('Image 2 shape is: ', data2.shape)

# modify an image array with another image of dimensions 250,167
plot_data = data.copy()
plot_data2=data2.copy()
for width in range (data2.shape[1]):
    for height in range(data2.shape[0]):
        plot_data[height][width+262] = plot_data2[height][width]

# Write the modified images
modified_filename = os.path.join(path, 'lenna-mod.jpg')
image.imsave(modified_filename, plot_data)

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()

