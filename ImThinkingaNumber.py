import random
PlayAgain = 'Y'
Trying = True
Tentativas = 0;


while PlayAgain == 'Y':

    print('Digite uma dificuldade: (1, 2, 3)')

    Dificulty = int(input());

    if      (Dificulty == 1):
        SelectedNumber = random.randint(0, 20)
        limit = 20;

    elif    (Dificulty == 2):
        SelectedNumber = random.randint(0, 40)
        limit = 40;

    elif    (Dificulty == 3):
        SelectedNumber = random.randint(0, 100)
        limit = 100;

    print('O número está entre 0 e ' + str(limit))

    Trying = True;
    
    while Trying:

        print('Digite sua tentativa...')
        Tryed = int(input())
        if(SelectedNumber == Tryed):
            print('Gol...')
            Trying = False;
            Tentativas = Tentativas + 1
            print('Você conseguiu em: ' + str(Tentativas) +  ' tentivas.')



        elif(Tryed > SelectedNumber):
                print('Tente mais baixo...')
                Tentativas = Tentativas + 1
                continue;

        elif(Tryed < SelectedNumber):
                print('Tente mais alto...')
                Tentativas = Tentativas + 1
                continue;