while True:
    g=[['-','-','-'],['-','-','-'],['-','-','-']]
    while True:
        m=int(input("Enter position in which you want to place X (1-9): "))
        while(m<1 or m>9 or g[(m-1)//3][(m-1)%3]!='-'):m=int(input("Enter position in which you want to place X (1-9): "))
        g[(m-1)//3][(m-1)%3]='X'
        if((g[0][0]==g[0][1]==g[0][2] and g[0][0]=='O') or (g[1][0]==g[1][1]==g[1][2] and g[1][0]=='O') or (g[2][0]==g[2][1]==g[2][2] and g[2][0]=='O') or (g[0][0]==g[1][0]==g[2][0] and g[0][0]=='O') or (g[0][1]==g[1][1]==g[2][1] and g[0][1]=='O') or ( g[0][2]==g[1][2]==g[2][2] and g[0][2]=='O') or (g[0][0]==g[1][1]==g[2][2] and g[0][0]=='O') or (g[2][0]==g[1][1]==g[0][2] and g[2][0]=='O')):print('Loss');break
        elif((g[0][0]==g[0][1]==g[0][2] and g[0][0]=='X') or (g[1][0]==g[1][1]==g[1][2] and g[1][0]=='X') or (g[2][0]==g[2][1]==g[2][2] and g[2][0]=='X') or (g[0][0]==g[1][0]==g[2][0] and g[0][0]=='X') or (g[0][1]==g[1][1]==g[2][1] and g[0][1]=='X') or ( g[0][2]==g[1][2]==g[2][2] and g[0][2]=='X') or (g[0][0]==g[1][1]==g[2][2] and g[0][0]=='X') or (g[2][0]==g[1][1]==g[0][2] and g[2][0]=='X')):print('Win');break
        elif(g[0].count('-')==0 and g[1].count('-')==0 and g[2].count('-')==0):print('Draw');break
        while True:
            if g[0][0]==g[0][1] and g[0][0]=='O' and g[0][2]=='-':g[0][2]='O';break
            elif g[0][0]==g[0][2] and g[0][0]=='O' and g[0][1]=='-':g[0][1]='O';break
            elif g[0][1]==g[0][2] and g[0][1]=='O' and g[0][0]=='-':g[0][0]='O';break
            elif g[1][0]==g[1][1] and g[1][0]=='O' and g[1][2]=='-':g[1][2]='O';break
            elif g[1][0]==g[1][2] and g[1][0]=='O' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[1][2] and g[1][1]=='O' and g[1][0]=='-':g[1][0]='O';break
            elif g[2][0]==g[2][1] and g[2][0]=='O' and g[2][2]=='-':g[2][2]='O';break
            elif g[2][0]==g[2][2] and g[2][0]=='O' and g[2][1]=='-':g[2][1]='O';break
            elif g[2][1]==g[2][2] and g[2][1]=='O' and g[2][0]=='-':g[2][0]='O';break
            elif g[0][0]==g[1][0] and g[0][0]=='O' and g[2][0]=='-':g[2][0]='O';break
            elif g[0][0]==g[2][0] and g[0][0]=='O' and g[1][0]=='-':g[1][0]='O';break
            elif g[1][0]==g[2][0] and g[1][0]=='O' and g[0][0]=='-':g[0][0]='O';break
            elif g[0][1]==g[1][1] and g[0][1]=='O' and g[2][1]=='-':g[2][1]='O';break
            elif g[0][1]==g[2][1] and g[0][1]=='O' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[2][1] and g[1][1]=='O' and g[0][1]=='-':g[0][1]='O';break
            elif g[0][2]==g[1][2] and g[0][2]=='O' and g[2][2]=='-':g[2][2]='O';break
            elif g[0][2]==g[2][2] and g[0][2]=='O' and g[1][2]=='-':g[1][2]='O';break
            elif g[1][2]==g[2][2] and g[1][2]=='O' and g[0][2]=='-':g[0][2]='O';break
            elif g[0][0]==g[1][1] and g[0][0]=='O' and g[2][2]=='-':g[2][2]='O';break
            elif g[0][0]==g[2][2] and g[0][0]=='O' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[2][2] and g[1][1]=='O' and g[0][0]=='-':g[0][0]='O';break
            elif g[0][2]==g[1][1] and g[0][2]=='O' and g[2][0]=='-':g[2][0]='O';break
            elif g[0][2]==g[2][0] and g[0][2]=='O' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[2][0] and g[1][1]=='O' and g[0][2]=='-':g[0][2]='O';break
            elif g[0][0]==g[0][1] and g[0][0]=='X' and g[0][2]=='-':g[0][2]='O';break
            elif g[0][0]==g[0][2] and g[0][0]=='X' and g[0][1]=='-':g[0][1]='O';break
            elif g[0][1]==g[0][2] and g[0][1]=='X' and g[0][0]=='-':g[0][0]='O';break
            elif g[1][0]==g[1][1] and g[1][0]=='X' and g[1][2]=='-':g[1][2]='O';break
            elif g[1][0]==g[1][2] and g[1][0]=='X' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[1][2] and g[1][1]=='X' and g[1][0]=='-':g[1][0]='O';break
            elif g[2][0]==g[2][1] and g[2][0]=='X' and g[2][2]=='-':g[2][2]='O';break
            elif g[2][0]==g[2][2] and g[2][0]=='X' and g[2][1]=='-':g[2][1]='O';break
            elif g[2][1]==g[2][2] and g[2][1]=='X' and g[2][0]=='-':g[2][0]='O';break
            elif g[0][0]==g[1][0] and g[0][0]=='X' and g[2][0]=='-':g[2][0]='O';break
            elif g[0][0]==g[2][0] and g[0][0]=='X' and g[1][0]=='-':g[1][0]='O';break
            elif g[1][0]==g[2][0] and g[1][0]=='X' and g[0][0]=='-':g[0][0]='O';break
            elif g[0][1]==g[1][1] and g[0][1]=='X' and g[2][1]=='-':g[2][1]='O';break
            elif g[0][1]==g[2][1] and g[0][1]=='X' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[2][1] and g[1][1]=='X' and g[0][1]=='-':g[0][1]='O';break
            elif g[0][2]==g[1][2] and g[0][2]=='X' and g[2][2]=='-':g[2][2]='O';break
            elif g[0][2]==g[2][2] and g[0][2]=='X' and g[1][2]=='-':g[1][2]='O';break
            elif g[1][2]==g[2][2] and g[1][2]=='X' and g[0][2]=='-':g[0][2]='O';break
            elif g[0][0]==g[1][1] and g[0][0]=='X' and g[2][2]=='-':g[2][2]='O';break
            elif g[0][0]==g[2][2] and g[0][0]=='X' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[2][2] and g[1][1]=='X' and g[0][0]=='-':g[0][0]='O';break
            elif g[0][2]==g[1][1] and g[0][2]=='X' and g[2][0]=='-':g[2][0]='O';break
            elif g[0][2]==g[2][0] and g[0][2]=='X' and g[1][1]=='-':g[1][1]='O';break
            elif g[1][1]==g[2][0] and g[1][1]=='X' and g[0][2]=='-':g[0][2]='O';break
            else:
                if g[0]==['X','-','-'] and g[1]==['-','O','-'] and g[2]==['-','-','X']:g[0][1]='O';break
                elif g[0]==['-','-','X'] and g[1]==['-','O','-'] and g[2]==['X','-','-']:g[0][1]='O';break
                elif g[0]==['X','-','-'] and g[1]==['-','O','-'] and g[2]==['-','X','-']:g[1][0]='O';break
                elif g[0]==['-','-','-'] and g[1]==['-','O','X'] and g[2]==['X','-','-']:g[0][1]='O';break
                elif g[0]==['-','-','X'] and g[1]==['-','O','-'] and g[2]==['-','X','-']:g[1][0]='O';break
                elif g[1][1]=='-':g[1][1]='O';break
                elif g[0][0]=='-':g[0][0]='O';break
                elif g[0][2]=='-':g[0][2]='O';break
                elif g[2][0]=='-':g[2][0]='O';break
                elif g[2][2]=='-':g[2][2]='O';break
                else:
                    if g[0][1]=='-':g[0][1]='O';break
                    if g[1][0]=='-':g[1][0]='O';break
                    if g[1][1]=='-':g[1][1]='O';break
                    if g[1][2]=='-':g[1][2]='O';break
                    if g[2][1]=='-':g[2][1]='O';break
        for i in range(1,10):
            if((i-1)%3!=2):print(g[(i-1)//3][(i-1)%3],end=' ')
            else:print(g[(i-1)//3][(i-1)%3])
        if((g[0][0]==g[0][1]==g[0][2] and g[0][0]=='O') or (g[1][0]==g[1][1]==g[1][2] and g[1][0]=='O') or (g[2][0]==g[2][1]==g[2][2] and g[2][0]=='O') or (g[0][0]==g[1][0]==g[2][0] and g[0][0]=='O') or (g[0][1]==g[1][1]==g[2][1] and g[0][1]=='O') or ( g[0][2]==g[1][2]==g[2][2] and g[0][2]=='O') or (g[0][0]==g[1][1]==g[2][2] and g[0][0]=='O') or (g[2][0]==g[1][1]==g[0][2] and g[2][0]=='O')):print('Loss');break
        elif((g[0][0]==g[0][1]==g[0][2] and g[0][0]=='X') or (g[1][0]==g[1][1]==g[1][2] and g[1][0]=='X') or (g[2][0]==g[2][1]==g[2][2] and g[2][0]=='X') or (g[0][0]==g[1][0]==g[2][0] and g[0][0]=='X') or (g[0][1]==g[1][1]==g[2][1] and g[0][1]=='X') or ( g[0][2]==g[1][2]==g[2][2] and g[0][2]=='X') or (g[0][0]==g[1][1]==g[2][2] and g[0][0]=='X') or (g[2][0]==g[1][1]==g[0][2] and g[2][0]=='X')):print('Win');break
