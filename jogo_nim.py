def computador_escolhe_jogada(n,m):
    jogada_comp = 0
    while jogada_comp == 0:
        jogada_comp = estrategia(n,m)
        msg_jogada_comp(jogada_comp)
        n = n-jogada_comp    
        msg_tabuleiro(n)    
    return jogada_comp


def usuario_escolhe_jogada(n,m):
    jogada_usuar = 0
    while jogada_usuar > m or jogada_usuar < 1:
        jogada_usuar = int(input(' Quantas peças você vai tirar? '))
        if jogada_usuar > m or jogada_usuar < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            msg_jogada_usuar(jogada_usuar)
            n = n - jogada_usuar
            msg_tabuleiro(n)    
    return jogada_usuar                    

    

def partida():
    n = 0
    m = 1
    while m > n or n <= 0 or m <= 0:

        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))
        if m > n or n <= 0 or m <= 0:
            print()
            print('Valor invalido! Favor digitar um valor que seja valido onde o limte de peças por jogada seja maior que a quantidade de peças e que ambos sejam diferente de zero')
            print()

    if n % (m+1) == 0:
        print()
        print('Voce começa!')
        while n > 0:
            print()
            jogada_usuar =  usuario_escolhe_jogada(n,m)
            n = n-jogada_usuar
            jogada_comp = computador_escolhe_jogada(n,m)
            n = n-jogada_comp
        if n == 0:
            print('Fim do jogo! O computador ganhou!')    
    else:
        print()
        print('Computador começa!')
        while n > 0:
            print()
            jogada_comp =  computador_escolhe_jogada(n,m)
            n = n-jogada_comp
            if n == 0:
                break
            jogada_usuar = usuario_escolhe_jogada(n,m)
            n = n-jogada_usuar
        if n == 0:
            print('Fim do jogo! O computador ganhou!')
            

     

def campeonato(partidas):
    partidas = 0
    while partidas <=3:
        partidas = partidas + 1
        if partidas == 1:
            print()
            print('**** Rodada 1 ****')
            print()
            partida()
        if partidas == 2:
            print()
            print('**** Rodada 2 ****')
            print()
            partida()
        if partidas == 3:
            print()
            print('**** Rodada 3 ****')
            print()
            partida()
            print()        
            print('**** Final do campeonato! ****')
            print()
    print('Placar: Você 0 X 3 Computador')


def msg_tabuleiro(n):
    if n == 1:
        print('Agora resta apenas uma peça no tabuleiro')
        print()
    else:
        if n > 1 :
            print('Agora restam ', n, ' peças no tabuleiro.')
            print()
        else:
            pass    




def msg_jogada_usuar(jogada_usuar):
    if jogada_usuar == 1:
        print()
        print('Voce tirou uma peça.')
    else:
        print()
        print('Voce tirou ', jogada_usuar, ' peças.')    


def msg_jogada_comp(jogada_comp):
    if jogada_comp == 1:
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou ', jogada_comp, ' peças.')

def estrategia(n,m):
    jogada_comp = 0
    if n<=m:
        jogada_comp = n
        n = n-jogada_comp
    while n % (m+1) != 0 and n>m:
        jogada_comp = n-(m+1)
        n = n-jogada_comp
        if jogada_comp>m:
            n = n+jogada_comp
            jogada_comp = m
            n = n-jogada_comp
            while n % (m+1) != 0 and n>m:
                n = n+1
                jogada_comp = jogada_comp-1 

    return jogada_comp    




escolha_partida = 0
valida = False
while escolha_partida > 2 or escolha_partida < 1:
    escolha_partida = int(input(' Bem-vindo ao jogo do NIM! Escolha:\n \n 1 - para jogar uma partida isolada\n 2 - para jogar um campeonato '))
    if escolha_partida > 2 or escolha_partida < 1:
        print()
        print('Valor invalido. Favor escolher uma das opções.')
        print()
    else:
        valida = True
    while valida == True:
        if escolha_partida == 1:
            print()
            print('Voce escolheu uma partida isolada')
            print()
            print('**** Inicio de Partida ****')
            print()
            partida()
            valida = False      
        if escolha_partida == 2:
            print()
            print('Voce escolheu um campeonato!')
            campeonato(0)
            valida = False         
     
  