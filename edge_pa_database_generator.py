import copy
from collections import deque
import time
import numpy as np

P=0
def string_to_2d_list(string):
    global P
    P+=1
    words = string.split()  # Split the string into words
    return [words[i:i+9] for i in range(0, len(words), 9)]
def list_to_string(two_d_list):
    global P
    P+=1
    return " ".join([item for sublist in two_d_list for item in sublist])
"""import the tools that I need """
cube =np.array([
    ['W'] * 9, ['R'] * 9, ['B'] * 9, ['O'] * 9, ['G'] * 9, ['Y'] * 9])

goal = np.array([
    ['W']*9, ['R']*9, ['B']*9, ['O']*9, ['G']*9, ['Y']*9
])
def rotate_face_clockwise(face,face_index):
    face = np.array(face)
    cube[face_index]=np.rot90(face.reshape(3, 3), 1).flatten()
# Rotation d'une face dans le sens anti-horaire
def rotate_face_anticlockwise(face,face_index):
    face = np.array(face)
    cube[face_index]=np.rot90(face.reshape(3, 3), 3).flatten()

# movement up sens horaire
def move_U1() :
    initial_segment= cube[1][0:3]
    cube[1][0:3] = cube[2][0:3]
    cube[2][0:3] = cube[3][0:3]
    cube[3][0:3] = cube[4][0:3]
    cube[4][0:3] =initial_segment
    rotate_face_clockwise(cube[0],0)
    return cube

# mouvement up sens anti horaire
def move_U2() :
    initial_segment = cube[4][0:3]       # pour comprendre le code il faut consisdere
    cube[4][0:3] = cube[3][0:3]          # que le haut du cube cest la face blanche
    cube[3][0:3] = cube[2][0:3]           # et la partie en face de nous cest la face verte
    cube[2][0:3] = cube[1][0:3]
    cube[1][0:3] = initial_segment
    rotate_face_anticlockwise(cube[0],0)
def move_D1():
    initial_segment = cube[3][6:9]
    cube[3][6:9] = cube[2][6:9]
    cube[2][6:9] = cube[1][6:9]
    cube[1][6:9] = cube[4][6:9]
    cube[4][6:9] = initial_segment
    rotate_face_clockwise(cube[5],5)  # Rotation horaire
    return cube
def move_D2():
    initial_segment = cube[2][6:9]
    cube[2][6:9] = cube[3][6:9]
    cube[3][6:9] = cube[4][6:9]
    cube[4][6:9] = cube[1][6:9]
    cube[1][6:9] = initial_segment
    rotate_face_anticlockwise(cube[5],5)  # Rotation horaire pour annuler l'effet de D1
    return cube
# mouvement front sens horaire
def move_F1():
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[0][6:9]
    cube[0][6:9] = cube[3][2:9][::-3]
    cube[3][2:9:3] = cube[5][0:3]
    cube[5][0:3] = initial_segment[::-1]
    rotate_face_clockwise(cube[4],4)
    return cube
# mouvement front sens anti horaire
def move_F2():
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[5][0:3][::-1]
    cube[5][0:3] = cube[3][2:9][::3]
    cube[3][2:9:3] = cube[0][6:9][::-1]
    cube[0][6:9] = initial_segment
    rotate_face_anticlockwise(cube[4],4)
    return cube
def move_B1():
    initial_segment = cube[3][::3]
    cube[3][::3] = cube[0][0:3][::-1]
    cube[0][0:3] = cube[1][2:9][::3]
    cube[1][2:9:3]= cube[5][6:9][::-1]
    cube[5][6:9] = initial_segment[::1]
    rotate_face_clockwise(cube[2],2)
    return cube
def move_B2():
    initial_segment = cube[1][2:9][::3]
    cube[1][2:9:3] = cube[0][0:3]
    cube[0][0:3] = cube[3][::3][::-1]
    cube[3][::3] = cube[5][6:9]
    cube[5][6:9] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[2],2)
    return cube
def move_R1():
    initial_segment =  cube[0][2:9:3]
    cube[0][2:9:3]=  cube[4][2:9:3]
    cube[4][2:9:3]= cube[5][2:9:3]
    cube[5][2:9:3]= cube[2][::3][::-1]
    cube[2][::3]= initial_segment[::-1]
    rotate_face_clockwise(cube[1],1)

    return cube
def move_R2():
    initial_segment = cube[2][::3]
    cube[2][::3]= cube[5][2:9:3][::-1]
    cube[5][2:9:3] = cube[4][2:9:3]
    cube[4][2:9:3] = cube[0][2:9:3]
    cube[0][2:9:3] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[1],1)
    return cube
def move_L1():
    initial_segment =  cube[5][::3]
    cube[5][::3]= cube[4][::3]
    cube[4][::3]= cube[0][::3]
    cube[0][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3]= initial_segment[::-1]
    rotate_face_clockwise(cube[3],3)
    return cube
def move_L2():
    initial_segment = cube[4][::3]
    cube[4][::3] = cube[5][::3]
    cube[5][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3] = cube[0][::3][::-1]
    cube[0][::3] = initial_segment
    rotate_face_anticlockwise(cube[3],3)
def move_UU():
    move_U1()
    move_U1()
def move_DD():
    move_D1()
    move_D1()
def move_RR():
    move_R1()
    move_R1()
def move_LL():
    move_L1()
    move_L1()
def move_BB():
    move_B1()
    move_B1()
def move_FF():
    move_F1()
    move_F1()
def switch_corner(cube3D,cx,cy,cz,x,y,z):
    store= cube3D[cx][cy][cz]
    cube3D[cx][cy][cz] = cube3D[x][y][z]
    cube3D[x][y][z]= store

def treed_to_2d(cube3D):
    d_cube = [[cube3D[0][0][0][0], cube3D[0][1][0][0], cube3D[0][2][0][0], cube3D[1][0][0][0], cube3D[1][1][0][0],
               cube3D[1][2][0][0], cube3D[2][0][0][0], cube3D[2][1][0][0], cube3D[2][2][0][0]],
              [cube3D[2][2][0][2], cube3D[1][2][0][1], cube3D[0][2][0][1], cube3D[2][2][1][1], cube3D[1][2][1][0],
               cube3D[0][2][1][0], cube3D[2][2][2][1], cube3D[1][2][2][0], cube3D[0][2][2][0]],
              [cube3D[0][2][0][2], cube3D[0][1][0][1], cube3D[0][0][0][2], cube3D[0][2][1][1], cube3D[0][1][1][0],
               cube3D[0][0][1][1], cube3D[0][2][2][1], cube3D[0][1][2][0], cube3D[0][0][2][1]],
              [cube3D[0][0][0][1], cube3D[1][0][0][1], cube3D[2][0][0][2], cube3D[0][0][1][0], cube3D[1][0][1][0],
               cube3D[2][0][1][1], cube3D[0][0][2][0], cube3D[1][0][2][0], cube3D[2][0][2][1]],
              [cube3D[2][0][0][1], cube3D[2][1][0][1], cube3D[2][2][0][1], cube3D[2][0][1][0], cube3D[2][1][1][0],
               cube3D[2][2][1][0], cube3D[2][0][2][0], cube3D[2][1][2][0], cube3D[2][2][2][0]],
              [cube3D[2][0][2][2], cube3D[2][1][2][1], cube3D[2][2][2][2], cube3D[1][0][2][1], cube3D[1][1][2][0],
               cube3D[1][2][2][1], cube3D[0][0][2][2], cube3D[0][1][2][1], cube3D[0][2][2][2]]
              ]
    return d_cube
def convert_to_3D_format(cube):

    converted_cube = [
        [[ [cube[0][0], cube[3][0], cube[2][2]], [cube[3][3], cube[2][5]], [cube[3][6], cube[2][8], cube[5][6]] ],
         [ [cube[0][1], cube[2][1]], [cube[2][4],], [cube[2][7], cube[5][7]] ],
         [ [cube[0][2], cube[1][2], cube[2][0]], [cube[1][5], cube[2][3]], [cube[1][8], cube[2][6], cube[5][8]] ]],

        [[ [cube[0][3], cube[3][1]], [cube[3][4],], [cube[3][7], cube[5][3]] ],
         [ [cube[0][4],], [None,],[cube[5][4],] ],
         [ [cube[0][5], cube[1][1]], [cube[1][4]], [cube[1][7], cube[5][5]] ]],

        [[ [cube[0][6], cube[4][0], cube[3][2]], [cube[4][3], cube[3][5]], [cube[4][6], cube[3][8], cube[5][0]] ],
         [ [cube[0][7], cube[4][1]], [cube[4][4],], [cube[4][7], cube[5][1]]],
        [ [cube[0][8], cube[4][2], cube[1][0]], [cube[4][5], cube[1][3]], [cube[4][8], cube[1][6], cube[5][2]] ]]
    ]
    return converted_cube

"""useful variables"""

pruned = []
open_state = deque()
pre_open = []
edge_dic= dict()
move_set1 = [move_U1, move_R1, move_B1, move_L1,move_D1,move_UU, move_DD, move_LL, move_RR, move_FF, move_BB,move_F1]
move_set1_undo= [move_U2, move_R2, move_B2, move_L2, move_D2,move_UU, move_DD, move_LL, move_RR, move_FF, move_BB,move_F2]
move_set2 = [move_U2, move_R2, move_B2, move_L2, move_F2, move_D2]
move_set2_undo =[move_U1, move_R1, move_B1, move_L1, move_F1,move_D1]
continue_algo = True
start_time = time.time()

"""functions"""

# calculate the heuristic for the current state of cube
def flip_edge(cube3D,x,y,z):
    store= cube3D[x][y][z][1]
    cube3D[x][y][z][1]=cube3D[x][y][z][0]
    cube3D[x][y][z][0]=store


def turn_clockwise_corner(cube3D,x,y,z):
    store= cube3D[x][y][z][0]
    cube3D[x][y][z][0]=cube3D[x][y][z][2]
    cube3D[x][y][z][2]=cube3D[x][y][z][1]
    cube3D[x][y][z][1]=store
def turn_anti_clockwise_core(cube3D,x,y,z):
    store= cube3D[x][y][z][0]
    cube3D[x][y][z][0]=cube3D[x][y][z][1]
    cube3D[x][y][z][1]= cube3D[x][y][z][2]
    cube3D[x][y][z][2]=store
def noturn(cube3D,x,y,z):
    pass
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
    pre_open.clear()
    face_classification= {"move_B1":1,"move_B2":1,"move_BB":1,"move_U1":2,"move_U2":2,"move_UU":2,"move_D1":1,"move_D2":1,
                          "move_DD":1,"move_F1":2,"move_F2":2,"move_FF":2,"move_L1":1,"move_L2":1,"move_LL":1,"move_R1":2,
                          "move_R2":2,"move_RR":2}
    if open_state:
        g= open_state[0][1]+1
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

    # Appliquer les mouvements de move_set1
    for x in range(12):
        if  any(move_set1[x] in sublist for sublist in possibility) :
            move_set1[x]()  # Appliquer le mouvement F1, F2, etc.
            # Vérifier si on reste sous le seuil
            current_cube_as_string=list_to_string(cube)
            if g <= threshold:
                    pre_open.append([move_set1[x],g,current_cube_as_string])
            move_set1_undo[x]()

    # Appliquer les mouvements de move_set2
    for x in range(6):
        if  any(move_set2[x] in sublist for sublist in possibility) :
            # Appliquer le mouvement
            move_set2[x]()
            # Vérifier si on reste sous le seuil
            current_cube_as_string=list_to_string(cube)
            if g <= threshold:
                pre_open.append([move_set2[x], g,current_cube_as_string])
            # Annuler le mouvement
            move_set2_undo[x]()
list_of_edge_rotation=[noturn,flip_edge]
edge_coordinate_list=((0,0,1),(0,1,0),(0,1,2),(0,2,1),
                       (1,0,0),(1,0,2),(1,2,0),(1,2,2),
                       (2,0,1),(2,1,0),(2,1,2),(2,2,1))
"""looking for the solution of one cubie """
original_cube = np.copy(cube)  # Place this before the loop
process_completion_percentage=0
for coordinate in edge_coordinate_list:
    process_completion_percentage+=1/12
    print(f"process completion level: {process_completion_percentage*100} %")
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if (x + y + z) % 2 == 1 and (x,y,z)!=(1,1,1):
                    # switching to a new cubie each time
                    threshold = 0
                    open_state.clear()
                    cube=np.copy(original_cube)  # Reset the cube for each corner
                    cube3D = convert_to_3D_format(cube)
                    switch_corner(cube3D, coordinate[0], coordinate[1], coordinate[2], x, y, z)
                    # loop to change corner orientation at a position
                    for function in list_of_edge_rotation:

                        start = copy.deepcopy(cube3D)
                        function(start, x, y, z)
                        continue_algo = 1
                        # calculating how far a permutation of a cubie is away from solved
                        while continue_algo:

                            cube = treed_to_2d(start)
                            if convert_to_3D_format(cube)[coordinate[0]][coordinate[1]][coordinate[2]] == \
                                    convert_to_3D_format(goal)[coordinate[0]][coordinate[1]][coordinate[2]]:
                                edge_dic[(tuple(start[x][y][z]), x, y, z)] = 0

                                break
                            # now we get the new threshold
                            threshold += 1
                            # now we can get the new openstate
                            get_f_scores(threshold)

                            open_state.extendleft(pre_open)

                            # now we can start the loop for the algo
                            while open_state:
                                cube = string_to_2d_list(open_state[0][2])
                                # we check if this is the solution and if yes we break the loop
                                if convert_to_3D_format(cube)[coordinate[0]][coordinate[1]][coordinate[2]] == \
                                        convert_to_3D_format(goal)[coordinate[0]][coordinate[1]][coordinate[2]]:
                                    edge_dic[(tuple(start[x][y][z]), x, y, z)] = open_state[0][1]

                                    continue_algo = 0

                                    break
                                get_f_scores(threshold)
                                open_state.popleft()
                                open_state.extendleft(pre_open)

                                # in this case if open state is empty the line of code wont just be readed and it will go to the next it    eration
                            threshold += 1
                            continue

print("---------------------------------------------------------------------------------------------------------------------------------")
print("bellow is the database with the solution to every single edge position and orientation you can copy paste it in a file now")
print(edge_dic)
print("number of element in the data base :",edge_dic.__len__())
print("---------------------------------------------------------------------------------------------------------------------------------")

