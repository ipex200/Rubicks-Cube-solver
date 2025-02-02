
"""import the tools that I need """
import copy
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

"""useful variables"""
start= copy.deepcopy(cube)
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

"""functions"""
# calculate the heuristic for the current state of cube
def heuristic(current, goal):
    dif = 0
    for face_index in range(len(current)):
        for square_index in range(len(current[face_index])):
            if current[face_index][square_index] != goal[face_index][square_index]:
                dif += 1
    return dif / 20
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
    if not open_state:
        g=1
    else:
        g= open_state[0][4]+1
    # Appliquer les mouvements de move_set1
    for x in range(len(move_set1)):
        move_set1[x]()  # Appliquer le mouvement F1, F2, etc.

        # Calculer la fonction de coût f = g + h (heuristique)
        f = g + heuristic(cube,goal)
        # Vérifier si on reste sous le seuil
        if f <= threshold:
            pre_open.append([move_set1[x],f,heuristic(cube,goal),copy.deepcopy(cube),g])
        if f > threshold:
            pruned.append([move_set1[x],f,heuristic(cube,goal),copy.deepcopy(cube),g])
        # Annuler le mouvement
        move_set1_undo[x]()
    # Appliquer les mouvements de move_set2
    for x in range(len(move_set2)):
        # Appliquer le mouvement
        move_set2[x]()
        # Calculer la fonction de coût f = g + h (heuristique)
        f = g + heuristic(cube, goal)
        # Vérifier si on reste sous le seuil
        if f <= threshold:
            pre_open.append([move_set2[x], f, heuristic(cube, goal), copy.deepcopy(cube),g])
        if f > threshold:
            pruned.append([move_set2[x], f, heuristic(cube, goal), copy.deepcopy(cube),g])
        # Annuler le mouvement
        move_set2_undo[x]()
    # Trier les résultats pour garder les meilleurs en fonction de f
    pre_open.sort(key=lambda x: (x[1], x[2]))
    return pre_open, pruned
"""zone to scramble the cube with some moves"""

move_D1()
move_B2()
move_F2()
move_D2()
move_D2()
move_L2()
move_D1()
start= copy.deepcopy(cube)
#lalgo trouve la solution avec f1/F2 / D1/ D2 / R1/R2/L1/L2/ quand on utilise quatre move
"""algorythm"""
while continue_algo:
    global threshold
    iteration += 1
    # we handle the case for the first iteration
    if iteration == 1:
        open_state.clear()
        threshold= heuristic(cube,goal)
        get_f_scores(threshold)
        open_state = pre_open+ open_state
        #we check each node under the threshold
        while open_state:

            cube = copy.deepcopy(open_state[0][3])
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
        cube= copy.deepcopy(start)
        open_state.clear()
        #now we get the new threshold
        pruned.sort(key=lambda x: (x[1], x[2]))
        threshold = pruned[0][1]*1.1
        pruned.clear()
        #now we can get the new openstate
        get_f_scores(threshold)
        open_state = pre_open + open_state
        #now we can start the loop for the algo
        print(iteration)
        while open_state:
            cube = copy.deepcopy(open_state[0][3])
            # we check if this is the solution and if yes we break the loop
            if cube == goal:
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