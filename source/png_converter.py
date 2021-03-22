
#converts grayscale image to ascii
def png_to_ascii(file_path_in, dir_out, intended_height, intended_width):
    #loads the image in
    #splits the image into chunks based on height and width
    #output colour is the average of those pixels
    #stored in a 2d array
    #outputs the first row, then a newline, then the 2nd row, etc
    #done based on a threshold

    #outputted file name is the same as the input file, but .txt and in dir_out
