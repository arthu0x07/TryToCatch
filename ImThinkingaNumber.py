print(' Irei pensar em um número. Selecione uma Dificuldade: (1, 2, 3).')


def StartingGame( DificultySelected = input() ):
    if int(DificultySelected) == 1:
        GameDificultyOne()
    
    elif int(DificultySelected) == 2:
        GameDificultyTwo()

    elif int(DificultySelected) == 3:
        GameDificultyThree()

    else:
        print('Selecione um valor pré-definido')
        StartingGame()

def GameDificultyOne():

