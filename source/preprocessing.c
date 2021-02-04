#include <stdio.h> //input and output for debugging
#include <linux/types.h> //types

//takes in an image, and produces an ascii version of it

int main()  {
   //converts all .png files inside ../imagesForProcessing into the ascii version
   //this ascii version is stored inside ../tempFiles
   
   //as source video is black-grey-white, RGB are all the same, and so we can use any for brightness
   //so map the colour 0-255 to a coresponding ascii character, based on brighness
   //output as a text file
}
