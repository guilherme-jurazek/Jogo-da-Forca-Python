import random
sub_letters = []

words_user = []
tips_user = []

words_fruits = ["banana", "caju", "goiaba", "laranja", "morango", "kiwi", "acerola", "pitanga", "tamarindo", "uva"]
tips_fruits = ["Fruta de cor amarela.", "Tem castanha.", "Romeu e Julieta.", "Tem nome de cor.", "É bom com chocolate.",
               "Groselha chinesa.", "Também chamado de cerejeira-do-pará.", "Parece uma pequena abóbora.",
               "Evita a osteoporose e combate a anemia.", "Usado para fazer vinho." ]

words_games = ["minecraft", "overwatch", "destiny", "tibia", "terraria", "runeterra", "uncharted", "gorogoa", "fortnite", "spore"]
tips_games = ["Blocos...", "Dizem que copiou o Team Fortress.", "Ambiente 'mítico de ficção cientifica'.", "Um dos primeiros MMO.",
              "Minecraft 2D.", "Jogo de cartas.", "Exclusivo do Playstation.", "Um jogo que se assemelha a uma obra de arte.",
               "Danças icônicas.", "Evolução."]

words_movies = ["frozen", "parasita", "resgate", "coringa", "mulan", "matrix", "shrek", "megamente", "rio", "thor"]
tips_movies = ["Let's go.", "Óscar 2019.", "1 contra 1000.", "Quase óscar 2019.", "Na guerra não importa o gênero.",
              "Realidade alternativa.", "Faz urru!", "Grande mente...", "Pássaros que falam.", "Martelo forte."]

words_foods = ["bacon", "ovo", "bolo", "geleia", "bombom", "brigadeiro", "lanche", "pastel", "crepe", "bolacha"]
tips_foods = ["Combina com ovo, conforme os americanos.", "Combina com bacon, conforme os americanos.",
              "Não pode faltar no aniversário.", "Feito de frutas.", "Pequeno e gostoso.", "Leite condensado está nos igredientes.",
              "Ótimo para quem não quer emagrecer.", "Retangular.", "Triangular.", "Bolacha."]
words_themes = ["FRUTAS", "JOGOS", "FILMES", "ALIMENTOS"]
words = [words_fruits, words_games, words_movies, words_foods]
tips = [tips_fruits, tips_games, tips_movies, tips_foods]
end3 = 0
while end3 == 0:
    print("----------------------JOGO DA FORCA----------------------")
    print()
    print("                        JOGAR(1)")
    print()
    print("                  MODO DESENVOLVEDOR(2)")
    print()
    print("                  LISTA DE PALAVRAS(3)")
    print()
    print("                         SAIR(4)")
    print()
    print("---------------------------------------------------------")
    print()
    decision = int(input("O que deseja fazer ? "))
    print()
    if decision == 1:
        print("--------------------|    TEMAS    |----------------------")
        print()
        print("                       FRUTAS(1)")
        print()
        print("                       JOGOS(2)")
        print()
        print("                       FILMES(3)")
        print()
        print("                       COMIDAS(4)")
        print()
        print("                  PALAVRAS DO USUARIO(5)")
        print("                     (Temas diversos)")
        print()
        print("---------------------------------------------------------")
        print()
        theme = int(input("Qual tema vai querer ? "))
        print()
        print("---------------------------------------------------------")
        count = 0
        count_error = 0
        sub_letters = []
        exb = 0
        if theme == 1:
            random_word = random.choice(words_fruits)
            for i in range(0, 10, 1):
                if random_word == words_fruits[i]:
                    position=int(i)
            random_tip = tips_fruits[position]
        elif theme == 2:
            random_word = random.choice(words_games)
            for i in range(0, 10, 1):
                if random_word == words_games[i]:
                    position=int(i)
            random_tip = tips_games[position]
        elif theme == 3:
            random_word = random.choice(words_movies)
            for i in range(0, 10, 1):
                if random_word == words_movies[i]:
                    position=int(i)
            random_tip = tips_movies[position]
        elif theme == 4:
            random_word = random.choice(words_foods)
            for i in range(0, 10, 1):
                if random_word == words_foods[i]:
                    position=int(i)
            random_tip = tips_foods[position]
        elif theme == 5:
            if len(words_user) == 0:
                print("Nenhuma palavra foi adicionada ainda")
                exb = 1
            else:
                random_word = random.choice(words_user)
                for i in range(0, len(words_user), 1):
                    if random_word == words_user[i]:
                        position=int(i)
                random_tip = tips_user[position]

        correct = ''
        if exb == 0:
            underline = ['_'] * len(random_word)

            while count < len(random_word):
                if count_error == 0:
                    print("    +---+")
                    print("    |   |")
                    print("    |")
                    print("    |")
                    print("    |")
                    print("    |")
                    print("=========")
                    print()
                elif count_error == 1:
                    print("    +---+")
                    print("    |   |")
                    print("    |   0")
                    print("    |")
                    print("    |")
                    print("    |")
                    print("=========")
                    print()
                elif count_error == 2:
                    print("    +---+")
                    print("    |   |")
                    print("    |   0")
                    print("    |   |")
                    print("    |")
                    print("    |")
                    print("=========")
                    print()
                elif count_error == 3:
                    print("    +---+")
                    print("    |   |")
                    print("    |   0")
                    print("    |  /|")
                    print("    |")
                    print("    |")
                    print("=========")
                    print()
                elif count_error == 4:
                    print("    +---+")
                    print("    |   |")
                    print("    |   0")
                    print("    |  /|\ ")
                    print("    |")
                    print("    |")
                    print("=========")
                    print()
                    print("Tem apenas mais duas tentativas! Aqui vai uma dica:")
                    print()
                    print(random_tip)
                    print()
                elif count_error == 5:
                    print("    +---+")
                    print("    |   |")
                    print("    |   0")
                    print("    |  /|\ ")
                    print("    |  /")
                    print("    |")
                    print("=========")
                    print()
                elif count_error == 6:
                    print("    +---+")
                    print("    |   |")
                    print("    |   0")
                    print("    |  /|\ ")
                    print("    |  / \ ")
                    print("    |")
                    print("=========")
                    print()
                    count=len(random_word)

                for i in range(len(underline)):
                    print(underline[i], end=' ')
                print()

                print()
                if(count_error<6):
                    letter = str(input("Digite uma letra : "))
                var = 0





                if letter not in sub_letters:
                    print()
                    if(len(letter)==1):
                        if letter in random_word:
                            for i in range(len(random_word)):
                                if random_word[i] == letter:
                                    underline[i] = letter
                            count+=1*random_word.count(letter)
                            sub_letters.append(letter)
                        else:
                            count_error+=1
                            sub_letters.append(letter)
                    elif(len(letter)==len(random_word)):
                        if letter in random_word:
                            count = len(random_word)
                        else:
                            print("Palavra errada!")
                            count_error+=1
                    elif (len(letter)>1):
                        print("Palavra errada!")
                        count_error+=1
                else:
                    print()
                    print("Letra já digitada!")
                    print()
                print()
                print("Letras tentadas :", end="")
                print(sub_letters)
                print()
            print()
            print("---------------------------------------------------------")
            print()
            if count_error<6:
                print("Parabéns! Você acertou a palavra: ")
                print(random_word)
            else:
                print("Que pena, você não conseguiu acertar! A palavra era: ")
                print(random_word)
            print()
            print("---------------------------------------------------------")
    elif decision == 2:
        end2 = 0
        while end2 == 0:
            print("--------------|     MODO DESENVOLVEDOR    |----------------")
            print()
            print("                    ALTERAR PALAVRAS(1)")
            print()
            print("                   ADICIONAR PALAVRAS(2)")
            print()
            print("                    REMOVER PALAVRAS(3)")
            print()
            print("                     ALTERAR DICAS(4)")
            print()
            print("                        VOLTAR(5)")
            print()
            print("-----------------------------------------------------------")
            print()
            interact = int(input("O que deseja fazer ? "))
            print()
            print("---------------------------------------------------------")
            end=0
            while end == 0:
                if interact == 1:
                    print("--------------------|    TEMAS    |----------------------")
                    print()
                    print("                        FRUTAS(1)")
                    print()
                    print("                        JOGOS(2)")
                    print()
                    print("                        FILMES(3)")
                    print()
                    print("                        COMIDAS(4)")
                    print()
                    print("---------------------------------------------------------")
                    print()
                    theme = int(input("A palavra se encontra em qual dos seguintes temas ? "))
                    print()
                    count_change = 0
                    word_change = ""
                    while count_change == 0:
                        word_change = input("Qual palavra deseja alterar? ")
                        if word_change in words[theme-1]:
                            count_change += 1
                        else:
                            print()
                            print("Essa palavra não está no sistema!")
                            print()
                    k=0
                    while k < len(words[theme-1]):
                        if word_change == words[theme-1][k]:
                            words[theme - 1][k] = (input("Qual a alteração que você deseja? "))
                        k+=1
                    print()
                    print("Deseja alterar outra palavra? 1(SIM) 2(NÃO)")
                    print()
                    if int(input()) == 2:
                        end += 1
                elif interact == 2:
                    print()
                    print("--------------------|    TEMAS    |----------------------")
                    print()
                    print("                        FRUTAS(1)")
                    print()
                    print("                        JOGOS(2)")
                    print()
                    print("                        FILMES(3)")
                    print()
                    print("                        COMIDAS(4)")
                    print()
                    print("---------------------------------------------------------")
                    print()
                    theme = int(input("A palavra que você quer adicionar se encontra em qual dos seguintes temas ? "))
                    print()
                    word = (input("Qual palavra deseja adicionar ? "))
                    words[theme - 1].append(word)
                    words_user.append(word)
                    print()
                    tip = (input("Qual a dica dessa palavra ? "))
                    tips[theme - 1].append(tip)
                    tips_user.append(tip)
                    print()
                    print()
                    print("Deseja adicionar mais uma palavra? 1(SIM) 2(NÃO)")
                    print()
                    if int(input()) == 2:
                        end += 1

                elif interact == 3:
                    print("--------------------|    TEMAS    |----------------------")
                    print()
                    print("                        FRUTAS(1)")
                    print()
                    print("                        JOGOS(2)")
                    print()
                    print("                        FILMES(3)")
                    print()
                    print("                        COMIDAS(4)")
                    print()
                    print("---------------------------------------------------------")
                    print()
                    theme = int(input("A palavra se encontra em qual dos seguintes temas ? "))
                    print()
                    count_change = 0
                    word_change = ""
                    while count_change == 0:
                        word_change = input("Qual palavra deseja remover? ")
                        if word_change in words[theme - 1]:
                            count_change += 1
                        else:
                            print()
                            print("Essa palavra não está no sistema!")
                            print()
                    k = 0
                    while k < len(words[theme - 1]):
                        if word_change == words[theme - 1][k]:
                            del(words[theme - 1][k])
                            del(tips[theme - 1][k])
                        k += 1
                    print()
                    print("Deseja remover outra palavra? 1(SIM) 2(NÃO)")
                    print()
                    if int(input()) == 2:
                        end += 1
                elif interact == 4:
                    print("--------------------|    TEMAS    |----------------------")
                    print()
                    print("                        FRUTAS(1)")
                    print()
                    print("                        JOGOS(2)")
                    print()
                    print("                        FILMES(3)")
                    print()
                    print("                        COMIDAS(4)")
                    print()
                    print("---------------------------------------------------------")
                    print()
                    theme = int(input("A dica se encontra em qual dos seguintes temas ? "))
                    print()
                    count_change = 0
                    word_change = ""
                    while count_change == 0:
                        word_change = input("Qual a palavra da dica que deseja alterar? ")
                        if word_change in words[theme - 1]:
                            count_change += 1
                        else:
                            print()
                            print("Essa palavra não está no sistema!")
                            print()
                    k = 0
                    while k < len(words[theme - 1]):
                        if word_change == words[theme - 1][k]:
                            tips[theme - 1][k] = (input("Qual a alteração que você deseja? "))
                        k += 1
                    print()
                    print("Deseja alterar outra dica? 1(SIM) 2(NÃO)")
                    print()
                    if int(input()) == 2:
                        end += 1
                elif interact == 5:
                    end += 1
                    end2 += 1
    elif decision == 3:
        i=0
        for i in range(len(words_themes)):
            print()
            print("-->", end="")
            print(words_themes[i], end="")
            print("<--")
            print()
            for j in range(len(words[i])):
                print("-", end="")
                print(words[i][j])
            print()
            print("-------------------------------------------------------")
    elif decision == 4:
        end3 += 1




    pgt = int(input("\nReponder novamente? (Sim=1/Não=2)\n"))

