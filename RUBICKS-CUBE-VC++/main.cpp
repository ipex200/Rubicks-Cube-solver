#include <iostream>
#include <stack>
#include <chrono>
#include <string>
#include <set>
#include <algorithm>
#include <vector>
#include <variant> 
#include <unordered_set>
#include "heuristic_dictionaries.cpp"
#include "move.cpp"

// Define a hash function for cube_type
struct CubeHash {
    size_t operator()(const cube_type& cube) const {
        std::hash<unsigned char> hasher;
        size_t seed = 0;
        for (const auto& i : cube) {
            seed ^= hasher(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};

// Some useful variables
struct Node {
    MoveFunc move;   // function pointer
    float f;         // f-score
    cube_type cube;  // cube state
    int g;           // g-score
};

std::array<unsigned char, 54> cube = {0,0,0,0,0,0,0,0,0 ,1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,
                                      3,3,3,3,3,3,3,3,3 ,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,};

std::array<unsigned char, 54> goal = {0,0,0,0,0,0,0,0,0 ,1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,
                                      3,3,3,3,3,3,3,3,3 ,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5};
std::array<int,27> hashed_cube;
void(*previous_move)(cube_type&) ;
std::string previous_move_name;
std::stack<Node> open_state;
std::vector<Node> pre_open; // change this line later
std::array<MoveFunc, 18> move_set = {move_U1, move_R1, move_B1, move_L1, move_D1, move_F1,
                                      move_U2, move_R2, move_B2, move_L2, move_D2, move_F2,
                                      move_UU, move_DD, move_LL, move_RR, move_FF, move_BB};

// Precomputed move lists

std::unordered_map<MoveFunc, int> moveTypeMap;
std::unordered_set<cube_type, CubeHash> before; // use unordered_set with hash
std::unordered_map<std::string, int> face_classification = 
                {{"move_B1", 1}, {"move_B2", 1}, {"move_BB", 1}, {"move_U1", 2}, {"move_U2", 2}, {"move_UU", 2},
                 {"move_D1", 1}, {"move_D2", 1}, {"move_DD", 1}, {"move_F1", 2}, {"move_F2", 2}, {"move_FF", 2},
                 {"move_L1", 1}, {"move_L2", 1}, {"move_LL", 1}, {"move_R1", 2}, {"move_R2", 2},  {"move_RR", 2}};

bool continue_algo = true;

char g ;
int iteration=0;
int total_distance_edge=0;
int total_distance_corner=0;
float threshold=0;
long long htime=0;

// Replace your current heuristic function with this optimized version
inline float heuristic(cube_type& cube) {
    auto start = std::chrono::high_resolution_clock::now();
    int total_distance_edge;
    int total_distance_corner;
    
    // Compute all corner hashes directly (no loops)
    total_distance_corner = corner_data_base[cube[0]*19683 + cube[27]*729 + cube[20]*27]+ corner_data_base[cube[33]*19683 + cube[26]*729 + cube[51]*27 + 2]+ corner_data_base[cube[2]*19683 + cube[11]*729 + cube[18]*27 + 6]+ corner_data_base[cube[17]*19683 + cube[24]*729 + cube[53]*27 + 8]+ corner_data_base[cube[6]*19683 + cube[36]*729 + cube[29]*27 + 18]+ corner_data_base[cube[42]*19683 + cube[35]*729 + cube[45]*27 + 20]+ corner_data_base[cube[8]*19683 + cube[38]*729 + cube[9]*27 + 24]+ corner_data_base[cube[44]*19683 + cube[15]*729 + cube[47]*27 + 26];
    
    // Compute all edge hashes directly (no loops)
    total_distance_edge  = edge_data_base[cube[30]*729 + cube[23]*27 + 1]+ edge_data_base[cube[1]*729 + cube[19]*27 + 3]+ edge_data_base[cube[25]*729 + cube[52]*27 + 5]+ edge_data_base[cube[14]*729 + cube[21]*27 + 7]+ edge_data_base[cube[3]*729 + cube[28]*27 + 9]+ edge_data_base[cube[34]*729 + cube[48]*27 + 11]+ edge_data_base[cube[5]*729 + cube[10]*27 + 15]+ edge_data_base[cube[16]*729 + cube[50]*27 + 17]+ edge_data_base[cube[39]*729 + cube[32]*27 + 19]+ edge_data_base[cube[7]*729 + cube[37]*27 + 21]+ edge_data_base[cube[43]*729 + cube[46]*27 + 23]+ edge_data_base[cube[41]*729 + cube[12]*27 + 25];
    
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::micro> elapsed = end - start;
    htime += elapsed.count();
    
    return total_distance_edge/4+total_distance_corner;

}
    


long long total_get_f_scores_time = 0;

void get_f_scores(float& threshold, cube_type& cube, std::vector<Node>& pre_open, std::stack<Node>& open_state, std::unordered_map<std::string, int>& face_classification, char& g, void(*previous_move)(cube_type&)) {
    auto start = std::chrono::high_resolution_clock::now();
    pre_open.clear();
    
    
    if (!open_state.empty()) {
        g = open_state.top().g + 1;
        previous_move = open_state.top().move;
        previous_move_name = funcNames[previous_move];
    } else {
        g = 1;
        previous_move = No_move;
        previous_move_name = funcNames[previous_move];
    }

    // Use precomputed allowedMovesMap
    std::vector<MoveFunc> allowedMoves;
    if (previous_move == No_move) {
        allowedMoves.assign(move_set.begin(), move_set.end());
    } else {
        allowedMoves = allowedMovesMap[previous_move];
    }
    auto reset = cube;

    for (const MoveFunc& move : allowedMoves) {
        move(cube);
        if (before.find(cube) == before.end()) {
            float h = heuristic(cube);
            float f = g + h;
            if (f <= threshold) {
                pre_open.push_back(Node{move, f, cube, g});
            }
            before.insert(cube);
        }
        cube = std::move(reset);
    }
    std::sort(pre_open.begin(), pre_open.end(), [](const Node &a, const Node &b) { return a.f < b.f; });
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::micro> elapsed = end - start;
    total_get_f_scores_time += elapsed.count();
}

int main() {
  
    auto start_time = std::chrono::high_resolution_clock::now();
    pre_open.reserve(18);  
before.reserve(500'000);
    // Scramble the cube
    move_D2(cube);
    move_U1(cube);
    move_B1(cube);
    move_L2(cube);
    move_R1(cube);
    move_F2(cube);
    move_RR(cube);
    move_L1(cube);
    move_U1(cube);
    move_F1(cube);
    auto start_cube = cube;

    while (continue_algo) {
        before.clear();
        iteration += 1;
        if (iteration == 1) {
            threshold = heuristic(cube);
            std::cout << "iteration: " << iteration << " threshold: " << threshold << std::endl;
            get_f_scores(threshold, cube, pre_open, open_state, face_classification, g, previous_move);
            for (const Node& element : pre_open) {
                open_state.push(element);
            }
            while (!open_state.empty()) {
                cube = open_state.top().cube;
                if (cube == goal) {
                    continue_algo = false;
                    break;
                }
                get_f_scores(threshold, cube, pre_open, open_state, face_classification, g, previous_move);
                open_state.pop();
                for (const Node& element : pre_open) {
                    open_state.push(element);
                }
            }
        } else {
            cube = start_cube;
            threshold += 0.25;
            std::cout << "iteration: " << iteration << " threshold: " << threshold << std::endl;
            get_f_scores(threshold, cube, pre_open, open_state, face_classification, g, previous_move);
            for (const Node& element : pre_open) {
                open_state.push(element);
            }
            while (!open_state.empty()) {
                cube = open_state.top().cube;
                if (cube == goal) {
                    continue_algo = false;
                    break;
                }
                get_f_scores(threshold, cube, pre_open, open_state, face_classification, g, previous_move);
                open_state.pop();
                for (const Node& element : pre_open) {
                    open_state.push(element);
                }
            }
        }
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
    std::cout << "si tu vois cela cest que sa marche!!!!!" << std::endl;
    std::cout << "------program execution time: " << duration << " micro seconds ------" << std::endl;
    std::cout << "---get_fscore execution time: " << total_get_f_scores_time << " micro second ---" << std::endl;
    std::cout << "----heuristic execution time: " << htime << " micro second ----" << std::endl;

    return 0;
}