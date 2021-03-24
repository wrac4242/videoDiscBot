from PIL import Image
import time
import numpy as np

#64 characters, makes maths easier
colour_converter = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvuxrjft/\|(1{[?-_+~<i!lI;:,\"^`. "

#converts grayscale image to ascii
def png_to_ascii(file_path_in, dir_out, intended_height, intended_width):
    start_time = time.time()

    img = Image.open(file_path_in)

    file_out = dir_out + file_path_in.split("/")[-1]
    print(file_out)
    #loads the image in
    #splits the image into chunks based on height and width
    #output colour is the average of those pixels
    #stored in a 2d array
    #outputs the first row, then a newline, then the 2nd row, etc
    #done based on a threshold
    print("converting {0} to ascii text".format(file_path_in))

    brightness_array = np.zeros((intended_height, intended_width))

    #code to convert image into a 2d array of lower quality, with brightness between 0 and 255

    #code to convert brightness_array into the text

    print("{0} converted, took {1} seconds".format(file_path_in, time.time()-start_time))
    print(brightness_array)
    #outputted file name is the same as the input file, but .txt and in dir_out
print(len(colour_converter))
#png_to_ascii("/home/wrac/videoDiscBot/imagesForProcessing/bad_apple_images/bad_apple_0002288.png","../out_files/", 10, 10)
