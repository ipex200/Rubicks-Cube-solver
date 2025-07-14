from collections import deque
from heuristic_dictionaries import *
import time
from itertools import chain

cube =  [
        ['W', 'W', 'W',
         'W', 'W', 'W',
         'W', 'W', 'W'],  # Face blanche

        ['R', 'R', 'R',
         'R', 'R', 'R',
         'R', 'R', 'R'],  # Face rouge

        ['B', 'B', 'B',
         'B', 'B', 'B',
         'B', 'B', 'B'],  # Face bleue

        ['O', 'O', 'O',
         'O', 'O', 'O',
         'O', 'O', 'O'],  # Face orange

        ['G', 'G', 'G',
         'G', 'G', 'G',
         'G', 'G', 'G'],  # Face verte

        ['Y', 'Y', 'Y',
         'Y', 'Y', 'Y',
         'Y', 'Y', 'Y']]  # Face jaune

goal =  [
        ['W', 'W', 'W',
         'W', 'W', 'W',
         'W', 'W', 'W'],  # Face blanche

        ['R', 'R', 'R',
         'R', 'R', 'R',
         'R', 'R', 'R'],  # Face rouge

        ['B', 'B', 'B',
         'B', 'B', 'B',
         'B', 'B', 'B'],  # Face bleue

        ['O', 'O', 'O',
         'O', 'O', 'O',
         'O', 'O', 'O'],  # Face orange

        ['G', 'G', 'G',
         'G', 'G', 'G',
         'G', 'G', 'G'],  # Face verte

        ['Y', 'Y', 'Y',
         'Y', 'Y', 'Y',
         'Y', 'Y', 'Y']]  # Face jaune
def string_to_2d_list(string):
    global P
    P+=1
    words = string.split()  # Split the string into words
    return [words[i:i+9] for i in range(0, len(words), 9)]
def list_to_string(two_d_list):
    global P
    P+=1
    return " ".join(item for sublist in two_d_list for item in sublist)
def rotate_face_clockwise(face,face_idx):
    cube[face_idx]= [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

# Rotation d'une face dans le sens anti-horaire
def rotate_face_anticlockwise(face,face_idx):
    cube[face_idx]=  [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]
def rotate_face_180_degre(face_idx):
    cube[face_idx]= cube[face_idx][::-1]
def move_U1(cube) :
    initial_segment= cube[1][0:3]
    cube[1][0:3] = cube[2][0:3]
    cube[2][0:3] = cube[3][0:3]
    cube[3][0:3] = cube[4][0:3]
    cube[4][0:3] =initial_segment
    rotate_face_clockwise(cube[0],0)
    return cube

# mouvement up sens anti horaire
def move_U2(cube) :
    initial_segment = cube[4][0:3]       # pour comprendre le code il faut consisdere
    cube[4][0:3] = cube[3][0:3]          # que le haut du cube cest la face blanche
    cube[3][0:3] = cube[2][0:3]           # et la partie en face de nous cest la face verte
    cube[2][0:3] = cube[1][0:3]
    cube[1][0:3] = initial_segment
    rotate_face_anticlockwise(cube[0],0)
def move_D1(cube):
    initial_segment = cube[3][6:9]
    cube[3][6:9] = cube[2][6:9]
    cube[2][6:9] = cube[1][6:9]
    cube[1][6:9] = cube[4][6:9]
    cube[4][6:9] = initial_segment
    rotate_face_clockwise(cube[5],5)  # Rotation horaire
    return cube
def move_D2(cube):
    initial_segment = cube[2][6:9]
    cube[2][6:9] = cube[3][6:9]
    cube[3][6:9] = cube[4][6:9]
    cube[4][6:9] = cube[1][6:9]
    cube[1][6:9] = initial_segment
    rotate_face_anticlockwise(cube[5],5)  # Rotation horaire pour annuler l'effet de D1
    return cube
# mouvement front sens horaire
def move_F1(cube):
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[0][6:9]
    cube[0][6:9] = cube[3][2:9][::-3]
    cube[3][2:9:3] = cube[5][0:3]
    cube[5][0:3] = initial_segment[::-1]
    rotate_face_clockwise(cube[4],4)
    return cube
# mouvement front sens anti horaire
def move_F2(cube):
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[5][0:3][::-1]
    cube[5][0:3] = cube[3][2:9][::3]
    cube[3][2:9:3] = cube[0][6:9][::-1]
    cube[0][6:9] = initial_segment
    rotate_face_anticlockwise(cube[4],4)
    return cube
def move_B1(cube):
    initial_segment = cube[3][::3]
    cube[3][::3] = cube[0][0:3][::-1]
    cube[0][0:3] = cube[1][2:9][::3]
    cube[1][2:9:3]= cube[5][6:9][::-1]
    cube[5][6:9] = initial_segment[::1]
    rotate_face_clockwise(cube[2],2)
    return cube
def move_B2(cube):
    initial_segment = cube[1][2:9][::3]
    cube[1][2:9:3] = cube[0][0:3]
    cube[0][0:3] = cube[3][::3][::-1]
    cube[3][::3] = cube[5][6:9]
    cube[5][6:9] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[2],2)
    return cube
def move_R1(cube):
    initial_segment =  cube[0][2:9:3]
    cube[0][2:9:3]=  cube[4][2:9:3]
    cube[4][2:9:3]= cube[5][2:9:3]
    cube[5][2:9:3]= cube[2][::3][::-1]
    cube[2][::3]= initial_segment[::-1]
    rotate_face_clockwise(cube[1],1)

    return cube
def move_R2(cube):
    initial_segment = cube[2][::3]
    cube[2][::3]= cube[5][2:9:3][::-1]
    cube[5][2:9:3] = cube[4][2:9:3]
    cube[4][2:9:3] = cube[0][2:9:3]
    cube[0][2:9:3] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[1],1)
    return cube
def move_L1(cube):
    initial_segment =  cube[5][::3]
    cube[5][::3]= cube[4][::3]
    cube[4][::3]= cube[0][::3]
    cube[0][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3]= initial_segment[::-1]
    rotate_face_clockwise(cube[3],3)
    return cube
def move_L2(cube):
    initial_segment = cube[4][::3]
    cube[4][::3] = cube[5][::3]
    cube[5][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3] = cube[0][::3][::-1]
    cube[0][::3] = initial_segment
    rotate_face_anticlockwise(cube[3],3)
def move_UU(cube):
    cube[1][:3],cube[3][:3]= cube[3][:3],cube[1][:3]
    cube[2][:3], cube[4][:3] = cube[4][:3], cube[2][:3]
    rotate_face_180_degre(face_idx=0)
def move_DD(cube):
    cube[1][-3:], cube[3][-3:] = cube[3][-3:], cube[1][-3:]
    cube[2][-3:], cube[4][-3:] = cube[4][-3:], cube[2][-3:]
    rotate_face_180_degre(face_idx=5)
def move_RR(cube):
    cube[0][2:9:3],  cube[5][2:9:3] = cube[5][2:9:3],  cube[0][2:9:3]
    cube[2][::3],  cube[4][2:9:3] = cube[4][2:9:3][::-1], cube[2][::3][::-1]
    rotate_face_180_degre(face_idx=1)
def move_LL(cube):#needs correction
    cube[0][::3], cube[5][::3] = cube[5][::3], cube[0][::3]
    cube[2][2:9:3], cube[4][::3] = cube[4][::3][::-1], cube[2][2:9:3][::-1]
    rotate_face_180_degre(face_idx=3)
def move_BB(cube):
    cube[0][:3],cube[5][-3:]=cube[5][-3:][::-1],cube[0][:3][::-1]
    cube[1][2:9:3],cube[3][::3]=cube[3][::3][::-1],cube[1][2:9:3][::-1]
    rotate_face_180_degre(2)
def move_FF(cube):
    cube[0][-3:],cube[5][:3]= cube[5][:3][::-1],cube[0][-3:][::-1]
    cube[3][2:9:3],cube[1][::3]=cube[1][::3][::-1],cube[3][2:9:3][::-1]
    rotate_face_180_degre(face_idx=4)
def convert_to_3D_format(cube):
    converted_cube = [
        [[ (cube[0][0], cube[3][0], cube[2][2]), (cube[3][3], cube[2][5]), (cube[3][6], cube[2][8], cube[5][6]) ],
         [ (cube[0][1], cube[2][1]), (cube[2][4],), (cube[2][7], cube[5][7]) ],
         [ (cube[0][2], cube[1][2], cube[2][0]), (cube[1][5], cube[2][3]), (cube[1][8], cube[2][6], cube[5][8]) ]],

        [[ (cube[0][3], cube[3][1]), (cube[3][4],), (cube[3][7], cube[5][3]) ],
         [ (cube[0][4],), (None,),(cube[5][4],) ],
         [ (cube[0][5], cube[1][1]), (cube[1][4]), (cube[1][7], cube[5][5]) ]],

        [[ (cube[0][6], cube[4][0], cube[3][2]), (cube[4][3], cube[3][5]), (cube[4][6], cube[3][8], cube[5][0]) ],
         [ (cube[0][7], cube[4][1]), (cube[4][4],), (cube[4][7], cube[5][1])],
         [ (cube[0][8], cube[4][2], cube[1][0]), (cube[4][5], cube[1][3]), (cube[4][8], cube[1][6], cube[5][2]) ]]
    ]
    return converted_cube


"""useful variables"""
P=0
open_state = deque()
pre_open = []
iteration = 0
calculated_heuristiques= {}
move_set1 = [move_U1, move_R1, move_B1, move_L1,move_D1,move_UU, move_DD, move_LL, move_RR, move_FF, move_BB,move_F1]
move_set1_undo= [move_U2, move_R2, move_B2, move_L2, move_D2,move_UU, move_DD, move_LL, move_RR, move_FF, move_BB,move_F2]
move_set2 = [move_U2, move_R2, move_B2, move_L2, move_F2, move_D2]
move_set2_undo =[move_U1, move_R1, move_B1, move_L1, move_F1,move_D1]
continue_algo = True
continue_iteration = True
continue_search= True
before=set()
global_start = time.time()
start_time = time.time()
"""functions"""

# calculate the heuristic for the current state of cube
def heuristic(current):
    current_cube= convert_to_3D_format(current)
    total_distance_edge=0
    total_distance_corner=0
    # Iterate over cubi all positions in the 3x3x3 cube
    for a in edge_coordinate_list:
        x,y,z =a[0],a[1],a[2]
        cubie= current_cube[x][y][z]
        total_distance_edge+= edge_data_base[(tuple(cubie),x,y,z)]
    for a in corner_coordinate_list:
        x,y,z =a[0],a[1],a[2]
        cubie= current_cube[x][y][z]
        total_distance_corner+= corner_data_base[(tuple(cubie),x,y,z)]
    return max(total_distance_edge/4,total_distance_corner)
#function that allows me to print the cube in a bette way
def print_cube(cube):
    for face in cube:
        for x in range(0,9,3):
            print(face[x:x+3])
        print("")
# calculate the f_score and classify them  for every possible child of the current cube
fois=0
def get_f_scores(threshold):
    global start_time
    global fois
    fois+=1
    global  pre_open
    global pruned
    pre_open.clear()
    face_classification= {"move_B1":1,"move_B2":1,"move_BB":1,"move_U1":2,"move_U2":2,"move_UU":2,"move_D1":1,"move_D2":1,
                          "move_DD":1,"move_F1":2,"move_F2":2,"move_FF":2,"move_L1":1,"move_L2":1,"move_LL":1,"move_R1":2,
                          "move_R2":2,"move_RR":2}
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
    for x in range(12):
        if  move_set1[x] in possibility:
            move_set1[x](cube)  # Appliquer le mouvement F1, F2, etc.
            # Calculer la fonction de coût f = g + h (heuristique)


            # Vérifier si on reste sous le seuil
            current_cube_as_string=list_to_string(cube)
            if current_cube_as_string not in before:

                if current_cube_as_string not in calculated_heuristiques:
                    h = heuristic(cube)
                    calculated_heuristiques[current_cube_as_string]= h
                else:
                    h= calculated_heuristiques[current_cube_as_string]

                f = g + h

                if f <= threshold:
                    pre_open.append((move_set1[x],f,current_cube_as_string,g))
                before.add(current_cube_as_string)
                    # Annuler le mouvement
            move_set1_undo[x](cube)

    # Appliquer les mouvements de move_set2
    for x in range(6):
        if  move_set2[x] in possibility:
            # Appliquer le mouvement
            move_set2[x](cube)
            # Calculer la fonction de coût f = g + h (heuristique)

            # Vérifier si on reste sous le seuil
            current_cube_as_string=list_to_string(cube)
            if current_cube_as_string not in before:

                if current_cube_as_string not in calculated_heuristiques:
                    h = heuristic(cube)
                    calculated_heuristiques[current_cube_as_string] = h
                else:
                    h = calculated_heuristiques[current_cube_as_string]

                f = g + h

                if f <= threshold:
                    pre_open.append((move_set2[x], f,current_cube_as_string,g))
                # Annuler le mouvement
                before.add(current_cube_as_string)
            move_set2_undo[x](cube)
    # Trier les résultats pour garder les meilleurs en fonction de f

    pre_open.sort(key=lambda x: (x[1]))
"""zone to scramble the cube with some moves"""
move_D2(cube)
move_U1(cube)
move_B1(cube)
move_L2(cube)
move_R1(cube)
move_F2(cube)
move_RR(cube)
move_L1(cube)
move_D2(cube)
print_cube(cube)
start= list_to_string(cube)
list_time= 0
#lalgo trouve la solution avec f1/F2 / D1/ D2 / R1/R2/L1/L2/ quand on utilise quatre move
"""algorythm"""
while continue_algo:
    global threshold
    before.clear()
    open_state.clear()

    iteration += 1
    # we handle the case for the first iteration
    if iteration == 1:
        threshold= heuristic(cube)

        get_f_scores(threshold)
        open_state.extendleft(pre_open)
        #we check each node under the threshold
        while open_state:
            list_time  +=1

            cube = string_to_2d_list(open_state[0][3])
            # we check if this is the solution and if yes we break the loop
            if cube == goal:
                continue_algo = 0
                break

            # if its not we explore the children and we remove the one that we just visited to avoid repetition
            get_f_scores(threshold)
            open_state.popleft()
            open_state.extendleft(pre_open)
        #in this case if open state is empty the line of code wont just be readed and it will go to the next iteration

        continue
    #now we handle the case for the other iterationw
    else:
        cube= string_to_2d_list(start)
        #now we get the new threshold
        start_time = time.time()
        print("---iteration time: %s seconds ---" % (time.time() - start_time))

        threshold = threshold+0.25
        print("iteration #",iteration,"threshold:",threshold,)
        #now we can get the new openstate
        get_f_scores(threshold)
        open_state.extendleft(pre_open)
        #now we can start the loop for the algo
        while open_state:
            list_time  +=1
            cube = string_to_2d_list(open_state[0][2])
            # we check if this is the solution and if yes we break the loop
            if cube == goal:

                continue_algo = 0
                break

            # if its not we explore the children and we remove the one that we just visited to avoid repetition
            get_f_scores(threshold)
            open_state.popleft()
            open_state.extendleft(pre_open)

            # in this case if open state is empty the line of code wont just be readed and it will go to the next it    eration

        continue
print_cube(cube)
print("si tu vois cela cest que sa marche!!!!!")
print("---iteration time: %s seconds ---" % (time.time() - start_time))
print("---global time: %s seconds ---" % (time.time() - global_start))
print("p",P)
print(fois)
print("khk",list_time)
"""p 23306035
1623087
khk 1623070"""