#бібліотеки
from time import sleep
from xml.etree.ElementTree import XMLParser

#поле гравця 1

line_0_p1=['0','1','2','3','4','5','6','7','8','9','10']
line_1_p1=['1','_','_','_','_','_','_','_','_','_','_']
line_2_p1=['2','_','_','_','_','_','_','_','_','_','_']
line_3_p1=['3','_','_','_','_','_','_','_','_','_','_']
line_4_p1=['4','_','_','_','_','_','_','_','_','_','_']
line_5_p1=['5','_','_','_','_','_','_','_','_','_','_']
line_6_p1=['6','_','_','_','_','_','_','_','_','_','_']
line_7_p1=['7','_','_','_','_','_','_','_','_','_','_']
line_8_p1=['8','_','_','_','_','_','_','_','_','_','_']
line_9_p1=['9','_','_','_','_','_','_','_','_','_','_']
line_10_p1=['10','_','_','_','_','_','_','_','_','_','_']

#оле битви гравця 1

line_0_p1b=['0','1','2','3','4','5','6','7','8','9','10']
line_1_p1b=['1','_','_','_','_','_','_','_','_','_','_']
line_2_p1b=['2','_','_','_','_','_','_','_','_','_','_']
line_3_p1b=['3','_','_','_','_','_','_','_','_','_','_']
line_4_p1b=['4','_','_','_','_','_','_','_','_','_','_']
line_5_p1b=['5','_','_','_','_','_','_','_','_','_','_']
line_6_p1b=['6','_','_','_','_','_','_','_','_','_','_']
line_7_p1b=['7','_','_','_','_','_','_','_','_','_','_']
line_8_p1b=['8','_','_','_','_','_','_','_','_','_','_']
line_9_p1b=['9','_','_','_','_','_','_','_','_','_','_']
line_10_p1b=['10','_','_','_','_','_','_','_','_','_','_']

#поле гравця 2

line_0_p2=['0','1','2','3','4','5','6','7','8','9','10']
line_1_p2=['1','_','_','_','_','_','_','_','_','_','_']
line_2_p2=['2','_','_','_','_','_','_','_','_','_','_']
line_3_p2=['3','_','_','_','_','_','_','_','_','_','_']
line_4_p2=['4','_','_','_','_','_','_','_','_','_','_']
line_5_p2=['5','_','_','_','_','_','_','_','_','_','_']
line_6_p2=['6','_','_','_','_','_','_','_','_','_','_']
line_7_p2=['7','_','_','_','_','_','_','_','_','_','_']
line_8_p2=['8','_','_','_','_','_','_','_','_','_','_']
line_9_p2=['9','_','_','_','_','_','_','_','_','_','_']
line_10_p2=['10','_','_','_','_','_','_','_','_','_','_']

#поле битви гравця 2

line_0_p2b=['0','1','2','3','4','5','6','7','8','9','10']
line_1_p2b=['1','_','_','_','_','_','_','_','_','_','_']
line_2_p2b=['2','_','_','_','_','_','_','_','_','_','_']
line_3_p2b=['3','_','_','_','_','_','_','_','_','_','_']
line_4_p2b=['4','_','_','_','_','_','_','_','_','_','_']
line_5_p2b=['5','_','_','_','_','_','_','_','_','_','_']
line_6_p2b=['6','_','_','_','_','_','_','_','_','_','_']
line_7_p2b=['7','_','_','_','_','_','_','_','_','_','_']
line_8_p2b=['8','_','_','_','_','_','_','_','_','_','_']
line_9_p2b=['9','_','_','_','_','_','_','_','_','_','_']
line_10_p2b=['10','_','_','_','_','_','_','_','_','_','_']

#деф функції
def lines_print(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10):
    for i in (l0):
        print(i,end=' ')
    print()
    for i in (l1):
        print(i,end=' ')
    print()
    for i in (l2):
        print(i,end=' ')
    print()
    for i in (l3):
        print(i,end=' ')
    print()
    for i in (l4):
        print(i,end=' ')
    print()
    for i in (l5):
        print(i,end=' ')
    print()
    for i in (l6):
        print(i,end=' ')
    print()
    for i in (l7):
        print(i,end=' ')
    print()
    for i in (l8):
        print(i,end=' ')
    print()
    for i in (l9):
        print(i,end=' ')
    print()
    for i in (l10):
        print(i,end=' ')
    print()

def test_dr_fl_pl1(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,ty,tx):
    #l1
    if (ty==1):
        if (l1[tx]=='_'):
            if (tx==1):
                if (l1[2]=='_'):
                    if (l2[1]=='_'and l2[2]=='_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0

            elif(tx==10):
                if (l1[9]=='_'):
                    if (l2[10]=='_'and l2[9]=='_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0

            else:
                if (l1[tx-1]=='_'and l1[tx+1]=='_'):
                    if (l2[tx]=='_' and l2[tx-1]=='_'and l2[tx+1]=='_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0

        else:
            return 0
    #l2
    elif(ty==2):
        if (tx==1):
            if (l2[1]=='_'and l2[2]=='_'):
                if(l1[1]=='_'and l1[2]=='_'):
                    if (l3[1]=='_'and l3[2]=='_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif(tx==10):
            if (l2[10]=='_' and l2[9]=='_'):
                if(l1[9]=='_'and l1[10]=='_'):
                    if(l3[9]=="-"and l3[10]=='_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l2[tx-1]=='_' and l2[tx]=='_' and l2[tx+1]=='_'):
                if (l1[tx-1]=='_' and l1[tx]=='_' and l1[tx+1]=='_'):
                    if (l3[tx - 1] == '_' and l3[tx] == '_' and l3[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    #l3
    elif(ty==3):
        if (tx == 1):
            if (l3[1] == '_' and l3[2] == '_'):
                if (l2[1] == '_' and l2[2] == '_'):
                    if (l4[1] == '_' and l4[2] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif (tx == 10):
            if (l3[10] == '_' and l3[9] == '_'):
                if (l2[9] == '_' and l2[10] == '_'):
                    if (l4[9] == "-" and l4[10] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l3[tx - 1] == '_' and l3[tx] == '_' and l3[tx + 1] == '_'):
                if (l2[tx - 1] == '_' and l2[tx] == '_' and l2[tx + 1] == '_'):
                    if (l4[tx - 1] == '_' and l4[tx] == '_' and l4[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    # l4
    elif (ty == 4):
        if (tx == 1):
            if (l4[1] == '_' and l4[2] == '_'):
                if (l3[1] == '_' and l3[2] == '_'):
                    if (l5[1] == '_' and l5[2] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif (tx == 10):
            if (l4[10] == '_' and l4[9] == '_'):
                if (l3[9] == '_' and l3[10] == '_'):
                    if (l5[9] == "-" and l5[10] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l4[tx - 1] == '_' and l4[tx] == '_' and l4[tx + 1] == '_'):
                if (l3[tx - 1] == '_' and l3[tx] == '_' and l3[tx + 1] == '_'):
                    if (l5[tx - 1] == '_' and l5[tx] == '_' and l5[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    # l5
    elif (ty == 5):
        if (tx == 1):
            if (l5[1] == '_' and l5[2] == '_'):
                if (l4[1] == '_' and l4[2] == '_'):
                    if (l6[1] == '_' and l6[2] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif (tx == 10):
            if (l5[10] == '_' and l5[9] == '_'):
                if (l4[9] == '_' and l4[10] == '_'):
                    if (l6[9] == "-" and l6[10] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l5[tx - 1] == '_' and l5[tx] == '_' and l5[tx + 1] == '_'):
                if (l4[tx - 1] == '_' and l4[tx] == '_' and l4[tx + 1] == '_'):
                    if (l6[tx - 1] == '_' and l6[tx] == '_' and l6[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    # l6
    elif (ty == 6):
        if (tx == 1):
            if (l6[1] == '_' and l6[2] == '_'):
                if (l5[1] == '_' and l5[2] == '_'):
                    if (l7[1] == '_' and l7[2] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif (tx == 10):
            if (l6[10] == '_' and l6[9] == '_'):
                if (l5[9] == '_' and l5[10] == '_'):
                    if (l7[9] == "-" and l7[10] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l6[tx - 1] == '_' and l6[tx] == '_' and l6[tx + 1] == '_'):
                if (l5[tx - 1] == '_' and l5[tx] == '_' and l5[tx + 1] == '_'):
                    if (l7[tx - 1] == '_' and l7[tx] == '_' and l7[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    # l7
    elif (ty == 7):
        if (tx == 1):
            if (l7[1] == '_' and l7[2] == '_'):
                if (l6[1] == '_' and l6[2] == '_'):
                    if (l8[1] == '_' and l8[2] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif (tx == 10):
            if (l7[10] == '_' and l7[9] == '_'):
                if (l6[9] == '_' and l6[10] == '_'):
                    if (l8[9] == "_" and l8[10] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l7[tx - 1] == '_' and l7[tx] == '_' and l7[tx + 1] == '_'):
                if (l6[tx - 1] == '_' and l6[tx] == '_' and l6[tx + 1] == '_'):
                    if (l8[tx - 1] == '_' and l8[tx] == '_' and l8[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    # l8
    elif (ty == 8):
        if (tx == 1):
            if (l8[1] == '_' and l8[2] == '_'):
                if (l7[1] == '_' and l7[2] == '_'):
                    if (l9[1] == '_' and l9[2] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif (tx == 10):
            if (l8[10] == '_' and l8[9] == '_'):
                if (l7[9] == '_' and l7[10] == '_'):
                    if (l9[9] == "-" and l9[10] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l8[tx - 1] == '_' and l8[tx] == '_' and l8[tx + 1] == '_'):
                if (l7[tx - 1] == '_' and l7[tx] == '_' and l7[tx + 1] == '_'):
                    if (l9[tx - 1] == '_' and l9[tx] == '_' and l9[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    # l9
    elif (ty == 9):
        if (tx == 1):
            if (l9[1] == '_' and l9[2] == '_'):
                if (l8[1] == '_' and l8[2] == '_'):
                    if (l10[1] == '_' and l10[2] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif (tx == 10):
            if (l9[10] == '_' and l9[9] == '_'):
                if (l8[9] == '_' and l8[10] == '_'):
                    if (l10[9] == "-" and l10[10] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            if (l9[tx - 1] == '_' and l9[tx] == '_' and l9[tx + 1] == '_'):
                if (l8[tx - 1] == '_' and l8[tx] == '_' and l8[tx + 1] == '_'):
                    if (l10[tx - 1] == '_' and l10[tx] == '_' and l10[tx + 1] == '_'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    #l10
    elif(ty==10):
        if (tx==1):
            if(l10[1]=='_'and l10[2]=='_'):
                if (l9[1]=='_'and l9[2]=='_'):
                    return 1
                else:
                    return 0
            return 0
        elif(tx==10):
            if (l10[10] == '_' and l10[9] == '_'):
                if (l9[10] == '_' and l9[9] == '_'):
                    return 1
                else:
                    return 0
            return 0
        else:
            if(l10[tx-1]=='_'and l10[tx]=='_'and l10[tx+1]=='_'):
                if (l9[tx - 1] == '_' and l9[tx] == '_' and l9[tx + 1] == '_'):
                    return 1
                else:
                    return 0
            else:
                return 0
def fill(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,p):
    pal4=12

    while True:
        print(p,' в вас залишилося',pal4)
        if (pal4==0):
            break
        else:
            lines_print(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10)
            print(p,'виберіть кординати y та x в які хочете поставити корабиль')
            while True:
                try:
                    y,x=map(int,input().split(' '))
                    if(test_dr_fl_pl1(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,y,x)==1):
                        break
                    else:
                        print('тут не можна поставити ')
                except ValueError:
                    print('потрібно цифрами')
            if (y==1):
                l1[x]='@'
            elif(y==2):
                l2[x]='@'
            elif (y == 3):
                l3[x]='@'
            elif (y == 4):
                l4[x]='@'
            elif (y == 5):
                l5[x]='@'
            elif (y == 6):
                l6[x]='@'
            elif (y == 7):
                l7[x]='@'
            elif (y == 8):
                l8[x]='@'
            elif (y == 9):
                l9[x]='@'
            elif (y == 10):
                l10[x]='@'
            lines_print(l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10)
            pal4-=1
def battel_test(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,ty,tx):
    if (ty==1):
        if (l1[tx]=='_'):
            return 1
        elif(l1[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==2):
        if (l2[tx]=='_'):
            return 1
        elif(l2[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==3):
        if (l3[tx]=='_'):
            return 1
        elif(l3[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==4):
        if (l4[tx]=='_'):
            return 1
        elif(l4[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==5):
        if (l5[tx]=='_'):
            return 1
        elif(l5[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==6):
        if (l6[tx]=='_'):
            return 1
        elif(l6[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==7):
        if (l7[tx]=='_'):
            return 1
        elif(l7[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==8):
        if (l8[tx]=='_'):
            return 1
        elif(l8[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==9):
        if (l9[tx]=='_'):
            return 1
        elif(l9[tx]=='@'):
            return 2
        else:
            return 0
    elif (ty==10):
        if (l10[tx]=='_'):
            return 1
        elif(l10[tx]=='@'):
            return 2
        else:
            return 0

def battel(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l0b,l1b,l2b,l3b,l4b,l5b,l6b,l7b,l8b,l9b,l10b,p,lf):
    print(p,'введіть y та x кординати пострілу')
    while True:
        try:
            y,x=map(int,input().split(' '))
            is_hit=battel_test(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,y,x)
            if (is_hit==0):
                print('ця клітинка вже знищена')
            else:
                break
        except ValueError:
            print('введеня має виконуватися цифрами')
    if (is_hit==1):
        print(p, 'непопав')
        if(y==1):
            l1[x]='#'
            l1b[x] = '#'
        elif (y == 2):
            l2[x]='#'
            l2b[x] = '#'
        elif (y == 3):
            l3[x] = '#'
            l3b[x] = '#'
        elif (y == 4):
            l4[x] = '#'
            l4b[x] = '#'
        elif (y == 5):
            l5[x] ='#'
            l5b[x] = '#'
        elif (y == 6):
            l6[x] ='#'
            l6b[x] = '#'
        elif (y == 7):
            l7[x] = '#'
            l7b[x] = '#'
        elif (y == 8):
            l8[x] = '#'
            l8b[x] = '#'
        elif (y == 9):
            l9[x] = '#'
            l9b[x] = '#'
        elif (y == 10):
            l10[x]= '#'
            l10b[x] = '#'
    elif(is_hit==2):
        lf-=1
        if (y==1):
            if (x==1):
                l1[1]='X'
                l1[2]='#'
                l2[1] = '#'
                l2[2] = '#'
            elif(x==10):
                l1[10] = 'X'
                l1[9] = '#'
                l2[10] = '#'
                l2[9] = '#'
            else:
                l1[x]='X'
                l1[x-1]='#'
                l1[x+1]='#'
                l2[x] = '#'
                l2[x - 1] = '#'
                l2[x + 1] = '#'
        elif(y==2):
            if(x==1):
                l2[1]='X'
                l2[2]='#'
                l1[1] = '#'
                l1[2] = '#'
                l3[1] = '#'
                l3[2] = '#'
            elif (x == 10):
                l2[10] = 'X'
                l2[9] = '#'
                l1[10] = '#'
                l1[9] = '#'
                l3[10] = '#'
                l3[9] = '#'
            else:
                l2[x]='X'
                l2[x-1]='#'
                l2[x+1]='#'
                l1[x] = '#'
                l1[x - 1] = '#'
                l1[x + 1] = '#'
                l3[x] = '#'
                l3[x - 1] = '#'
                l3[x + 1] = '#'
        elif (y == 3):
            if (x == 1):
                l3[1] = 'X'
                l3[2] = '#'
                l2[1] = '#'
                l2[2] = '#'
                l4[1] = '#'
                l4[2] = '#'
            elif (x == 10):
                l3[10] = 'X'
                l3[9] = '#'
                l2[10] = '#'
                l2[9] = '#'
                l4[10] = '#'
                l4[9] = '#'
            else:
                l3[x] = 'X'
                l3[x - 1] = '#'
                l3[x + 1] = '#'
                l2[x] = '#'
                l2[x - 1] = '#'
                l2[x + 1] = '#'
                l4[x] = '#'
                l4[x - 1] = '#'
                l4[x + 1] = '#'
        elif (y == 4):
            if (x == 1):
                l4[1] = 'X'
                l4[2] = '#'
                l3[1] = '#'
                l3[2] = '#'
                l5[1] = '#'
                l5[2] = '#'
            elif (x == 10):
                l4[10] = 'X'
                l4[9] = '#'
                l3[10] = '#'
                l3[9] = '#'
                l5[10] = '#'
                l5[9] = '#'
            else:
                l4[x] = 'X'
                l4[x - 1] = '#'
                l4[x + 1] = '#'
                l3[x] = '#'
                l3[x - 1] = '#'
                l3[x + 1] = '#'
                l5[x] = '#'
                l5[x - 1] = '#'
                l5[x + 1] = '#'
        elif (y == 5):
            if (x == 1):
                l5[1] = 'X'
                l5[2] = '#'
                l4[1] = '#'
                l4[2] = '#'
                l6[1] = '#'
                l6[2] = '#'
            elif (x == 10):
                l5[10] = 'X'
                l5[9] = '#'
                l4[10] = '#'
                l4[9] = '#'
                l6[10] = '#'
                l6[9] = '#'
            else:
                l5[x] = 'X'
                l5[x - 1] = '#'
                l5[x + 1] = '#'
                l4[x] = '#'
                l4[x - 1] = '#'
                l4[x + 1] = '#'
                l6[x] = '#'
                l6[x - 1] = '#'
                l6[x + 1] = '#'
        elif (y == 6):
            if (x == 1):
                l6[1] = 'X'
                l6[2] = '#'
                l5[1] = '#'
                l5[2] = '#'
                l7[1] = '#'
                l7[2] = '#'
            elif (x == 10):
                l6[10] = 'X'
                l6[9] = '#'
                l5[10] = '#'
                l5[9] = '#'
                l7[10] = '#'
                l7[9] = '#'
            else:
                l6[x] = 'X'
                l6[x - 1] = '#'
                l6[x + 1] = '#'
                l5[x] = '#'
                l5[x - 1] = '#'
                l5[x + 1] = '#'
                l7[x] = '#'
                l7[x - 1] = '#'
                l7[x + 1] = '#'
        elif (y == 7):
            if (x == 1):
                l7[1] = 'X'
                l7[2] = '#'
                l6[1] = '#'
                l6[2] = '#'
                l8[1] = '#'
                l8[2] = '#'
            elif (x == 10):
                l7[10] = 'X'
                l7[9] = '#'
                l6[10] = '#'
                l6[9] = '#'
                l8[10] = '#'
                l8[9] = '#'
            else:
                l7[x] = 'X'
                l7[x - 1] = '#'
                l7[x + 1] = '#'
                l6[x] = '#'
                l6[x - 1] = '#'
                l6[x + 1] = '#'
                l8[x] = '#'
                l8[x - 1] = '#'
                l8[x + 1] = '#'
        elif (y == 2):
            if (x == 1):
                l8[1] = 'X'
                l8[2] = '#'
                l7[1] = '#'
                l7[2] = '#'
                l9[1] = '#'
                l9[2] = '#'
            elif (x == 10):
                l8[10] = 'X'
                l8[9] = '#'
                l7[10] = '#'
                l7[9] = '#'
                l9[10] = '#'
                l9[9] = '#'
            else:
                l8[x] = 'X'
                l8[x - 1] = '#'
                l8[x + 1] = '#'
                l7[x] = '#'
                l7[x - 1] = '#'
                l7[x + 1] = '#'
                l9[x] = '#'
                l9[x - 1] = '#'
                l9[x + 1] = '#'
        elif (y == 9):
            if (x == 1):
                l9[1] = 'X'
                l9[2] = '#'
                l8[1] = '#'
                l8[2] = '#'
                l10[1] = '#'
                l10[2] = '#'
            elif (x == 10):
                l9[10] = 'X'
                l9[9] = '#'
                l8[10] = '#'
                l8[9] = '#'
                l10[10] = '#'
                l10[9] = '#'
            else:
                l9[x] = 'X'
                l9[x - 1] = '#'
                l9[x + 1] = '#'
                l8[x] = '#'
                l8[x - 1] = '#'
                l8[x + 1] = '#'
                l10[x] = '#'
                l10[x - 1] = '#'
                l10[x + 1] = '#'
        elif(y==10):
            if(x==1):
                l10[1]='X'
                l10[2]='#'
                l9[1]='#'
                l9[2]='#'
            elif(x==10):
                l10[10] = 'X'
                l10[9] = '#'
                l9[10] = '#'
                l9[9] = '#'
            else:
                l10[x]='X'
                l10[x-1]='#'
                l10[x+1]='#'
                l9[x] = '#'
                l9[x - 1] = '#'
                l9[x + 1] = '#'
    if(is_hit==2):
        print(p,'попав')
        if (y==1):
            if (x==1):
                l1b[1]='X'
                l1b[2]='#'
                l2b[1] = '#'
                l2b[2] = '#'
            elif(x==10):
                l1b[10] = 'X'
                l1b[9] = '#'
                l2b[10] = '#'
                l2b[9] = '#'
            else:
                l1b[x]='X'
                l1b[x-1]='#'
                l1b[x+1]='#'
                l2b[x] = '#'
                l2b[x - 1] = '#'
                l2b[x + 1] = '#'
        elif(y==2):
            if(x==1):
                l2b[1]='X'
                l2b[2]='#'
                l1b[1] = '#'
                l1b[2] = '#'
                l3b[1] = '#'
                l3b[2] = '#'
            elif (x == 10):
                l2b[10] = 'X'
                l2b[9] = '#'
                l1b[10] = '#'
                l1b[9] = '#'
                l3b[10] = '#'
                l3b[9] = '#'
            else:
                l2b[x]='X'
                l2b[x-1]='#'
                l2b[x+1]='#'
                l1b[x] = '#'
                l1b[x - 1] = '#'
                l1b[x + 1] = '#'
                l3b[x] = '#'
                l3b[x - 1] = '#'
                l3b[x + 1] = '#'
        elif (y == 3):
            if (x == 1):
                l3b[1] = 'X'
                l3b[2] = '#'
                l2b[1] = '#'
                l2b[2] = '#'
                l4b[1] = '#'
                l4b[2] = '#'
            elif (x == 10):
                l3b[10] = 'X'
                l3b[9] = '#'
                l2b[10] = '#'
                l2b[9] = '#'
                l4b[10] = '#'
                l4b[9] = '#'
            else:
                l3b[x] = 'X'
                l3b[x - 1] = '#'
                l3b[x + 1] = '#'
                l2b[x] = '#'
                l2b[x - 1] = '#'
                l2b[x + 1] = '#'
                l4b[x] = '#'
                l4b[x - 1] = '#'
                l4b[x + 1] = '#'
        elif (y == 4):
            if (x == 1):
                l4b[1] = 'X'
                l4b[2] = '#'
                l3b[1] = '#'
                l3b[2] = '#'
                l5b[1] = '#'
                l5b[2] = '#'
            elif (x == 10):
                l4b[10] = 'X'
                l4b[9] = '#'
                l3b[10] = '#'
                l3b[9] = '#'
                l5b[10] = '#'
                l5b[9] = '#'
            else:
                l4b[x] = 'X'
                l4b[x - 1] = '#'
                l4b[x + 1] = '#'
                l3b[x] = '#'
                l3b[x - 1] = '#'
                l3b[x + 1] = '#'
                l5b[x] = '#'
                l5b[x - 1] = '#'
                l5b[x + 1] = '#'
        elif (y == 5):
            if (x == 1):
                l5b[1] = 'X'
                l5b[2] = '#'
                l4b[1] = '#'
                l4b[2] = '#'
                l6b[1] = '#'
                l6b[2] = '#'
            elif (x == 10):
                l5b[10] = 'X'
                l5b[9] = '#'
                l4b[10] = '#'
                l4b[9] = '#'
                l6b[10] = '#'
                l6b[9] = '#'
            else:
                l5b[x] = 'X'
                l5b[x - 1] = '#'
                l5b[x + 1] = '#'
                l4b[x] = '#'
                l4b[x - 1] = '#'
                l4b[x + 1] = '#'
                l6b[x] = '#'
                l6b[x - 1] = '#'
                l6b[x + 1] = '#'
        elif (y == 6):
            if (x == 1):
                l6b[1] = 'X'
                l6b[2] = '#'
                l5b[1] = '#'
                l5b[2] = '#'
                l7b[1] = '#'
                l7b[2] = '#'
            elif (x == 10):
                l6b[10] = 'X'
                l6b[9] = '#'
                l5b[10] = '#'
                l5b[9] = '#'
                l7b[10] = '#'
                l7b[9] = '#'
            else:
                l6b[x] = 'X'
                l6b[x - 1] = '#'
                l6b[x + 1] = '#'
                l5b[x] = '#'
                l5b[x - 1] = '#'
                l5b[x + 1] = '#'
                l7b[x] = '#'
                l7b[x - 1] = '#'
                l7b[x + 1] = '#'
        elif (y == 7):
            if (x == 1):
                l7b[1] = 'X'
                l7b[2] = '#'
                l6b[1] = '#'
                l6b[2] = '#'
                l8b[1] = '#'
                l8b[2] = '#'
            elif (x == 10):
                l7b[10] = 'X'
                l7b[9] = '#'
                l6b[10] = '#'
                l6b[9] = '#'
                l8b[10] = '#'
                l8b[9] = '#'
            else:
                l7b[x] = 'X'
                l7b[x - 1] = '#'
                l7b[x + 1] = '#'
                l6b[x] = '#'
                l6b[x - 1] = '#'
                l6b[x + 1] = '#'
                l8b[x] = '#'
                l8b[x - 1] = '#'
                l8b[x + 1] = '#'
        elif (y == 2):
            if (x == 1):
                l8b[1] = 'X'
                l8b[2] = '#'
                l7b[1] = '#'
                l7b[2] = '#'
                l9b[1] = '#'
                l9b[2] = '#'
            elif (x == 10):
                l8b[10] = 'X'
                l8b[9] = '#'
                l7b[10] = '#'
                l7b[9] = '#'
                l9b[10] = '#'
                l9b[9] = '#'
            else:
                l8b[x] = 'X'
                l8b[x - 1] = '#'
                l8b[x + 1] = '#'
                l7b[x] = '#'
                l7b[x - 1] = '#'
                l7b[x + 1] = '#'
                l9b[x] = '#'
                l9b[x - 1] = '#'
                l9b[x + 1] = '#'
        elif (y == 9):
            if (x == 1):
                l9b[1] = 'X'
                l9b[2] = '#'
                l8b[1] = '#'
                l8b[2] = '#'
                l10b[1] = '#'
                l10b[2] = '#'
            elif (x == 10):
                l9b[10] = 'X'
                l9b[9] = '#'
                l8b[10] = '#'
                l8b[9] = '#'
                l10b[10] = '#'
                l10b[9] = '#'
            else:
                l9b[x] = 'X'
                l9b[x - 1] = '#'
                l9b[x + 1] = '#'
                l8b[x] = '#'
                l8b[x - 1] = '#'
                l8b[x + 1] = '#'
                l10b[x] = '#'
                l10b[x - 1] = '#'
                l10b[x + 1] = '#'
        elif(y==10):
            if(x==1):
                l10b[1]='X'
                l10b[2]='#'
                l9b[1]='#'
                l9b[2]='#'
            elif(x==10):
                l10b[10] = 'X'
                l10b[9] = '#'
                l9b[10] = '#'
                l9b[9] = '#'
            else:
                l10b[x]='X'
                l10b[x-1]='#'
                l10b[x+1]='#'
                l9b[x] = '#'
                l9b[x - 1] = '#'
                l9b[x + 1] = '#'

#гра

fl1=12
fl2=12

print('вітаю в моїй авторській грі яка є тро видозміненим морським боєм')
print('в данній грі в двох гравців є 12 однопалубних кораблів')
print('та вистріли по черзі ')
print('інші правила не змінені')
p1_n=input('перший гравець введіть ваше імя')
p2_n=input('другий гравець мені потрібно також ваше імя')
print(p1_n,'ви виставляєте ваші кораблики',p2_n,'не підгядає')
sleep(5)
fill(line_0_p1,line_1_p1,line_2_p1,line_3_p1,line_4_p1,line_5_p1,line_6_p1,line_7_p1,line_8_p1,line_9_p1,line_10_p1,p1_n)
print('\n'*100)
print('тепер ви міняєтеся ролями')
sleep(5)
fill(line_0_p2,line_1_p2,line_2_p2,line_3_p2,line_4_p2,line_5_p2,line_6_p2,line_7_p2,line_8_p2,line_9_p2,line_10_p2,p2_n)
print('\n'*100)
while True:
    lines_print(line_0_p2b, line_1_p2b, line_2_p2b, line_3_p2b, line_4_p2b, line_5_p2b, line_6_p2b, line_7_p2b,line_8_p2b, line_9_p2b, line_10_p2b)
    battel(line_0_p2, line_1_p2, line_2_p2, line_3_p2, line_4_p2, line_5_p2, line_6_p2, line_7_p2, line_8_p2, line_9_p2,line_10_p2, line_0_p2b, line_1_p2b, line_2_p2b, line_3_p2b, line_4_p2b, line_5_p2b, line_6_p2b, line_7_p2b,line_8_p2b, line_9_p2b, line_10_p2b, p1_n, fl2)
    lines_print(line_0_p2b, line_1_p2b, line_2_p2b, line_3_p2b, line_4_p2b, line_5_p2b, line_6_p2b, line_7_p2b,line_8_p2b, line_9_p2b, line_10_p2b)
    if (fl2 == 0):
        print('вітаю', p1_n, 'переміг')
        break

    lines_print(line_0_p1b,line_1_p1b,line_2_p1b,line_3_p1b,line_4_p1b,line_5_p1b,line_6_p1b,line_7_p1b,line_8_p1b,line_9_p1b,line_10_p1b)
    battel(line_0_p1,line_1_p1,line_2_p1,line_3_p1,line_4_p1,line_5_p1,line_6_p1,line_7_p1,line_8_p1,line_9_p1,line_10_p1,line_0_p1b,line_1_p1b,line_2_p1b,line_3_p1b,line_4_p1b,line_5_p1b,line_6_p1b,line_7_p1b,line_8_p1b,line_9_p1b,line_10_p1b,p2_n,fl1)
    lines_print(line_0_p1b, line_1_p1b, line_2_p1b, line_3_p1b, line_4_p1b, line_5_p1b, line_6_p1b, line_7_p1b,line_8_p1b, line_9_p1b, line_10_p1b)
    if (fl1==0):
        print('вітаю',p2_n,'переміг')
        break
