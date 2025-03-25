#поле гри

line_1=['_','_','_','_','_','_','_','_','_']
line_2=['_','_','_','_','_','_','_','_','_']
line_3=['_','_','_','_','_','_','_','_','_']
line_4=['_','_','_','_','_','_','_','_','_']
line_5=['_','_','_','_','_','_','_','_','_']
line_6=['_','_','_','_','_','_','_','_','_']
line_7=['_','_','_','_','_','_','_','_','_']
line_8=['_','_','_','_','_','_','_','_','_']
line_9=['_','_','_','_','_','_','_','_','_']

#функції програми
def win_test(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9,y):
    if (y==1):
        #перевірка по осі X
        if (l_1[0] == 'X'and l_1[1] == 'X'and l_1[2] == 'X'and l_1[3] == 'X'and l_1[4] == 'X'and l_1[5]== 'X' and l_1[6]== 'X' and l_1[7]== 'X' and l_1[8]=='X'):
            return 1
        elif (l_2[0] == 'X'and l_2[1] == 'X'and l_2[2] == 'X'and l_2[3]== 'X' and l_2[4] == 'X'and l_2[5]== 'X' and l_2[6] == 'X'and l_2[7]== 'X' and l_2[8]=='X'):
            return 1
        elif (l_3[0]== 'X' and l_3[1] == 'X'and l_3[2] == 'X'and l_3[3] == 'X'and l_3[4] == 'X'and l_3[5]== 'X' and l_3[6] == 'X'and l_3[7] == 'X'and l_3[8]=='X'):
            return 1
        elif (l_4[0]== 'X' and l_4[1] == 'X'and l_4[2] == 'X'and l_4[3] == 'X'and l_4[4] == 'X'and l_4[5]== 'X' and l_4[6] == 'X'and l_4[7]== 'X' and l_4[8]=='X'):
            return 1
        elif (l_5[0] == 'X'and l_5[1] == 'X'and l_5[2]== 'X' and l_5[3] == 'X'and l_5[4] == 'X'and l_5[5]== 'X' and l_5[6] == 'X'and l_5[7]== 'X' and l_5[8]=='X'):
            return 1
        elif (l_6[0] == 'X'and l_6[1]== 'X' and l_6[2] == 'X'and l_6[3] == 'X'and l_6[4]== 'X' and l_6[5]== 'X' and l_6[6] == 'X'and l_6[7]== 'X' and l_6[8]=='X'):
            return 1
        elif (l_7[0] == 'X'and l_7[1] == 'X'and l_7[2] == 'X'and l_7[3]== 'X' and l_7[4]== 'X' and l_7[5]== 'X' and l_7[6] == 'X'and l_7[7]== 'X' and l_7[8]=='X'):
            return 1
        elif (l_8[0] == 'X'and l_8[1]== 'X' and l_8[2] == 'X'and l_8[3]== 'X' and l_8[4]== 'X' and l_8[5] == 'X'and l_8[6] == 'X'and l_8[7]== 'X' and l_8[8]=='X'):
            return 1
        elif (l_9[0] == 'X'and l_9[1] == 'X'and l_9[2] == 'X'and l_9[3] == 'X'and l_9[4] == 'X'and l_9[5] == 'X'and l_9[6] == 'X'and l_9[7]== 'X' and l_9[8]=='X'):
            return 1
        #перевірка по осі Y
        elif(l_1[0] == 'X'and l_2[0] == 'X'and l_3[0] == 'X'and l_4[0] == 'X'and l_5[0] == 'X'and l_6[0] == 'X'and l_7[0]== 'X' and l_8[0]== 'X' and l_9[0] == 'X'):
            return 1
        elif (l_1[1] == 'X'and l_2[1] == 'X'and l_3[1]== 'X' and l_4[1] == 'X'and l_5[1]== 'X' and l_6[1] == 'X'and l_7[1] == 'X'and l_8[1] == 'X'and l_9[1] == 'X'):
            return 1
        elif (l_1[2] == 'X'and l_2[2] == 'X'and l_3[2]== 'X' and l_4[2] == 'X'and l_5[2] == 'X'and l_6[2] == 'X'and l_7[2] == 'X'and l_8[2]== 'X' and l_9[2] == 'X'):
            return 1
        elif (l_1[3]== 'X' and l_2[3] == 'X'and l_3[3]== 'X' and l_4[3] == 'X'and l_5[3] == 'X'and l_6[3] == 'X'and l_7[3] == 'X'and l_8[3]== 'X' and l_9[3] == 'X'):
            return 1
        elif (l_1[4] == 'X'and l_2[4] == 'X'and l_3[4] == 'X'and l_4[4] == 'X'and l_5[4] == 'X'and l_6[4] == 'X'and l_7[4]== 'X' and l_8[4] == 'X'and l_9[4] == 'X'):
            return 1
        elif (l_1[5] == 'X'and l_2[5] == 'X'and l_3[5] == 'X'and l_4[5] == 'X'and l_5[5] == 'X'and l_6[5] == 'X'and l_7[5] == 'X'and l_8[5] == 'X'and l_9[5] == 'X'):
            return 1
        elif (l_1[6] == 'X'and l_2[6] == 'X'and l_3[6] == 'X'and l_4[6]== 'X' and l_5[6] == 'X'and l_6[6] == 'X'and l_7[6]== 'X' and l_8[6] == 'X'and l_9[6] == 'X'):
            return 1
        elif (l_1[7] == 'X'and l_2[7] == 'X'and l_3[7] == 'X'and l_4[7] == 'X'and l_5[7]== 'X' and l_6[7] == 'X'and l_7[7] == 'X'and l_8[7]== 'X' and l_9[7] == 'X'):
            return 1
        elif (l_1[8] == 'X'and l_2[8] == 'X'and l_3[8] == 'X'and l_4[8] == 'X'and l_5[8]== 'X' and l_6[8] == 'X'and l_7[8]== 'X' and l_8[8]== 'X' and l_9[8] == 'X'):
            return 1
        #перевірка ліній навскоси
        elif(l_1[0] == 'X'and l_2[1] == 'X'and l_3[2] == 'X'and l_4[3] == 'X'and l_5[4]== 'X' and l_6[5]== 'X' and l_7[6]== 'X'and l_8[7]== 'X' and l_9[8] == 'X'):
            return 1
        elif (l_1[8] == 'X'and l_2[7]== 'X' and l_3[6] == 'X'and l_4[5] == 'X'and l_5[4] == 'X'and l_6[3] == 'X'and l_7[2] == 'X'and l_8[1]== 'X' and l_9[0] == 'X'):
            return 1
    elif(y==2):
        # перевірка по осі X
        if (l_1[0] == 'O' and l_1[1]  == 'O'and l_1[2]  == 'O'and l_1[3]== 'O' and l_1[4]== 'O' and l_1[5]== 'O' and l_1[6]== 'O' and l_1[7] == 'O'and l_1[8] == 'O'):
            return 1
        elif (l_2[0] == 'O' and l_2[1]  == 'O'and l_2[2]  == 'O'and l_2[3]== 'O' and l_2[4]== 'O'and l_2[5]== 'O' and l_2[6] == 'O'and l_2[7] == 'O'and l_2[8] == 'O'):
            return 1
        elif (l_3[0] == 'O' and l_3[1]  == 'O'and l_3[2]  == 'O'and l_3[3]== 'O' and l_3[4]== 'O'and l_3[5]== 'O' and l_3[6] == 'O'and l_3[7]== 'O'and l_3[8] == 'O'):
            return 1
        elif (l_4[0] == 'O' and l_4[1]  == 'O'and l_4[2]  == 'O'and l_4[3]== 'O' and l_4[4]== 'O' and l_4[5] == 'O'and l_4[6]== 'O' and l_4[7]== 'O'and l_4[8] == 'O'):
            return 1
        elif (l_5[0]  == 'O'and l_5[1] == 'O' and l_5[2]  == 'O'and l_5[3] == 'O' and l_5[4]  == 'O'and l_5[5]  == 'O'and l_5[6]  == 'O'and l_5[7]  == 'O'and l_5[8] == 'O'):
            return 1
        elif (l_6[0] == 'O' and l_6[1] == 'O' and l_6[2]  == 'O'and l_6[3] == 'O' and l_6[4]  == 'O'and l_6[5] == 'O' and l_6[6]  == 'O'and l_6[7]  == 'O'and l_6[8] == 'O'):
            return 1
        elif (l_7[0] == 'O' and l_7[1]  == 'O'and l_7[2]  == 'O'and l_7[3]  == 'O'and l_7[4] == 'O' and l_7[5] == 'O' and l_7[6] == 'O' and l_7[7] == 'O' and l_7[8] == 'O'):
            return 1
        elif (l_8[0] == 'O' and l_8[1] == 'O' and l_8[2] == 'O' and l_8[3] == 'O' and l_8[4] == 'O' and l_8[5] == 'O' and l_8[6] == 'O' and l_8[7]  == 'O'and l_8[8] == 'O'):
            return 1
        elif (l_9[0] == 'O' and l_9[1] == 'O' and l_9[2] == 'O' and l_9[3] == 'O' and l_9[4]  == 'O'and l_9[5] == 'O' and l_9[6] == 'O' and l_9[7]  == 'O'and l_9[8] == 'O'):
            return 1
        # перевірка по осі Y
        elif (l_1[0] == 'O' and l_2[0] == 'O' and l_3[0] == 'O' and l_4[0] == 'O' and l_5[0]  == 'O'and l_6[0]  == 'O'and l_7[0]  == 'O'and l_8[0]  == 'O'and l_9[0] == 'O'):
            return 1
        elif (l_1[1] == 'O' and l_2[1] == 'O' and l_3[1] == 'O' and l_4[1] == 'O' and l_5[1]  == 'O'and l_6[1] == 'O' and l_7[1]  == 'O'and l_8[1] == 'O' and l_9[1] == 'O'):
            return 1
        elif (l_1[2] == 'O' and l_2[2] == 'O' and l_3[2] == 'O' and l_4[2] == 'O' and l_5[2] == 'O' and l_6[2] == 'O' and l_7[2] == 'O' and l_8[2] == 'O' and l_9[2] == 'O'):
            return 1
        elif (l_1[3] == 'O' and l_2[3] == 'O' and l_3[3] == 'O' and l_4[3] == 'O' and l_5[3] == 'O' and l_6[3] == 'O' and l_7[3] == 'O' and l_8[3] == 'O' and l_9[3] == 'O'):
            return 1
        elif (l_1[4] == 'O' and l_2[4] == 'O' and l_3[4] == 'O' and l_4[4] == 'O' and l_5[4] == 'O' and l_6[4] == 'O' and l_7[4] == 'O' and l_8[4] == 'O' and l_9[4] == 'O'):
            return 1
        elif (l_1[5] == 'O' and l_2[5] == 'O' and l_3[5] == 'O' and l_4[5] == 'O' and l_5[5] == 'O' and l_6[5] == 'O' and l_7[5] == 'O' and l_8[5] == 'O' and l_9[5] == 'O'):
            return 1
        elif (l_1[6] == 'O' and l_2[6] == 'O' and l_3[6] == 'O' and l_4[6] == 'O' and l_5[6] == 'O' and l_6[6] == 'O' and l_7[6] == 'O' and l_8[6] == 'O' and l_9[6] == 'O'):
            return 1
        elif (l_1[7] == 'O' and l_2[7] == 'O' and l_3[7] == 'O' and l_4[7] == 'O' and l_5[7] == 'O' and l_6[7] == 'O' and l_7[7] == 'O' and l_8[7] == 'O' and l_9[7] == 'O'):
            return 1
        elif (l_1[8] == 'O' and l_2[8] == 'O' and l_3[8] == 'O' and l_4[8] == 'O' and l_5[8] == 'O' and l_6[8] == 'O' and l_7[8] == 'O' and l_8[8] == 'O' and l_9[8] == 'O'):
            return 1
        # перевірка ліній навскоси
        elif (l_1[0] == 'O' and l_2[1] == 'O' and l_3[2] == 'O' and l_4[3] == 'O' and l_5[4] == 'O' and l_6[5] == 'O' and l_7[6] == 'O' and l_8[7] == 'O' and l_9[8] == 'O' == 'O'):
            return 1
        elif (l_1[8] == 'O' and l_2[7] == 'O' and l_3[6] == 'O' and l_4[5] == 'O' and l_5[4] == 'O' and l_6[3] == 'O' and l_7[2] == 'O' and l_8[1] == 'O' and l_9[0] == 'O'):
            return 1

def test_na_dyrnya(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9,x,y):
    if (y==1):
        if (l_1[x-1] == '_'):
            return 1
        else:
            return 0
    elif(y==2):
        if (l_2[x - 1] == '_'):
            return 1
        else:
            return 0
    elif (y==3):
        if (l_3[x - 1] == '_'):
            return 1
        else:
            return 0
    elif (y==4):
        if (l_4[x - 1] == '_'):
            return 1
        else:
            return 0
    elif (y==5):
        if (l_5[x - 1] == '_'):
            return 1
        else:
            return 0
    elif (y==6):
        if (l_6[x - 1] == '_'):
            return 1
        else:
            return 0
    elif (y==7):
        if (l_7[x - 1] == '_'):
            return 1
        else:
            return 0
    elif (y==8):
        if (l_8[x - 1] == '_'):
            return 1
        else:
            return 0
    else:
        if (l_9[x - 1] == '_'):
            return 1
        else:
            return 0

def enemy():
    pass

who_win=0
t=0
def game(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9):
        while (True):
            try:
                y,x=map(int,input('введіть кординати клітинки яку хочете вибрати ').split(' '))
                if(test_na_dyrnya(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9,x,y)==1):
                    break
            except ValueError:
                pass
        print(100 * '\n')
        if (y == 1):
            l_1[x - 1] = 'X'
        elif(y == 2):
            l_2[x - 1 ]= 'X'
        elif (y == 3):
            l_3[x - 1] = 'X'
        elif (y == 4):
            l_4[x - 1] = 'X'
        elif (y == 5):
            l_5[x - 1] = 'X'
        elif (y == 6):
            l_6[x - 1] = 'X'
        elif (y == 7):
            l_7[x - 1] = 'X'
        elif (y == 8):
            l_8[x - 1] = 'X'
        elif (y == 9):
            l_9[x - 1] = 'X'
        print(l_1[0], l_1[1], l_1[2], l_1[3], l_1[4], l_1[5], l_1[6], l_1[7], l_1[8])
        print(l_2[0], l_2[1], l_2[2], l_2[3], l_2[4], l_2[5], l_2[6], l_2[7], l_2[8])
        print(l_3[0], l_3[1], l_3[2], l_3[3], l_3[4], l_3[5], l_3[6], l_3[7], l_3[8])
        print(l_4[0], l_4[1], l_4[2], l_4[3], l_4[4], l_4[5], l_4[6], l_4[7], l_4[8])
        print(l_5[0], l_5[1], l_5[2], l_5[3], l_5[4], l_5[5], l_5[6], l_5[7], l_5[8])
        print(l_6[0], l_6[1], l_6[2], l_6[3], l_6[4], l_6[5], l_6[6], l_6[7], l_6[8])
        print(l_7[0], l_7[1], l_7[2], l_7[3], l_7[4], l_7[5], l_7[6], l_7[7], l_7[8])
        print(l_8[0], l_8[1], l_8[2], l_8[3], l_8[4], l_8[5], l_8[6], l_8[7], l_8[8])
        print(l_9[0], l_9[1], l_9[2], l_9[3], l_9[4], l_9[5], l_9[6], l_9[7], l_9[8])
        if (win_test(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9,1)==1):
            return 1
        while (True):
            try:
                y,x=map(int,input('введіть кординати клітинки яку хочете вибрати ').split(' '))
                if(test_na_dyrnya(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9,x,y)==1):
                    break
            except ValueError:
                pass
        print(100 * '\n')
        if (y == 1):
            l_1[x - 1] = 'O'
        elif(y == 2):
            l_2[x - 1 ]= 'O'
        elif (y == 3):
            l_3[x - 1] = 'O'
        elif (y == 4):
            l_4[x - 1] = 'O'
        elif (y == 5):
            l_5[x - 1] = 'O'
        elif (y == 6):
            l_6[x - 1] = 'O'
        elif (y == 7):
            l_7[x - 1] = 'O'
        elif (y == 8):
            l_8[x - 1] = 'O'
        elif (y == 9):
            l_9[x - 1] = 'O'
        print(l_1[0], l_1[1], l_1[2], l_1[3], l_1[4], l_1[5], l_1[6], l_1[7], l_1[8])
        print(l_2[0], l_2[1], l_2[2], l_2[3], l_2[4], l_2[5], l_2[6], l_2[7], l_2[8])
        print(l_3[0], l_3[1], l_3[2], l_3[3], l_3[4], l_3[5], l_3[6], l_3[7], l_3[8])
        print(l_4[0], l_4[1], l_4[2], l_4[3], l_4[4], l_4[5], l_4[6], l_4[7], l_4[8])
        print(l_5[0], l_5[1], l_5[2], l_5[3], l_5[4], l_5[5], l_5[6], l_5[7], l_5[8])
        print(l_6[0], l_6[1], l_6[2], l_6[3], l_6[4], l_6[5], l_6[6], l_6[7], l_6[8])
        print(l_7[0], l_7[1], l_7[2], l_7[3], l_7[4], l_7[5], l_7[6], l_7[7], l_7[8])
        print(l_8[0], l_8[1], l_8[2], l_8[3], l_8[4], l_8[5], l_8[6], l_8[7], l_8[8])
        print(l_9[0], l_9[1], l_9[2], l_9[3], l_9[4], l_9[5], l_9[6], l_9[7], l_9[8])
        if (win_test(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9,2)==1):
            return 2
        return game(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9)



#сама гра
while (True):
    print('удачі в вашому змагані')
    who_win=game(line_1,line_2,line_3,line_4,line_5,line_6,line_7,line_8,line_9)
    if (who_win==1):
        print('вітаю 1 гравець переміг')
    else:
        print('вітаю 2 гравець переміг')
    break