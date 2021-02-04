#include <stdio.h> //input and output for debugging
#include <linux/types.h> //types

//takes in an image, and produces an ascii version of it

int main()  {
   //converts all .png files inside ../imagesForProcessing into the ascii version
   //this ascii version is stored inside ../tempFiles
   
   //as source video is black-grey-white, RGB are all the same, and so we can use any for brightness
   //so map the colour 0-255 to a coresponding ascii character, based on brighness
   //output as a text file
   //each frame will be its own text file
   //
   //how tall and wide? has to be some factor of 1980x1080 
   //170 is the max width
   //so why not go max width 160, as it is a nice clean factor,
   //each character is 12x12 pixels
   //need to get average for them then
   //
}
