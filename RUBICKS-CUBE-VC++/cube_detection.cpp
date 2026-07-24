#include <iostream>
#include <unordered_map>
#include<array>
std::unordered_map<char,std::string> letter_to_color={
  {'W',"⬜"},
  {'w',"⬜"},
  {'R',"🟥"},
  {'r',"🟥"},
  {'B',"🟦"},
  {'b',"🟦"},
  {'O',"🟧"},
  {'o',"🟧"},
  {'G',"🟩"},
  {'g',"🟩"},
  {'Y',"🟨"},
  {'y',"🟨"},
};
void get_input_cube(){
  std::array<std::string,6> arrows= {"↑","←","←","←","← ↑","no turn"};
  std::array<std::string,6> faces= {"White face","Green face","Red face","Blue face","Orange face","Yellow face"};

  std::cout<<"INSTRUCTIONS"<<std::endl;
  std::cout<<"----------------------------------------------------------------------------------------------------------------"<<std::endl;
  std::cout<<"_Enter the cube configuration as a string of 54 characters (W,R,B,O,G,Y) "<<std::endl;
  std::cout<<"_make sure thaet the WHITE face is facing you and the GREEN face is at the bottom"<<std::endl; 
  std::cout<<"----------------------------------------------------------------------------------------------------------------"<<std::endl;

  for(int current_face=0;current_face<6;current_face++){
  std::cout<<"_enter the colors on the  face by starting from top left to bottom right: "<<std::endl;
  std::string input = "oywrgboow";
  
  //u are supposed to use cin to defin input
  for(int i =0;i<3;i++){
    for(int j=0;j<3;j++){
       std::cout<<letter_to_color[input[i*3+j]];
       if (i==1 && j==2){
        std::cout<<faces[current_face]<<" turn: "<<arrows[current_face];
                        }
                        }
    std::cout <<std::endl;
    }

    std::cout <<std::endl;
                                 }
}
int main(){
  get_input_cube();

  return 0;
}