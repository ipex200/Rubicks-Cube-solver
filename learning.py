from collections import deque
from functools import lru_cache
from heuristic_dictionaries import *
import time
from move import *
cube = bytearray(b"WWWWWWWWWRRRRRRRRRBBBBBBBBBOOOOOOOOOGGGGGGGGGYYYYYYYYY")
goal = bytearray(b"WWWWWWWWWRRRRRRRRRBBBBBBBBBOOOOOOOOOGGGGGGGGGYYYYYYYYY")


"""useful variables"""
open_state = deque()
pre_open = []
iteration = 0
calculated_heuristics= {}
move_set = (move_U1, move_R1, move_B1, move_L1, move_D1, move_F1,
             move_U2, move_R2, move_B2, move_L2, move_D2, move_F2,
             move_UU, move_DD, move_LL, move_RR, move_FF, move_BB)
continue_algo = True
continue_iteration = True
continue_search= True
before=set()
face_classification = {"move_B1": 1, "move_B2": 1, "move_BB": 1, "move_U1": 2, "move_U2": 2, "move_UU": 2,
                       "move_D1": 1, "move_D2": 1,"move_DD": 1, "move_F1": 2, "move_F2": 2, "move_FF": 2,
                       "move_L1": 1, "move_L2": 1, "move_LL": 1,"move_R1": 2,"move_R2": 2, "move_RR": 2}
global_start = time.time()
start_time = time.time()
"""functions"""
# calculate the heuristic for the current state of cube
lru_max= 2**28
@lru_cache(maxsize=lru_max)
def heuristic(current):
    current_cube= convert_to_3D_format(current)
    total_distance_edge=0
    total_distance_corner=0
    # Iterate over cubi all positions in the 3x3x3 cube and note that CBnbr represent the number corresponding
    #to the position of the cube like position 0 1 2 3 4 ... 26
    for C in edge_coordinate_list:
        cubie= current_cube[C]
        total_distance_edge+= edge_data_base[cubie]
    for C in corner_coordinate_list:
        cubie= current_cube[C]
        total_distance_corner+= corner_data_base[cubie]
    return max(total_distance_edge/4,total_distance_corner)
#function that allows me to print the cube in a bette way
def print_cube(cube):
    for a in range(0,6):
        for x in range(a*9,a*9+9,3):
            print(list(cube[x:x+3].decode()))
        print("")
# calculate the f_score and classify them  for every possible child of the current cube
fois=0
def get_f_scores(threshold,cube,pre_open,open_state,face_classification):
    global fois
    fois+=1
    pre_open.clear()

    if open_state:
        g= open_state[0][3]+1
        previous_move= open_state[0][0]
        previous_move_name= previous_move.__name__
        if face_classification[previous_move_name]== 1:
            possibility = [[move_U1,move_U2,move_UU],[move_DD,move_D1,move_D2],[move_B1,move_B2,move_BB],[move_FF,move_F1,move_F2],
                       [move_LL,move_L2,move_L1],[move_RR,move_R1,move_R2]]
        else:
            possibility = [[move_U1, move_U2, move_UU,move_DD, move_D1, move_D2],
                           [move_B1, move_B2, move_BB,move_FF, move_F1, move_F2],
                           [move_LL, move_L2, move_L1,move_RR, move_R1, move_R2]]
    else:
        g=1
        previous_move=" "
        previous_move_name=""
        possibility = [[move_U1, move_U2, move_UU], [move_DD, move_D1, move_D2], [move_B1, move_B2, move_BB],
                       [move_FF, move_F1, move_F2],
                       [move_LL, move_L2, move_L1], [move_RR, move_R1, move_R2]]
    possibility= [sublist for sublist in possibility if previous_move not in sublist]
    possibility= [element for sublists in possibility for element in sublists]
    # Appliquer les mouvements de move_set1
    for x in range(18):
        if  move_set[x] in possibility:
            reset=cube.copy()
            move_set[x](cube)  # Appliquer le mouvement F1, F2, etc.
            # Calculer la fonction de coût f = g + h (heuristique)


            # Vérifier si on reste sous le seuil
            current_cube_as_string=bytes(cube)
            if current_cube_as_string not in before:

                h= heuristic(current_cube_as_string)

                f = g + h

                if f <= threshold:
                    if open_state:
                        previous_moves = open_state[0][4]
                        new_moves = previous_moves + [move_set[x].__name__]
                    else:
                        new_moves = [move_set[x].__name__]
                    pre_open.append((move_set[x], f, current_cube_as_string, g, new_moves.copy()))

                before.add(current_cube_as_string)
                    # Annuler le mouvement
            cube=reset.copy()
    # Appliquer les mouvements de move_set2
    pre_open.sort(key=lambda x: (x[1]))
"""zone to scramble the cube with some moves"""
move_D2(cube)
move_U1(cube)
move_B1(cube)
print_cube(cube)
start= cube.copy()
list_time= 0
#lalgo trouve la solution avec f1/F2 / D1/ D2 / R1/R2/L1/L2/ quand on utilise quatre move
"""algorythm"""
print("-----ida star-----")
while continue_algo:
    global threshold
    before.clear()
    open_state.clear()

    iteration += 1
    # we handle the case for the first iteration
    if iteration == 1:
        threshold= heuristic(bytes(cube))
        print("iteration # 1","threshold:",threshold)
        get_f_scores(threshold,cube,pre_open,open_state,face_classification)
        open_state.extendleft(pre_open)
        #we check each node under the threshold
        while open_state:
            list_time +=1

            cube =bytearray(open_state[0][2])
            # we check if this is the solution and if yes we break the loop
            if cube == goal:
                print("solution:", open_state[0][4])
                continue_algo = 0
                break

            # if its not we explore the children and we remove the one that we just visited to avoid repetition
            get_f_scores(threshold, cube, pre_open,open_state,face_classification)
            open_state.popleft()
            open_state.extendleft(pre_open)
        #in this case if open state is empty the line of code wont just be readed and it will go to the next iteration


    #now we handle the case for the other iterationw
    else:
        cube= start.copy()
        #now we get the new threshold
        start_time = time.time()
        threshold = threshold+0.25
        print("iteration #",iteration,"threshold:",threshold,)
        #now we can get the new openstate
        get_f_scores(threshold,cube,pre_open,open_state,face_classification)
        open_state.extendleft(pre_open)
        #now we can start the loop for the algo
        while open_state:
            list_time += 1
            cube=bytearray(open_state[0][2])
            # we check if this is the solution and if yes we break the loop
            if bytes(cube) == bytes(goal):
                continue_algo = 0
                print("solution:", open_state[0][4])

                break

            # if its not we explore the children and we remove the one that we just visited to avoid repetition
            get_f_scores(threshold, cube, pre_open,open_state,face_classification)
            open_state.popleft()
            open_state.extendleft(pre_open)

            # in this case if open state is empty the line of code wont just be readed and it will go to the next it    eration

        continue
print("si tu vois cela cest que sa marche!!!!!")
print("---iteration time: %s seconds ---" % (time.time() - start_time))
print("---global time: %s seconds ---" % (time.time() - global_start))
print(fois)
print("khk",list_time)
print(heuristic.cache_info())
"""p 23306035
1623087
khk 1623070"""
