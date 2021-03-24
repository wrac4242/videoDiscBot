from PIL import Image
import time
#converts grayscale image to ascii
def png_to_ascii(file_path_in, dir_out, intended_height, intended_width):
    start_time = time.time()

    img = Image.open(file_path_in)

    file_out = dir_out + file_path_in.split("/")[-1]

    #loads the image in
    #splits the image into chunks based on height and width
    #output colour is the average of those pixels
    #stored in a 2d array
    #outputs the first row, then a newline, then the 2nd row, etc
    #done based on a threshold
    print("converting {0} to ascii text".format(file_path_in))


    print("{0} converted, took {1} seconds".format(file_path_in, time.time()-start_time))

    #outputted file name is the same as the input file, but .txt and in dir_out
