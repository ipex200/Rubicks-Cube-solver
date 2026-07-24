#include <array>
#include <iostream>
#include <chrono>
#include "test.cpp"
 /* W : 0
    R: 1
    B: 2
    O: 3
    G: 4
    Y: 5
        */

std::array<unsigned char,12> temp_side;
std::array<unsigned char,9> temp_face;  
using cube_type_O= std::array<unsigned char,54> ;
using MoveFunc = void (*)(std::array<unsigned char,54>&);
cube_type_O cube_O=  {10,20,30,40,50,60,70,80,90 ,11,21,31,41,51,61,71,81,91, 12,22,32,42,52,62,72,82,92,
                   13,23,33,43,53,63,73,83,93 ,14,14,24,34,44,54,64,74,84, 95,95,95,95,95,95,95,95,95,};
void move_U1_O(cube_type_O cube){
    temp_face={ cube[6], cube[3], cube[0],cube[7], cube[4], cube[1],cube[8], cube[5], cube[2]};
    cube[0]= temp_face[0];cube[1]=temp_face[1] ;cube[2]=temp_face[2] ;cube[3]=temp_face[3] ;cube[4]=temp_face[4] ;cube[5]= temp_face[5];cube[6]= temp_face[6] ;cube[7]= temp_face[7] ;cube[8]=temp_face[8];
}
int main(){
    auto start_time = std::chrono::high_resolution_clock::now();

    for (int i=0;i<100'000'000; ++i){
        move_U1_O(cube_O);
        
    }
    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::seconds>(end_time - start_time).count();
    std::cout << "------assigment execution time: " << duration << "  seconds ------"<<std::endl;
    start_time = std::chrono::high_resolution_clock::now();

    for (int i=0;i<100'000'000; ++i){
        move_U1_T(cube_T);
        
    }
    end_time = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::seconds>(end_time - start_time).count();
    std::cout << "------shift execution time: " << duration << "  seconds ------"
;
    return 0;
}