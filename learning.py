
def string_to_2d_list(string):
    words = string.split()  # Split the string into words
    return [words[i:i+9] for i in range(0, len(words), 9)]
def list_to_string(two_d_list):
    return " ".join([item for sublist in two_d_list for item in sublist])

"""import the tools that I need """
import time
start_time = time.time()

cube = [
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
def rotate_face_clockwise(face):
    cube[cube.index(face)]= [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

# Rotation d'une face dans le sens anti-horaire
def rotate_face_anticlockwise(face):
    cube[cube.index(face)]=  [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]

# movement up sens horaire
def move_U1() :
    initial_segment= cube[1][0:3]
    cube[1][0:3] = cube[2][0:3]
    cube[2][0:3] = cube[3][0:3]
    cube[3][0:3] = cube[4][0:3]
    cube[4][0:3] =initial_segment
    rotate_face_clockwise(cube[0])
    return cube

# mouvement up sens anti horaire
def move_U2() :
    initial_segment = cube[4][0:3]       # pour comprendre le code il faut consisdere
    cube[4][0:3] = cube[3][0:3]          # que le haut du cube cest la face blanche
    cube[3][0:3] = cube[2][0:3]           # et la partie en face de nous cest la face verte
    cube[2][0:3] = cube[1][0:3]
    cube[1][0:3] = initial_segment
    rotate_face_anticlockwise(cube[0])
def move_D1():
    initial_segment = cube[3][6:9]
    cube[3][6:9] = cube[2][6:9]
    cube[2][6:9] = cube[1][6:9]
    cube[1][6:9] = cube[4][6:9]
    cube[4][6:9] = initial_segment
    rotate_face_clockwise(cube[5])  # Rotation horaire
    return cube
def move_D2():
    initial_segment = cube[2][6:9]
    cube[2][6:9] = cube[3][6:9]
    cube[3][6:9] = cube[4][6:9]
    cube[4][6:9] = cube[1][6:9]
    cube[1][6:9] = initial_segment
    rotate_face_anticlockwise(cube[5])  # Rotation horaire pour annuler l'effet de D1
    return cube
# mouvement front sens horaire
def move_F1():
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[0][6:9]
    cube[0][6:9] = cube[3][2:9][::-3]
    cube[3][2:9:3] = cube[5][0:3]
    cube[5][0:3] = initial_segment[::-1]
    rotate_face_clockwise(cube[4])
    return cube
# mouvement front sens anti horaire
def move_F2():
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[5][0:3][::-1]
    cube[5][0:3] = cube[3][2:9][::3]
    cube[3][2:9:3] = cube[0][6:9][::-1]
    cube[0][6:9] = initial_segment
    rotate_face_anticlockwise(cube[4])
    return cube
def move_B1():
    initial_segment = cube[3][::3]
    cube[3][::3] = cube[0][0:3][::-1]
    cube[0][0:3] = cube[1][2:9][::3]
    cube[1][2:9:3]= cube[5][6:9][::-1]
    cube[5][6:9] = initial_segment[::1]
    rotate_face_clockwise(cube[2])
    return cube
def move_B2():
    initial_segment = cube[1][2:9][::3]
    cube[1][2:9:3] = cube[0][0:3]
    cube[0][0:3] = cube[3][::3][::-1]
    cube[3][::3] = cube[5][6:9]
    cube[5][6:9] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[2])
    return cube
def move_R1():
    initial_segment =  cube[0][2:9:3]
    cube[0][2:9:3]=  cube[4][2:9:3]
    cube[4][2:9:3]= cube[5][2:9:3]
    cube[5][2:9:3]= cube[2][::3][::-1]
    cube[2][::3]= initial_segment[::-1]
    rotate_face_clockwise(cube[1])

    return cube
def move_R2():
    initial_segment = cube[2][::3]
    cube[2][::3]= cube[5][2:9:3][::-1]
    cube[5][2:9:3] = cube[4][2:9:3]
    cube[4][2:9:3] = cube[0][2:9:3]
    cube[0][2:9:3] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[1])
    return cube
def move_L1():
    initial_segment =  cube[5][::3]
    cube[5][::3]= cube[4][::3]
    cube[4][::3]= cube[0][::3]
    cube[0][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3]= initial_segment[::-1]
    rotate_face_clockwise(cube[3])
    return cube
def move_L2():
    initial_segment = cube[4][::3]
    cube[4][::3] = cube[5][::3]
    cube[5][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3] = cube[0][::3][::-1]
    cube[0][::3] = initial_segment
    rotate_face_anticlockwise(cube[3])
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
def convert_to_3D_format(cube):
    converted_cube = [
        [[ [cube[0][0], cube[3][0], cube[2][2]], [cube[3][3], cube[2][5]], [cube[3][6], cube[2][8], cube[5][6]] ],
         [ [cube[0][1], cube[2][1]], [cube[2][4]], [cube[2][7], cube[5][7]] ],
         [ [cube[0][2], cube[1][2], cube[2][0]], [cube[1][5], cube[2][3]], [cube[1][8], cube[2][6], cube[5][8]] ]],

        [[ [cube[0][3], cube[3][1]], [cube[3][4]], [cube[3][7], cube[5][3]] ],
         [ [cube[0][4]], [None],[cube[5][4]] ],
         [ [cube[0][5], cube[1][1]], [cube[1][4]], [cube[1][7], cube[5][5]] ]],

        [[ [cube[0][6], cube[4][0], cube[3][2]], [cube[4][3], cube[3][5]], [cube[4][6], cube[3][8], cube[5][0]] ],
         [ [cube[0][7], cube[4][1]], [cube[4][4]], [cube[4][7], cube[5][1]] ],
         [ [cube[0][8], cube[4][2], cube[1][0]], [cube[4][5], cube[1][3]], [cube[4][8], cube[1][6], cube[5][2]] ]]
    ]
    return converted_cube


"""useful variables"""

pruned = []
open_state = []
pre_open = []
current = []
path = []
iteration = 0

move_set1 = [move_U1, move_R1, move_B1, move_L1,move_D1,move_UU, move_DD, move_LL, move_RR, move_FF, move_BB,move_F1]
move_set1_undo= [move_U2, move_R2, move_B2, move_L2, move_D2,move_UU, move_DD, move_LL, move_RR, move_FF, move_BB,move_F2]
move_set2 = [move_U2, move_R2, move_B2, move_L2, move_F2, move_D2]
move_set2_undo =[move_U1, move_R1, move_B1, move_L1, move_F1,move_D1]
continue_algo = True
continue_iteration = True
continue_search= True
before={}
"""functions"""
# calculate the heuristic for the current state of cube
def heuristic(current, goal):
    solved_cube= convert_to_3D_format(goal)
    current_cube= convert_to_3D_format(current)
    total_distance = 0

    # Iterate over all positions in the 3x3x3 cube
    for x in range(3):
        for y in range(3):
            for z in range(3):
                cubie = current_cube[x][y][z]  # Get the current cubie

                # Find this cubie in the solved state
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            if set(solved_cube[i][j][k]) == set(cubie):  # Check by set since order may not matter
                                # Compute Manhattan distance and add to total
                                total_distance += abs(i - x) + abs(j - y) + abs(k - z)
                                break  # Stop searching once the cubie is found
    return (total_distance-8)/8
#function that allows me to print the cube in a bette way
def print_cube(cube):
    for face in cube:
        for x in range(0,9,3):
            print(face[x:x+3])
        print("")
# calculate the f_score and classify them  for every possible child of the current cube
def get_f_scores(threshold):
    global  pre_open
    global pruned
    pre_open.clear()
    face_classification= {"move_B1":1,
                          "move_B2":1,
                          "move_BB":1,

                          "move_U1":2,
                          "move_U2":2,
                          "move_UU":2,

                          "move_D1":1,
                          "move_D2":1,
                          "move_DD":1,

                          "move_F1":2,
                          "move_F2":2,
                          "move_FF":2,

                          "move_L1":1,
                          "move_L2":1,
                          "move_LL":1,
                          "move_R1":2,
                          "move_R2":2,
                          "move_RR":2}
    if open_state:
        g= open_state[0][4]+1
        previous_move= open_state[0][0]
        previous_move_name= previous_move.__name__
    else:
        g=1
        previous_move=" "
        previous_move_name=""
    if previous_move_name != "":
        if face_classification[previous_move_name]== 1:
            possibility = [[move_U1,move_U2,move_UU],[move_DD,move_D1,move_D2],[move_B1,move_B2,move_BB],[move_FF,move_F1,move_F2],
                       [move_LL,move_L2,move_L1],[move_RR,move_R1,move_R2]]
        else:
            possibility = [[move_U1, move_U2, move_UU,move_DD, move_D1, move_D2],
                           [move_B1, move_B2, move_BB,move_FF, move_F1, move_F2],
                           [move_LL, move_L2, move_L1,move_RR, move_R1, move_R2]]
    else:
        possibility = [[move_U1, move_U2, move_UU], [move_DD, move_D1, move_D2], [move_B1, move_B2, move_BB],
                       [move_FF, move_F1, move_F2],
                       [move_LL, move_L2, move_L1], [move_RR, move_R1, move_R2]]
    possibility= [sublist for sublist in possibility if previous_move not in sublist]
    # Appliquer les mouvements de move_set1
    for x in range(len(move_set1)):
        if  any(move_set1[x] in sublist for sublist in possibility) :
            move_set1[x]()  # Appliquer le mouvement F1, F2, etc.

            # Calculer la fonction de coût f = g + h (heuristique)
            f = g + heuristic(cube,goal)

            # Vérifier si on reste sous le seuil
            current_cube_as_string=list_to_string(cube)
            if f <= threshold:
                if current_cube_as_string not in before:
                    pre_open.append([move_set1[x],f,heuristic(cube,goal),current_cube_as_string,g])
            if f > threshold:
                pruned.append([move_set1[x],f,heuristic(cube,goal),current_cube_as_string,g])
            before.add(current_cube_as_string)
            # Annuler le mouvement
            move_set1_undo[x]()
        else :
            f = g + heuristic(cube, goal)
            pruned.append([move_set1[x], f, heuristic(cube, goal), list_to_string(cube), g])
    # Appliquer les mouvements de move_set2
    for x in range(len(move_set2)):
        if  any(move_set2[x] in sublist for sublist in possibility) :
            # Appliquer le mouvement
            move_set2[x]()
            # Calculer la fonction de coût f = g + h (heuristique)
            f = g + heuristic(cube, goal)
            # Vérifier si on reste sous le seuil
            current_cube_as_string=list_to_string(cube)
            if f <= threshold:
                if current_cube_as_string not in before:
                    pre_open.append([move_set2[x], f, heuristic(cube, goal),current_cube_as_string,g])
            if f > threshold:
                pruned.append([move_set2[x], f, heuristic(cube, goal),current_cube_as_string,g])

            before.add(current_cube_as_string)

            # Annuler le mouvement
            move_set2_undo[x]()
        else:
            f = g + heuristic(cube, goal)
            pruned.append([move_set2[x], f, heuristic(cube, goal), list_to_string(cube), g])
    # Trier les résultats pour garder les meilleurs en fonction de f
    pre_open.sort(key=lambda x: (x[1], x[2]))
    return pre_open, pruned
"""zone to scramble the cube with some moves"""
move_R1()
move_F2()
move_B2()
move_L1()
move_DD()
move_U2()
move_R2()
move_L1()
move_B2()
move_L1()
move_B2()
move_L1()
move_B1()
move_R1()
move_R2()
move_D1()
move_L1()
move_D1()
move_F1()
move_B1()
move_B2()
move_U2()
move_U1()
move_R1()
move_D1()
move_L2()
move_D2()
move_U2()
move_U2()
move_D1()
move_B1()
move_U2()
move_F1()
move_B1()
move_U1()
move_D1()
move_R1()
move_R2()
move_L1()
move_R2()

print(cube)
start= list_to_string(cube)
#lalgo trouve la solution avec f1/F2 / D1/ D2 / R1/R2/L1/L2/ quand on utilise quatre move
"""algorythm"""
while continue_algo:
    global threshold
    before = {""}

    iteration += 1
    # we handle the case for the first iteration
    if iteration == 1:
        open_state.clear()
        threshold= 0
        get_f_scores(threshold)
        open_state = pre_open+ open_state
        #we check each node under the threshold
        while open_state:
            cube = string_to_2d_list(open_state[0][3])
            # we check if this is the solution and if yes we break the loop
            if cube == goal:
                continue_algo = 0
                break

            # if its not we explore the children and we remove the one that we just visited to avoid repetition
            get_f_scores(threshold)
            open_state.pop(0)
            open_state = pre_open + open_state
        #in this case if open state is empty the line of code wont just be readed and it will go to the next iteration

        continue
    #now we handle the case for the other iterationw
    if iteration !=1:
        cube= string_to_2d_list(start)
        open_state.clear()
        #now we get the new threshold
        pruned.sort(key=lambda x: (x[1], x[2]))

        threshold = threshold+ 1
        print("iteration #",iteration,"threshold:",threshold,)
        pruned.clear()
        #now we can get the new openstate
        get_f_scores(threshold)
        open_state = pre_open + open_state
        #now we can start the loop for the algo
        while open_state:

            cube = string_to_2d_list(open_state[0][3])
            # we check if this is the solution and if yes we break the loop
            if cube[0] == goal[0]:

                continue_algo = 0
                break

            # if its not we explore the children and we remove the one that we just visited to avoid repetition
            get_f_scores(threshold)
            open_state.pop(0)
            open_state = pre_open + open_state

            # in this case if open state is empty the line of code wont just be readed and it will go to the next iteration

        continue
print_cube(cube)
print("si tu vois cela cest que sa marche!!!!!")
print("--- %s seconds ---" % (time.time() - start_time))
