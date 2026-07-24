#include <array>
#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

 /* W : 0
    R: 1
    B: 2
    O: 3
    G: 4
    Y: 5*/
    using cube_type= std::array<std::string,48> ;

void cube_represented_as_2D(cube_type cube){
  int i;
  std::array<std::string,6> faces= {"⬜","🟥","🟦","🟧","🟩","🟨"};
  for (int x=0;x<6;x++){
    i=x*8;
    std::cout<<cube[i+0]<<" "<<cube[i+1]<<" "<<cube[i+2]<<std::endl;
    std::cout<<cube[i+7]<<" "<<faces[x]<<" "<<cube[i+3]<<std::endl;
    std::cout<<cube[i+6]<<" "<<cube[i+5]<<" "<<cube[i+4]<<std::endl;
    std::cout<<std::endl;
  }
}
 
cube_type cube_T=  {"W0","W1","W2","W3","W4","W5","W6","W7",  "R0","R1","R2","R3","R4","R5","R6","R7",
                    "B0","B1","B2","B3","B4","B5","B6","B7",  "O0","O1","O2","O3","O4","O5","O6","O7",
                    "G0","G1","G2","G3","G4","G5","G6","G7",  "Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7"};

using MoveFunc = void (*)(std::array<unsigned char,54>&);

void move_U1_T(cube_type& cube){
   // rotate right by 2
std::rotate(cube.begin(), cube.begin()+6, cube.begin() + 8);
}
