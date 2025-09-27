
#include <iostream>
#include <chrono>

//some usefull variables


int main() {
    
    int a=7;
    int b =4;
    b= std::move(a);
    std::cout<<a;

    return 0;
} 