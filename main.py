import random
while True:   
    grid=[['-','-','-'],['-','-','-'],['-','-','-']]
    while True:
        while True:
            move=int(input())
            if move==1 and grid[0][0]=='-':grid[0][0]='X';break
            if move==2 and grid[0][1]=='-':grid[0][1]='X';break
            if move==3 and grid[0][2]=='-':grid[0][2]='X';break
            if move==4 and grid[1][0]=='-':grid[1][0]='X';break
            if move==5 and grid[1][1]=='-':grid[1][1]='X';break
            if move==6 and grid[1][2]=='-':grid[1][2]='X';break
            if move==7 and grid[2][0]=='-':grid[2][0]='X';break
            if move==8 and grid[2][1]=='-':grid[2][1]='X';break
            if move==9 and grid[2][2]=='-':grid[2][2]='X';break
        if grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[2][0]==grid[1][1]==grid[0][2] and grid[2][0]=='X':print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('You won');break
        elif grid[0].count('-')==0 and grid[1].count('-')==0 and grid[2].count('-')==0:print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2]);print('Draw');break
        while grid[0].count('-')+grid[1].count('-')+grid[2].count('-')!=0:
            if grid[0][0]==grid[0][1] and grid[0][0]=='O' and grid[0][2]=='-':grid[0][2]='O';break
            elif grid[0][0]==grid[0][2] and grid[0][0]=='O' and grid[0][1]=='-':grid[0][1]='O';break
            elif grid[0][1]==grid[0][2] and grid[0][1]=='O' and grid[0][0]=='-':grid[0][0]='O';break
            elif grid[1][0]==grid[1][1] and grid[1][0]=='O' and grid[1][2]=='-':grid[1][2]='O';break
            elif grid[1][0]==grid[1][2] and grid[1][0]=='O' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[1][2] and grid[1][1]=='O' and grid[1][0]=='-':grid[1][0]='O';break
            elif grid[2][0]==grid[2][1] and grid[2][0]=='O' and grid[2][2]=='-':grid[2][2]='O';break
            elif grid[2][0]==grid[2][2] and grid[2][0]=='O' and grid[2][1]=='-':grid[2][1]='O';break
            elif grid[2][1]==grid[2][2] and grid[2][1]=='O' and grid[2][0]=='-':grid[2][0]='O';break
            elif grid[0][0]==grid[1][0] and grid[0][0]=='O' and grid[2][0]=='-':grid[2][0]='O';break
            elif grid[0][0]==grid[2][0] and grid[0][0]=='O' and grid[1][0]=='-':grid[1][0]='O';break
            elif grid[1][0]==grid[2][0] and grid[1][0]=='O' and grid[0][0]=='-':grid[0][0]='O';break
            elif grid[0][1]==grid[1][1] and grid[0][1]=='O' and grid[2][1]=='-':grid[2][1]='O';break
            elif grid[0][1]==grid[2][1] and grid[0][1]=='O' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[2][1] and grid[1][1]=='O' and grid[0][1]=='-':grid[0][1]='O';break
            elif grid[0][2]==grid[1][2] and grid[0][2]=='O' and grid[2][2]=='-':grid[2][2]='O';break
            elif grid[0][2]==grid[2][2] and grid[0][2]=='O' and grid[1][2]=='-':grid[1][2]='O';break
            elif grid[1][2]==grid[2][2] and grid[1][2]=='O' and grid[0][2]=='-':grid[0][2]='O';break
            elif grid[0][0]==grid[1][1] and grid[0][0]=='O' and grid[2][2]=='-':grid[2][2]='O';break
            elif grid[0][0]==grid[2][2] and grid[0][0]=='O' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[2][2] and grid[1][1]=='O' and grid[0][0]=='-':grid[0][0]='O';break
            elif grid[0][2]==grid[1][1] and grid[0][2]=='O' and grid[2][0]=='-':grid[2][0]='O';break
            elif grid[0][2]==grid[2][0] and grid[0][2]=='O' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[2][0] and grid[1][1]=='O' and grid[0][2]=='-':grid[0][2]='O';break
            elif grid[0][0]==grid[0][1] and grid[0][0]=='X' and grid[0][2]=='-':grid[0][2]='O';break
            elif grid[0][0]==grid[0][2] and grid[0][0]=='X' and grid[0][1]=='-':grid[0][1]='O';break
            elif grid[0][1]==grid[0][2] and grid[0][1]=='X' and grid[0][0]=='-':grid[0][0]='O';break
            elif grid[1][0]==grid[1][1] and grid[1][0]=='X' and grid[1][2]=='-':grid[1][2]='O';break
            elif grid[1][0]==grid[1][2] and grid[1][0]=='X' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[1][2] and grid[1][1]=='X' and grid[1][0]=='-':grid[1][0]='O';break
            elif grid[2][0]==grid[2][1] and grid[2][0]=='X' and grid[2][2]=='-':grid[2][2]='O';break
            elif grid[2][0]==grid[2][2] and grid[2][0]=='X' and grid[2][1]=='-':grid[2][1]='O';break
            elif grid[2][1]==grid[2][2] and grid[2][1]=='X' and grid[2][0]=='-':grid[2][0]='O';break
            elif grid[0][0]==grid[1][0] and grid[0][0]=='X' and grid[2][0]=='-':grid[2][0]='O';break
            elif grid[0][0]==grid[2][0] and grid[0][0]=='X' and grid[1][0]=='-':grid[1][0]='O';break
            elif grid[1][0]==grid[2][0] and grid[1][0]=='X' and grid[0][0]=='-':grid[0][0]='O';break
            elif grid[0][1]==grid[1][1] and grid[0][1]=='X' and grid[2][1]=='-':grid[2][1]='O';break
            elif grid[0][1]==grid[2][1] and grid[0][1]=='X' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[2][1] and grid[1][1]=='X' and grid[0][1]=='-':grid[0][1]='O';break
            elif grid[0][2]==grid[1][2] and grid[0][2]=='X' and grid[2][2]=='-':grid[2][2]='O';break
            elif grid[0][2]==grid[2][2] and grid[0][2]=='X' and grid[1][2]=='-':grid[1][2]='O';break
            elif grid[1][2]==grid[2][2] and grid[1][2]=='X' and grid[0][2]=='-':grid[0][2]='O';break
            elif grid[0][0]==grid[1][1] and grid[0][0]=='X' and grid[2][2]=='-':grid[2][2]='O';break
            elif grid[0][0]==grid[2][2] and grid[0][0]=='X' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[2][2] and grid[1][1]=='X' and grid[0][0]=='-':grid[0][0]='O';break
            elif grid[0][2]==grid[1][1] and grid[0][2]=='X' and grid[2][0]=='-':grid[2][0]='O';break
            elif grid[0][2]==grid[2][0] and grid[0][2]=='X' and grid[1][1]=='-':grid[1][1]='O';break
            elif grid[1][1]==grid[2][0] and grid[1][1]=='X' and grid[0][2]=='-':grid[0][2]='O';break
            else:
                if grid[0]==['X','-','-'] and grid[1]==['-','O','-'] and grid[2]==['-','-','X']:grid[0][1]='O';break
                elif grid[0]==['-','-','X'] and grid[1]==['-','O','-'] and grid[2]==['X','-','-']:grid[0][1]='O';break
                elif grid[1][1]=='-':grid[1][1]='O';break
                elif grid[0][0]=='-':grid[0][0]='O';break
                elif grid[0][2]=='-':grid[0][2]='O';break
                elif grid[2][0]=='-':grid[2][0]='O';break
                elif grid[2][2]=='-':grid[2][2]='O';break
                else:
                    move=random.randint(2,8)
                    if move==2 and grid[0][1]=='-':l=0;grid[0][1]='O';break
                    if move==4 and grid[1][0]=='-':l=0;grid[1][0]='O';break
                    if move==5 and grid[1][1]=='-':l=0;grid[1][1]='O';break
                    if move==6 and grid[1][2]=='-':l=0;grid[1][2]='O';break
                    if move==8 and grid[2][1]=='-':l=0;grid[2][1]='O';break
        print(grid[0][0],end=' ');print(grid[0][1],end=' ');print(grid[0][2]);print(grid[1][0],end=' ');print(grid[1][1],end=' ');print(grid[1][2]);print(grid[2][0],end=' ');print(grid[2][1],end=' ');print(grid[2][2])
        if grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]=='O':print('You lost');break
        elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]=='O':print('You lost');break
        elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]=='O':print('You lost');break
        elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]=='O':print('You lost');break
        elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]=='O':print('You lost');break
        elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]=='O':print('You lost');break
        elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]=='O':print('You lost');break
        elif grid[2][0]==grid[1][1]==grid[0][2] and grid[2][0]=='O':print('You lost');break
