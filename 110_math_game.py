def gof(p):
    return 11-p
def game():
    x=0
    while True:
        pl=int(input('введіть число до 10 '))
        x+=pl
        if (x==110):
            print('you win')
            print('idk how')
            break
        bo=gof(pl)
        print(bo)
        x+=bo
        if (x==110):
            print('you lose')
            break
game()