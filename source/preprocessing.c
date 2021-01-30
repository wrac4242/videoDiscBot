#include <stdio.h> //input and output for debugging
#include <linux/types.h> //types

//takes in an image, and produces an ascii version of it

int main( int argc, char *argv[] )  {

   if( argc == 2 ) {
      printf("The file supplied is %s\n", argv[1]);
   }
   else if( argc > 2 ) {
      printf("Too many arguments supplied.\n");
   }
   else {
      printf("One argument expected.\n");
   }
}
