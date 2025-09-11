def move_U1(cube):
    cube[11], cube[10], cube[9], cube[18], cube[19], cube[20], cube[29], cube[28], cube[27], cube[36], cube[37], cube[38] = \
    cube[20], cube[19], cube[18], cube[27], cube[28], cube[29], cube[38], cube[37], cube[36], cube[9], cube[10], cube[11]
    cube[0:9] = [cube[6], cube[3], cube[0],cube[7], cube[4], cube[1],cube[8], cube[5], cube[2]]

def move_U2(cube):
    cube[36], cube[37], cube[38], cube[27], cube[28], cube[29], cube[18], cube[19], cube[20], cube[9], cube[10], cube[11] = \
    cube[27], cube[28], cube[29], cube[18], cube[19], cube[20], cube[9], cube[10], cube[11], cube[36], cube[37], cube[38]
    cube[0:9] = [cube[2], cube[5], cube[8],cube[1], cube[4], cube[7],cube[0], cube[3], cube[6]]

def move_UU(cube):
    cube[9], cube[10], cube[11], cube[27], cube[28], cube[29] = cube[27], cube[28], cube[29], cube[9], cube[10], cube[11]
    cube[18], cube[19], cube[20], cube[36], cube[37], cube[38] = cube[36], cube[37], cube[38], cube[18], cube[19], cube[20]
    cube[0:9] = [cube[8], cube[7], cube[6],cube[5], cube[4], cube[3],cube[2], cube[1], cube[0]]

def move_D1(cube):
    cube[33], cube[34], cube[35], cube[24], cube[25], cube[26], cube[15], cube[16], cube[17], cube[42], cube[43], cube[44] = \
    cube[24], cube[25], cube[26], cube[15], cube[16], cube[17], cube[42], cube[43], cube[44], cube[33], cube[34], cube[35]
    cube[45:54] = [cube[51], cube[48], cube[45],cube[52], cube[49], cube[46],cube[53], cube[50], cube[47]]

def move_D2(cube):
    cube[24], cube[25], cube[26], cube[33], cube[34], cube[35], cube[42], cube[43], cube[44], cube[15], cube[16], cube[17] = \
    cube[33], cube[34], cube[35], cube[42], cube[43], cube[44], cube[15], cube[16], cube[17], cube[24], cube[25], cube[26]
    cube[45:54] = [cube[47], cube[50], cube[53],cube[46], cube[49], cube[52],cube[45], cube[48], cube[51]]

def move_DD(cube):
    cube[15], cube[16], cube[17], cube[33], cube[34], cube[35] = cube[33], cube[34], cube[35], cube[15], cube[16], cube[17]
    cube[24], cube[25], cube[26], cube[42], cube[43], cube[44] = cube[42], cube[43], cube[44], cube[24], cube[25], cube[26]
    cube[45:54] = [cube[53], cube[52], cube[51],cube[50], cube[49], cube[48],cube[47], cube[46], cube[45]]

def move_F1(cube):
    cube[9], cube[12], cube[15], cube[6], cube[7], cube[8], cube[29], cube[32], cube[35], cube[45], cube[46], cube[47] = \
    cube[6], cube[7], cube[8], cube[35], cube[32], cube[29], cube[45], cube[46], cube[47], cube[15], cube[12], cube[9]
    cube[36:45] = [cube[42], cube[39], cube[36],cube[43], cube[40], cube[37],cube[44], cube[41], cube[38]]

def move_F2(cube):
    cube[9], cube[12], cube[15], cube[45], cube[46], cube[47], cube[29], cube[32], cube[35], cube[6], cube[7], cube[8] = \
    cube[47], cube[46], cube[45], cube[29], cube[32], cube[35], cube[8], cube[7], cube[6], cube[9], cube[12], cube[15]
    cube[36:45] = [cube[38], cube[41], cube[44],cube[37], cube[40], cube[43],cube[36], cube[39], cube[42]]

def move_FF(cube):
    cube[6], cube[7], cube[8], cube[45], cube[46], cube[47] = cube[47], cube[46], cube[45], cube[8], cube[7], cube[6]
    cube[29], cube[32], cube[35], cube[9], cube[12], cube[15] = cube[15], cube[12], cube[9], cube[35], cube[32], cube[29]
    cube[36:45] = [cube[44], cube[43], cube[42],cube[41], cube[40], cube[39],cube[38], cube[37], cube[36]]

def move_B1(cube):
    cube[27], cube[30], cube[33], cube[0], cube[1], cube[2], cube[11], cube[14], cube[17], cube[51], cube[52], cube[53] = \
    cube[2], cube[1], cube[0], cube[11], cube[14], cube[17], cube[53], cube[52], cube[51], cube[27], cube[30], cube[33]
    cube[18:27] = [cube[24], cube[21], cube[18],cube[25], cube[22], cube[19],cube[26], cube[23], cube[20]]

def move_B2(cube):
    cube[11], cube[14], cube[17], cube[0], cube[1], cube[2], cube[27], cube[30], cube[33], cube[51], cube[52], cube[53] = \
    cube[0], cube[1], cube[2], cube[33], cube[30], cube[27], cube[51], cube[52], cube[53], cube[17], cube[14], cube[11]
    cube[18:27] = [cube[20], cube[23], cube[26],cube[19], cube[22], cube[25],cube[18], cube[21], cube[24]]

def move_BB(cube):
    cube[0], cube[1], cube[2], cube[51], cube[52], cube[53] = cube[53], cube[52], cube[51], cube[2], cube[1], cube[0]
    cube[11], cube[14], cube[17], cube[27], cube[30], cube[33] = cube[33], cube[30], cube[27], cube[17], cube[14], cube[11]
    cube[18:27] = [cube[26], cube[25], cube[24],cube[23], cube[22], cube[21],cube[20], cube[19], cube[18]]

def move_R1(cube):
    cube[2], cube[5], cube[8], cube[38], cube[41], cube[44], cube[47], cube[50], cube[53], cube[18], cube[21], cube[24] = \
    cube[38], cube[41], cube[44], cube[47], cube[50], cube[53], cube[24], cube[21], cube[18], cube[8], cube[5], cube[2]
    cube[9:18] = [cube[15], cube[12], cube[9],cube[16], cube[13], cube[10],cube[17], cube[14], cube[11]]

def move_R2(cube):
    cube[18], cube[21], cube[24], cube[47], cube[50], cube[53], cube[38], cube[41], cube[44], cube[2], cube[5], cube[8] = \
    cube[53], cube[50], cube[47], cube[38], cube[41], cube[44], cube[2], cube[5], cube[8], cube[24], cube[21], cube[18]
    cube[9:18] = [cube[11], cube[14], cube[17],cube[10], cube[13], cube[16],cube[9],  cube[12], cube[15]]

def move_RR(cube):
    cube[2], cube[5], cube[8], cube[47], cube[50], cube[53] = cube[47], cube[50], cube[53], cube[2], cube[5], cube[8]
    cube[18], cube[21], cube[24], cube[38], cube[41], cube[44] = cube[44], cube[41], cube[38], cube[24], cube[21], cube[18]
    cube[9:18] = [cube[17], cube[16], cube[15],cube[14], cube[13], cube[12],cube[11], cube[10], cube[9]]

def move_L1(cube):
    cube[45], cube[48], cube[51], cube[36], cube[39], cube[42], cube[0], cube[3], cube[6], cube[20], cube[23], cube[26] = \
    cube[36], cube[39], cube[42], cube[0], cube[3], cube[6], cube[26], cube[23], cube[20], cube[51], cube[48], cube[45]
    cube[27:36] = [cube[33], cube[30], cube[27],cube[34], cube[31], cube[28],cube[35], cube[32], cube[29]]

def move_L2(cube):
    cube[36], cube[39], cube[42], cube[45], cube[48], cube[51], cube[20], cube[23], cube[26], cube[0], cube[3], cube[6] = \
    cube[45], cube[48], cube[51], cube[26], cube[23], cube[20], cube[6], cube[3], cube[0], cube[36], cube[39], cube[42]
    cube[27:36] = [cube[29], cube[32], cube[35],cube[28], cube[31], cube[34],cube[27], cube[30], cube[33]]

def move_LL(cube):
    cube[0], cube[3], cube[6], cube[45], cube[48], cube[51] = cube[45], cube[48], cube[51], cube[0], cube[3], cube[6]
    cube[20], cube[23], cube[26], cube[36], cube[39], cube[42] = cube[42], cube[39], cube[36], cube[26], cube[23], cube[20]
    cube[27:36] = [cube[35], cube[34], cube[33],cube[32], cube[31], cube[30],cube[29], cube[28], cube[27]]
