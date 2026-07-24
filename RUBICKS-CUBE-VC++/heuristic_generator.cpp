#include <iostream>
#include <chrono>
#include <string>
#include <deque>
#include <vector>
#include <unordered_set>
#include "move.cpp"

// Some useful variables
struct Node {
    char move;   // function pointer
    char g;              // g-score
    cube_type cube;  // cube state

};

std::array<unsigned char, 54> cube = {0,0,0,0,0,0,0,0,0 ,1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,
                                      3,3,3,3,3,3,3,3,3 ,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,};

std::array<unsigned char, 54> goal = {0,0,0,0,0,0,0,0,0 ,1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,
                                      3,3,3,3,3,3,3,3,3 ,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5};
std::array<int,27> hashed_cube;
void(*previous_move)(cube_type&) ;
std::string previous_move_name;
std::deque<Node> open_state;
std::array<MoveFunc, 18> move_set = {move_U1, move_R1, move_B1, move_L1, move_D1, move_F1,
                                      move_U2, move_R2, move_B2, move_L2, move_D2, move_F2,
                                      move_UU, move_DD, move_LL, move_RR, move_FF, move_BB};
    
// Precomputed move lists

std::unordered_map<MoveFunc, int> moveTypeMap;

bool continue_algo = true;
int depth_to_stop = 6;
char g ;
int iteration=0;
int total_distance_edge=0;
int total_distance_corner=0;
float threshold=0;
long long htime=0;

// Replace your current heuristic function with this optimized version


long long total_get_f_scores_time = 0;

void get_f_scores(float& threshold, cube_type& cube , std::deque<Node>& open_state , char& g, void(*previous_move)(cube_type&)) {
    auto start = std::chrono::high_resolution_clock::now();
    
    
    if (!open_state.empty()) {
        g = open_state.front().g + 1;
        previous_move = map_number_to_move[open_state.front().move];
    } else {
        g = 1;
        previous_move = No_move;
    }

    // Use precomputed allowedMovesMap
    std::vector<MoveFunc> allowedMoves;
    if (previous_move == No_move) {
        allowedMoves.assign(move_set.begin(), move_set.end());
    } else {
        allowedMoves = allowedMovesMap[previous_move];
    }

    for (const MoveFunc& move : allowedMoves) {
        move(cube);
            if (g <= threshold) {
                open_state.push_back(Node{map_move_to_number[move], g, cube,});

            }
        
        cube = open_state.front().cube;
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::micro> elapsed = end - start;
    total_get_f_scores_time += elapsed.count();
}

int main() {
  
    auto start_time = std::chrono::high_resolution_clock::now();
    auto start_cube = cube;
    while(continue_algo){
        iteration += 1;
        if (iteration == 1) {
            threshold = 0;
            std::cout << "iteration: " << iteration << " threshold: " << threshold << std::endl;
            get_f_scores(threshold, cube,open_state , g, previous_move);
                }
            
     else {
            cube = start_cube;
            threshold += depth_to_stop;
            std::cout << "iteration: " << iteration << " threshold: " << threshold << std::endl;
            get_f_scores(threshold, cube,open_state , g, previous_move);
            while (!open_state.empty()) {
                cube = open_state.front().cube;
                if (open_state.front().g==depth_to_stop) {
                    continue_algo = false;           

                    break;
                }
            get_f_scores(threshold, cube,open_state , g, previous_move);
            open_state.pop_front();
                
                }
            }
        }
    

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
    std::cout << "si tu vois cela cest que sa marche!!!!!" << std::endl;

    /*for (Node element :open_state){
    for (int x : element.cube)
        std::cout << x;
    std::cout << ": " << element.g<<"\\";    }\*/

    size_t memory_bytes = open_state.size() * (sizeof(open_state.front()));
    std::cout << "open_state memory ≈ "<< memory_bytes / 1024.0 << " KB "<<sizeof(open_state.front())<<"b"<<std::endl;
    std::cout << "------program execution time: " << duration << " micro seconds ------" << std::endl;
    std::cout << "---get_fscore execution time: " << total_get_f_scores_time << " micro second ---" << std::endl;
    return 0;
}