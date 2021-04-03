def usuario_escolhe_jogada(n,m):
    pecas = int(input("Quantas peças você vai tirar? "))

    if pecas > m or pecas <= 0 or pecas > n:
        while pecas > m or pecas <= 0 or pecas > n:
            print("Oops! Jogada inválida! Tente de novo.")
            pecas = int(input("Quantas peças você vai tirar? "))
        if pecas == 1:
            print("Você tirou uma peça.")
        else:
            print("Você tirou",pecas,"peças.")

    elif pecas == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou",pecas,"peças.")
    return pecas

def computador_escolhe_jogada(n,m):
    if n % (m+1) == 0:
        if m > 1:
            print("Computador tirou",m,"peças.")
        elif m == 1:
            print("Computador tirou uma peça.")
        return m

    else:
        if n == 1:
            print("Computador tirou uma peça.")
            return 1

        else:
            r = 1
            k = 0
            j = n
            while n % (m+1) != 0 and n >= 0:
                n = n - r
                k = n

            if n % (m+1) != 0:
                if m == n and m > 1:
                    print("Computador tirou",m,"peças")
                    return m

                elif n < m and n != 0:
                    print("Computador tirou",n,"peças")
                    return n
            else:
                if (j-k) == 1:
                    print("Computador tirou uma peça.")

                else:
                    print("Computador tirou",(j-k),"peças.")

                return j - k

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m+1) == 0 and m != 0:
        print("Você começa.")
        n = n - usuario_escolhe_jogada(n,m)

        if n == 0:
            print("Fim do jogo! Você ganhou.")
            return False
        else:
            print("Agora restam",n,"peças no tabuleiro.")

        while n > 0:
            n = n - computador_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return True
                break
            print("Agora restam",n,"peças no tabuleiro.")

            n = n - usuario_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! Você ganhou.")
                return False
                break
            print("Agora restam",n,"peças no tabuleiro.")

    else:
        print("Computador começa!")
        n = n - computador_escolhe_jogada(n,m)

        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            return True
        else:
            print("Agora restam",n,"peças no tabuleiro.")

        while n > 0:
            n = n - usuario_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! Você ganhou.")
                return False
                break
            print("Agora restam",n,"peças no tabuleiro.")

            n = n - computador_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return True
                break
            print("Agora restam",n,"peças no tabuleiro.")

def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print()
    print("1 - para jogar uma partida isolada ")
    o = int(input("2 - para jogar um campeonato "))
    if o == 1:
        print("Você escolheu partida isolada!")
        partida()

    else:
        print("Você escolheu um campeonato!")
        r = 1
        l = 0
        p = 0
        while r != 4:
            print("**** Rodada",r,"****")
            if partida() == True:
                l = l + 1
            else:
                p = p + 1
            r = r + 1

        print("**** Final do campeonato! ****")
        print()
        print("Placar: Você",p," X ",l," Computador")

campeonato()
