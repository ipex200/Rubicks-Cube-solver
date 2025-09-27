#include <array>

#include <unordered_map>
 /* W : 0
    R: 1
    B: 2
    O: 3
    G: 4
    Y: 5
        */

std::array<unsigned char,12> temp_side;
std::array<unsigned char,9> temp_face;  
using cube_type= std::array<unsigned char,54> ;
using MoveFunc = void (*)(std::array<unsigned char,54>&);

void No_move(cube_type& cube){}                            
void move_U1(cube_type& cube){
    temp_side={ cube[20], cube[19], cube[18], cube[27], cube[28], cube[29], cube[38], cube[37], cube[36], cube[9], cube[10], cube[11]};
    temp_face={ cube[6], cube[3], cube[0],cube[7], cube[4], cube[1],cube[8], cube[5], cube[2]};

    cube[11]= temp_side[0];cube[10]=temp_side[1]; cube[9]=temp_side[2]; cube[18]=temp_side[3]; cube[19]=temp_side[4]; cube[20]=temp_side[5]; cube[29]=temp_side[6]; cube[28]=temp_side[7]; cube[27]=temp_side[8]; cube[36]=temp_side[9]; cube[37]=temp_side[10]; cube[38]=temp_side[11]; 
   
    cube[0]= temp_face[0];cube[1]=temp_face[1] ;cube[2]=temp_face[2] ;cube[3]=temp_face[3] ;cube[4]=temp_face[4] ;cube[5]= temp_face[5];cube[6]= temp_face[6] ;cube[7]= temp_face[7] ;cube[8]=temp_face[8];
}
void move_U2(cube_type& cube){
    temp_side={cube[27], cube[28], cube[29], cube[18], cube[19], cube[20], cube[9], cube[10], cube[11], cube[36], cube[37], cube[38]};
    temp_face={cube[2], cube[5], cube[8],cube[1], cube[4], cube[7],cube[0], cube[3], cube[6]};

    cube[36]=temp_side[0] ; cube[37]= temp_side[1]; cube[38]=temp_side[2] ; cube[27]= temp_side[3]; cube[28]= temp_side[4]; cube[29]=temp_side[5] ; cube[18]=temp_side[6] ; cube[19]=temp_side[7] ; cube[20]= temp_side[8]; cube[9]= temp_side[9]; cube[10]=temp_side[10] ; cube[11]=temp_side[11];

    cube[0]= temp_face[0];cube[1]= temp_face[1];cube[2]=temp_face[2] ;cube[3]=temp_face[3] ;cube[4]=temp_face[4] ;cube[5]=temp_face[5] ;cube[6]=temp_face[6] ;cube[7]= temp_face[7];cube[8]=temp_face[8];
}
void move_UU(cube_type& cube){
    temp_side={ cube[27], cube[28], cube[29], cube[9], cube[10], cube[11],cube[36], cube[37], cube[38], cube[18], cube[19], cube[20]};
    temp_face={cube[8], cube[7], cube[6],cube[5], cube[4], cube[3],cube[2], cube[1], cube[0]};

    cube[9]= temp_side[0]; cube[10]= temp_side[1]; cube[11]= temp_side[2]; cube[27]= temp_side[3] ; cube[28]= temp_side[4]; cube[29] =temp_side[5];
    cube[18]= temp_side[6] ; cube[19]= temp_side[7]; cube[20]= temp_side[8]; cube[36]= temp_side[9]; cube[37]=temp_side[10] ; cube[38] = temp_side[11];

    cube[0]=temp_face[0];cube[1]=temp_face[1];cube[2]=temp_face[2];cube[3]=temp_face[3];cube[4]=temp_face[4];cube[5]=temp_face[5];cube[6]=temp_face[6];cube[7]=temp_face[7];cube[8] =temp_face[8] ;
}
void move_D1(cube_type& cube){
    temp_side={ cube[24], cube[25], cube[26], cube[15], cube[16], cube[17], cube[42], cube[43], cube[44], cube[33], cube[34], cube[35]};
    temp_face={cube[51], cube[48], cube[45],cube[52], cube[49], cube[46],cube[53], cube[50], cube[47]}; ;

    cube[33]=temp_side[0] ; cube[34]= temp_side[1] ; cube[35]= temp_side[2] ; cube[24]=temp_side[3]  ; cube[25]= temp_side[4] ; cube[26]= temp_side[5] ; cube[15]= temp_side[6] ; cube[16]= temp_side[7]  ; cube[17]=temp_side[8]  ; cube[42]= temp_side[9] ; cube[43]= temp_side[10] ; cube[44] =temp_side[11]  ;

    cube[45]= temp_face[0];cube[46]=temp_face[1] ;cube[47]= temp_face[2];cube[48]= temp_face[3];cube[49]=temp_face[4] ;cube[50]= temp_face[5];cube[51]= temp_face[6];cube[52]= temp_face[7];cube[53] = temp_face[8];
}
//je me suis arreter ici hier demain tu dois commencer par D2 etsuprimer ce commentaire
void move_D2(cube_type& cube){
    temp_side={cube[33], cube[34], cube[35], cube[42], cube[43], cube[44], cube[15], cube[16], cube[17], cube[24], cube[25], cube[26]};
    temp_face={cube[47], cube[50], cube[53],cube[46], cube[49], cube[52],cube[45], cube[48], cube[51]};
    cube[24]=temp_side[0]; cube[25]=temp_side[1] ; cube[26]=temp_side[2] ; cube[33]= temp_side[3]; cube[34]= temp_side[4]; cube[35]=temp_side[5] ; cube[42]=temp_side[6] ; cube[43]=temp_side[7] ; cube[44]=temp_side[8] ; cube[15]=temp_side[9] ; cube[16]=temp_side[10] ; cube[17] =temp_side[11] ;

    cube[45]= temp_face[0];cube[46]= temp_face[1];cube[47]=temp_face[2] ;cube[48]=temp_face[3] ;cube[49]= temp_face[4];cube[50]= temp_face[5];cube[51]= temp_face[6] ;cube[52]= temp_face[7] ;cube[53] = temp_face[8]; 
}
void move_DD(cube_type& cube){
    temp_side={cube[33], cube[34], cube[35], cube[15], cube[16], cube[17], cube[42], cube[43], cube[44], cube[24], cube[25], cube[26]};
    temp_face={ cube[53], cube[52], cube[51],cube[50], cube[49], cube[48],cube[47], cube[46], cube[45]};

    cube[15]=temp_side[0] ; cube[16]=temp_side[1] ; cube[17]= temp_side[2]; cube[33]= temp_side[3]; cube[34]=temp_side[4] ; cube[35] =temp_side[5] ;
    cube[24]=temp_side[6] ; cube[25]=temp_side[7] ; cube[26]=temp_side[8] ; cube[42]=temp_side[9] ; cube[43]=temp_side[10] ; cube[44] =temp_side[11];

    cube[45]= temp_face[0];cube[46]=temp_face[1] ;cube[47]=temp_face[2] ;cube[48]=temp_face[3] ;cube[49]=temp_face[4] ;cube[50]= temp_face[5];cube[51]=temp_face[6] ;cube[52]= temp_face[7];cube[53] =temp_face[8];
}
void move_F1(cube_type& cube){
    temp_side={cube[6], cube[7], cube[8], cube[35], cube[32], cube[29], cube[45], cube[46], cube[47], cube[15], cube[12], cube[9]};
    temp_face={ cube[42], cube[39], cube[36],cube[43], cube[40], cube[37],cube[44], cube[41], cube[38]};

    cube[9]=temp_side[0] ; cube[12]= temp_side[1]; cube[15]= temp_side[2]; cube[6]=temp_side[3] ; cube[7]=temp_side[4] ; cube[8]= temp_side[5]; cube[29]=temp_side[6] ; cube[32]= temp_side[7] ; cube[35]= temp_side[8] ; cube[45]= temp_side[9]; cube[46]=temp_side[10] ; cube[47] = temp_side[11] ;

    cube[36]= temp_face[0];cube[37]= temp_face[1];cube[38]= temp_face[2] ;cube[39]= temp_face[3];cube[40]= temp_face[4];cube[41]= temp_face[5];cube[42]= temp_face[6];cube[43]=temp_face[7] ;cube[44] = temp_face[8];
}
void move_F2(cube_type& cube){
    temp_side={cube[47], cube[46], cube[45], cube[29], cube[32], cube[35], cube[8], cube[7], cube[6], cube[9], cube[12], cube[15]};
    temp_face={cube[38], cube[41], cube[44],cube[37], cube[40], cube[43],cube[36], cube[39], cube[42]};

    cube[9]= temp_side[0]; cube[12]= temp_side[1]; cube[15]= temp_side[2]; cube[45]= temp_side[3]; cube[46]= temp_side[4]; cube[47]= temp_side[5]; cube[29]= temp_side[6]; cube[32]= temp_side[7]; cube[35]= temp_side[8]; cube[6]= temp_side[9]; cube[7]= temp_side[10]; cube[8] = temp_side[11];        

    cube[36]= temp_face[0];cube[37]= temp_face[1];cube[38]= temp_face[2];cube[39]= temp_face[3];cube[40]= temp_face[4];cube[41]= temp_face[5];cube[42]= temp_face[6];cube[43]= temp_face[7];cube[44] =temp_face[8] ;
}
void move_FF(cube_type& cube){
    temp_side={ cube[47], cube[46], cube[45], cube[8], cube[7], cube[6], cube[15], cube[12], cube[9], cube[35], cube[32], cube[29]};
    temp_face={cube[44], cube[43], cube[42],cube[41], cube[40], cube[39],cube[38], cube[37], cube[36]};
    
    cube[6]=temp_side[0]; cube[7]=temp_side[1]; cube[8]=temp_side[2]; cube[45]=temp_side[3]; cube[46]=temp_side[4]; cube[47] =temp_side[5];cube[29]=temp_side[6]; cube[32]=temp_side[7]; cube[35]=temp_side[8]; cube[9]=temp_side[9]; cube[12]=temp_side[10]; cube[15] =temp_side[11];

    cube[36]=temp_face[0];cube[37]=temp_face[1];cube[38]=temp_face[2];cube[39]=temp_face[3];cube[40]=temp_face[4];cube[41]=temp_face[5];cube[42]=temp_face[6];cube[43]=temp_face[7];cube[44] = temp_face[8];
}
void move_B1(cube_type& cube){
    temp_side={cube[2], cube[1], cube[0], cube[11], cube[14], cube[17], cube[53], cube[52], cube[51], cube[27], cube[30], cube[33]};
    temp_face={cube[24], cube[21], cube[18],cube[25], cube[22], cube[19],cube[26], cube[23], cube[20]};
    cube[27]=temp_side[0]; cube[30]=temp_side[1]; cube[33]=temp_side[2]; cube[0]=temp_side[3]; cube[1]=temp_side[4]; cube[2]=temp_side[5]; cube[11]=temp_side[6]; cube[14]=temp_side[7]; cube[17]=temp_side[8]; cube[51]=temp_side[9]; cube[52]=temp_side[10]; cube[53] =temp_side[11] ;

    cube[18]=temp_face[0]; cube[19]=temp_face[1]; cube[20]=temp_face[2];cube[21]=temp_face[3]; cube[22]=temp_face[4]; cube[23]=temp_face[5];cube[24]=temp_face[6]; cube[25]=temp_face[7]; cube[26] =temp_face[8];
}
void move_B2(cube_type& cube){
    temp_side={cube[0], cube[1], cube[2], cube[33], cube[30], cube[27], cube[51], cube[52], cube[53], cube[17], cube[14], cube[11]};
    temp_face={ cube[20], cube[23], cube[26],cube[19], cube[22], cube[25],cube[18], cube[21], cube[24]};

    cube[11]=temp_side[0] ; cube[14]= temp_side[1]; cube[17]=temp_side[2] ; cube[0]= temp_side[3]; cube[1]= temp_side[4]; cube[2]=temp_side[5] ; cube[27]= temp_side[6]; cube[30]=temp_side[7] ; cube[33]=temp_side[8] ; cube[51]= temp_side[9]; cube[52]= temp_side[10]; cube[53] =temp_side[11] ;

    cube[18]= temp_face[0]; cube[19]=temp_face[1]; cube[20]=temp_face[2] ;cube[21]= temp_face[3]; cube[22]= temp_face[4]; cube[23]= temp_face[5];cube[24]=temp_face[6] ; cube[25]= temp_face[7] ; cube[26] = temp_face[8];
}

void move_BB(cube_type& cube){
    temp_side={cube[53], cube[52], cube[51], cube[2], cube[1], cube[0], cube[33], cube[30], cube[27], cube[17], cube[14], cube[11]};
    temp_face={cube[26], cube[25], cube[24],cube[23], cube[22], cube[21],cube[20], cube[19], cube[18]};

    cube[0]=temp_side[0]; cube[1]=temp_side[1]; cube[2]=temp_side[2]; cube[51]=temp_side[3]; cube[52]=temp_side[4]; cube[53] = temp_side[5];
    cube[11]=temp_side[6]; cube[14]=temp_side[7]; cube[17]=temp_side[8]; cube[27]=temp_side[9]; cube[30]=temp_side[10]; cube[33] =temp_side[11];

    cube[18] = temp_face[0];cube[19] = temp_face[1];cube[20] = temp_face[2];cube[21] = temp_face[3];cube[22] = temp_face[4];cube[23] = temp_face[5];cube[24] = temp_face[6];cube[25] = temp_face[7];cube[26] = temp_face[8];    }
void move_R1(cube_type& cube){
    temp_side={cube[38], cube[41], cube[44], cube[47], cube[50], cube[53], cube[24], cube[21], cube[18], cube[8], cube[5], cube[2]};
    temp_face={cube[15], cube[12], cube[9],cube[16], cube[13], cube[10],cube[17], cube[14], cube[11]};
    
    cube[2]=temp_side[0]; cube[5]=temp_side[1]; cube[8]=temp_side[2]; cube[38]=temp_side[3]; cube[41]=temp_side[4]; cube[44]=temp_side[5]; cube[47]=temp_side[6]; cube[50]=temp_side[7]; cube[53]=temp_side[8]; cube[18]=temp_side[9]; cube[21]=temp_side[10]; cube[24] =temp_side[11]; ;

    cube[9]=temp_face[0]; cube[10]=temp_face[1]; cube[11]=temp_face[2];cube[12]=temp_face[3]; cube[13]=temp_face[4]; cube[14]=temp_face[5];cube[15]=temp_face[6]; cube[16]=temp_face[7]; cube[17]= temp_face[8];
}
void move_R2(cube_type& cube){
    temp_side={cube[53], cube[50], cube[47], cube[38], cube[41], cube[44], cube[2], cube[5], cube[8], cube[24], cube[21], cube[18]};
    temp_face={cube[11], cube[14], cube[17],cube[10], cube[13], cube[16],cube[9],  cube[12], cube[15]}; 

    cube[18]=temp_side[0]; cube[21]=temp_side[1]; cube[24]=temp_side[2]; cube[47]=temp_side[3]; cube[50]=temp_side[4]; cube[53]=temp_side[5]; cube[38]=temp_side[6]; cube[41]=temp_side[7]; cube[44]=temp_side[8]; cube[2]=temp_side[9]; cube[5]=temp_side[10]; cube[8] =temp_side[11] ;

    cube[9]=temp_face[0]; cube[10]=temp_face[1]; cube[11]=temp_face[2];cube[12]=temp_face[3]; cube[13]=temp_face[4]; cube[14]=temp_face[5];cube[15]=temp_face[6]; cube[16]=temp_face[7]; cube[17] = temp_face[8];
}
void move_RR(cube_type& cube){
    temp_side={ cube[47], cube[50], cube[53], cube[2], cube[5], cube[8],cube[44], cube[41], cube[38], cube[24], cube[21], cube[18]};
    temp_face={ cube[17], cube[16], cube[15],cube[14], cube[13], cube[12],cube[11], cube[10], cube[9]};
    
    cube[2]=temp_side[0]; cube[5]=temp_side[1]; cube[8]=temp_side[2]; cube[47]=temp_side[3]; cube[50]=temp_side[4]; cube[53] =temp_side[5];
    cube[18]=temp_side[6]; cube[21]=temp_side[7]; cube[24]=temp_side[8]; cube[38]=temp_side[9]; cube[41]=temp_side[10]; cube[44] = temp_side[11];

    cube[9]=temp_face[0]; cube[10]=temp_face[1]; cube[11]=temp_face[2];cube[12]=temp_face[3]; cube[13]=temp_face[4]; cube[14]=temp_face[5];cube[15]=temp_face[6]; cube[16]=temp_face[7]; cube[17] =temp_face[8];
}
void move_L1(cube_type& cube){
    temp_side={cube[36], cube[39], cube[42], cube[0], cube[3], cube[6], cube[26], cube[23], cube[20], cube[51], cube[48], cube[45]};
    temp_face={cube[33], cube[30], cube[27],cube[34], cube[31], cube[28],cube[35], cube[32], cube[29]};

    cube[45]=temp_side[0]; cube[48]=temp_side[1]; cube[51]=temp_side[2]; cube[36]=temp_side[3]; cube[39]=temp_side[4]; cube[42]=temp_side[5]; cube[0]=temp_side[6]; cube[3]=temp_side[7]; cube[6]=temp_side[8]; cube[20]=temp_side[9]; cube[23]=temp_side[10]; cube[26]=temp_side[11]; 

    cube[27]=temp_face[0]; cube[28]=temp_face[1]; cube[29]=temp_face[2];cube[30]=temp_face[3]; cube[31]=temp_face[4]; cube[32]=temp_face[5];cube[33]=temp_face[6]; cube[34]=temp_face[7]; cube[35]=temp_face[8];
}
void move_L2(cube_type& cube){
    temp_side={cube[45], cube[48], cube[51], cube[26], cube[23], cube[20], cube[6], cube[3], cube[0], cube[36], cube[39], cube[42]};
    temp_face={cube[29], cube[32], cube[35],cube[28], cube[31], cube[34],cube[27], cube[30], cube[33]};

    cube[36]=temp_side[0]; cube[39]=temp_side[1]; cube[42]=temp_side[2]; cube[45]=temp_side[3]; cube[48]=temp_side[4]; cube[51]=temp_side[5]; cube[20]=temp_side[6]; cube[23]=temp_side[7]; cube[26]=temp_side[8]; cube[0]=temp_side[9]; cube[3]=temp_side[10]; cube[6]=temp_side[11];
    
    cube[27]=temp_face[0]; cube[28]=temp_face[1]; cube[29]=temp_face[2];cube[30]=temp_face[3]; cube[31]=temp_face[4]; cube[32]=temp_face[5];cube[33]=temp_face[6]; cube[34]=temp_face[7]; cube[35]=temp_face[8];
}
void move_LL(cube_type& cube){
    temp_side={cube[45], cube[48], cube[51], cube[0], cube[3], cube[6],cube[42], cube[39], cube[36], cube[26], cube[23], cube[20]};
    temp_face={cube[35], cube[34], cube[33],cube[32], cube[31], cube[30],cube[29], cube[28], cube[27]};

    cube[0]=temp_side[0]; cube[3]=temp_side[1]; cube[6]=temp_side[2]; cube[45]=temp_side[3]; cube[48]=temp_side[4]; cube[51]=temp_side[5];
    cube[20]=temp_side[6]; cube[23]=temp_side[7]; cube[26]=temp_side[8]; cube[36]=temp_side[9]; cube[39]=temp_side[10]; cube[42]=temp_side[11];
    cube[27]=temp_face[0]; cube[28]=temp_face[1]; cube[29]=temp_face[2];cube[30]=temp_face[3]; cube[31]=temp_face[4]; cube[32]=temp_face[5];cube[33]=temp_face[6]; cube[34]=temp_face[7]; cube[35]=temp_face[8];   
 }
void hash_cube(const cube_type& cube ,std::array<int,27>& hash_container){
    hash_container ={
    cube[0]*19683+ cube[27]*729+ cube[20]*27,     //index 0 corner
    cube[30]*729+cube[23]*27+1,                   //index 1 edge
    cube[33]*19683+ cube[26]*729+cube[51]*27+2,   //index 2 corner
    cube[1]*729+ cube[19]*27+3,                   //index 3 edge
    0,                                            //index 4
    cube[25]*729+ cube[52]*27+5,                  //index 5 edge
    cube[2]*19683+ cube[11]*729+ cube[18]*27+6,   //index 6 corner
    cube[14]*729+ cube[21]*27+7,                  //index 7 edge
    cube[17]*19683+ cube[24]*729+cube[53]*27+8,   //index 8 corner
    cube[3]*729+ cube[28]*27+9,                   //index 9 edge
    0,                                            //index 10
    cube[34]*729+ cube[48]*27+11,                 //index 11 edge
    0,                                            //index 12
    0,                                            //index 13
    0,                                            //index 14
    cube[5]*729+ cube[10]*27+15,                  //index 15 edge
    0,                                            //index 16
    cube[16]*729+ cube[50]*27+17,                 //index 17 edge
    cube[6]*19683+ cube[36]*729+cube[29]*27+18,   //index 18 corner
    cube[39]*729+ cube[32]*27+19,                 //index 19 edge
    cube[42]*19683+ cube[35]*729+cube[45]*27+20,  //index 20 corner
    cube[7]*729+ cube[37]*27+21,                  //index 21 edge
    0,                                            //index 22
    cube[43]*729+ cube[46]*27+23,                 //index 23 edge
    cube[8]*19683+ cube[38]*729+  cube[9]*27+24,  //index 24 corner
    cube[41]*729+ cube[12]*27+25,                 //index 25 edge
    cube[44]*19683+cube[15]*729+cube[47]*27+26};   //index 26 corner
    
}
std::unordered_map<MoveFunc, std::string> funcNames = {
    {move_U1, "move_U1"},
    {move_U2, "move_U2"},
    {move_UU, "move_UU"},
    {move_D1, "move_D1"},
    {move_D2, "move_D2"},
    {move_DD, "move_DD"},
    {move_F1, "move_F1"},
    {move_F2, "move_F2"},
    {move_FF, "move_FF"},
    {move_B1, "move_B1"},
    {move_B2, "move_B2"},
    {move_BB, "move_BB"},
    {move_R1, "move_R1"},
    {move_R2, "move_R2"},
    {move_RR, "move_RR"},
    {move_L1, "move_L1"},
    {move_L2, "move_L2"},
    {move_LL, "move_LL"},
    {No_move, "No_move"}
};
//filtered_possibility
std::unordered_map<MoveFunc, std::vector<MoveFunc>> allowedMovesMap{
    {move_U1, {move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_U2, {move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_UU, {move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_D1, {move_UU,move_U2,move_U1,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_D2,{move_UU,move_U2,move_U1,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_DD,{move_UU,move_U2,move_U1,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_F1,{move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_F2,{move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_FF,{move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2}},
    {move_B1, {move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2,move_FF, move_F1, move_F2}},
    {move_B2, {move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2,move_FF, move_F1, move_F2}},
    {move_BB, {move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_LL, move_L2, move_L1,move_RR, move_R1, move_R2,move_FF, move_F1, move_F2}},
    {move_R1,{move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,}},
    {move_R2, {move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,}},
    {move_RR,  {move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,}},
    {move_L1, {move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_RR, move_R1, move_R2}},
    {move_L2, {move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_RR, move_R1, move_R2}},
    {move_LL,{move_U1, move_U2, move_UU,move_DD, move_D1, move_D2,move_B1, move_B2, move_BB,move_FF, move_F1, move_F2,move_RR, move_R1, move_R2}},

};