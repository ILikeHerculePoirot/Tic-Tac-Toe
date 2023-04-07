import random
g=1;l=0;h=0
grid=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]
while g==1:
    while h==0:
        move=int(input())
        if move==1 and grid[0][0]=='-':grid[0][0]='X';h=1
        if move==2 and grid[0][1]=='-':grid[0][1]='X';h=1
        if move==3 and grid[0][2]=='-':grid[0][2]='X';h=1
        if move==4 and grid[1][0]=='-':grid[1][0]='X';h=1
        if move==5 and grid[1][1]=='-':grid[1][1]='X';h=1
        if move==6 and grid[1][2]=='-':grid[1][2]='X';h=1
        if move==7 and grid[2][0]=='-':grid[2][0]='X';h=1
        if move==8 and grid[2][1]=='-':grid[2][1]='X';h=1
        if move==9 and grid[2][2]=='-':grid[2][2]='X';h=1
    while l==0:
        move=random.randint(1,9)
        if move==1 and grid[0][0]=="-":l=0;grid[0][0]='O';l=1
        if move==2 and grid[0][1]=="-":l=0;grid[0][1]='O';l=1
        if move==3 and grid[0][2]=="-":l=0;grid[0][2]='O';l=1
        if move==4 and grid[1][0]=="-":l=0;grid[1][0]='O';l=1
        if move==5 and grid[1][1]=="-":l=0;grid[1][1]='O';l=1
        if move==6 and grid[1][2]=="-":l=0;grid[1][2]='O';l=1
        if move==7 and grid[2][0]=="-":l=0;grid[2][0]='O';l=1
        if move==8 and grid[2][1]=="-":l=0;grid[2][1]='O';l=1
        if move==9 and grid[2][2]=="-":l=0;grid[2][2]='O';l=1
    l=0;h=0;print(grid[0][0],end=" ");print(grid[0][1],end=" ");print(grid[0][2]);print(grid[1][0],end=" ");print(grid[1][1],end=" ");print(grid[1][2]);print(grid[2][0],end=" ");print(grid[2][1],end=" ");print(grid[2][2])
    if grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]=="X":print("You won");g=0
    elif grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]=="O":print("You lost");g=0
    elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]=="X":print("You won");g=0
    elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]=="O":print("You lost");g=0
    elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]=="X":print("You won");g=0
    elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]=="O":print("You lost");g=0
    elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]=="X":print("You won");g=0
    elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]=="O":print("You lost");g=0
    elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]=="X":print("You won");g=0
    elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]=="O":print("You lost");g=0
    elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]=="X":print("You won");g=0
    elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]=="O":print("You lost");g=0
    elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]=="X":print("You won");g=0
    elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]=="O":print("You lost");g=0
    elif grid[2][0]==grid[1][1]==grid[0][2] and grid[2][0]=="X":print("You won");g=0
    elif grid[2][0]==grid[1][1]==grid[0][2] and grid[2][0]=="O":print("You lost");g=0
    elif grid[0].count('-')==0 and grid[1].count('-')==0 and grid[2].count('-')==0:print("It was a draw");g=0
