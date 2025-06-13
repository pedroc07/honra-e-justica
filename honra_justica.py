import random
import pickle
import time
import os

#EDITAR O ACESSO AO TEMPLO E AO DRAGÃO

class Samurai:
    def __init__(self, nome, level, xp, hp, atk, dfs, vel, ataques=[1, 2, 3]):
        self.level = level
        self.nome = nome  # nome do jogador
        self.alcunha = ""
        self.zerou = False
        self.xp = xp  # relativo à experiência do jogador
        self.katana = 0  # itens sob posse do jogador
        self.grana = 10  # dinheiro do jogador
        self.hp = hp
        self.hp_max = self.hp
        self.atk = atk
        self.dfs = dfs
        self.vel = vel
        self.escolha = ''
        self.ataques = ataques
        self.vitorias = 30
        self.historia = 0
        self.escolhas_fase1 = [1, 2, 3, 4, 5]
        self.escolhas_fase2 = [1, 2, 3, 4, 5]
        self.viu_dragao = False
        self.ouviu_templo = False

    def upar(self):
        xp_necessario = self.level * 100
        while self.xp >= xp_necessario:
            self.level += 1
            self.xp = 0
            xp_necessario = self.level * 100
            self.atk += random.randint(1, 3)
            self.dfs += random.randint(1, 3)
            self.vel += random.randint(1, 3)
            self.hp_max += random.randint(2, 5)
            print(f"{self.alcunha}{self.nome} upou para o nível {self.level}")
        self.vitorias += 1

    def imprime_stats(self):
        print(f'\nNome: {self.alcunha}{self.nome}')
        print(f'Level: {self.level}')
        print(f'Experiência: {self.xp}')
        print(f'HP: {self.hp}/{self.hp_max}')
        print(f'Ataque: {self.atk}')
        print(f'Defesa: {self.dfs}')
        print(f'Velocidade: {self.vel}')
        print(f'Vitórias: {self.vitorias}')
        input("\nAperte ENTER para sair")

    def ataque_rapido(self, inimigo):
        print("")
        if inimigo.escolha == 2:
            inimigo.hp -= self.atk
            self.hp -= inimigo.atk
            print(f"{self.nome} realizou um ataque rápido")
            print(f"{inimigo.nome} perdeu {self.atk} de vida")
            print(f"{inimigo.nome} realizou um ataque rápido")
            print(f"{self.nome} perdeu {inimigo.atk} de vida")
        elif inimigo.escolha == 1:
            inimigo.hp -= self.atk
            print(f"{self.alcunha}{self.nome} realizou um ataque rápido")
            print(
                f"{inimigo.nome} tentou um ataque forte e perdeu {self.atk} de vida"
            )
        elif inimigo.escolha == 3 or inimigo.escolha == 6:
            print(f"{self.alcunha}{self.nome} tentou um ataque rápido")
            print(f"{inimigo.nome} defendeu e o empurrou de volta")
            self.hp -= self.atk//2
        elif inimigo.escolha == 4:
            #ataque exclusivo do dragão
            print(f"{inimigo.nome} bradou chamas")
            print(
                f"{self.alcunha}{self.nome} tentou um ataque rápido e perdeu {int(inimigo.atk*1.5)} de vida"
            )
            self.hp -= int(inimigo.atk * 1.5)
        elif inimigo.escolha == 5:
            acerto = random.randint(1, 2)
            if acerto == 1:
                print(f"{inimigo.nome} deu um tiro mas errou")
                inimigo.hp -= self.atk
                print(f"{self.alcunha}{self.nome} realizou um ataque rápido")
                print(f"{inimigo.nome} perdeu {self.atk} de vida")
            else:
                print(
                    f"{inimigo.nome} deu um tiro"
                )
                print(f"{self.alcunha}{self.nome} tentou um ataque rápido e perdeu 10 de vida")
                self.hp -= 10

    def ataque_forte(self, inimigo):
        print("")
        if inimigo.escolha == 2 or inimigo.escolha == 6:
            self.hp -= inimigo.atk
            print(f"{inimigo.nome} realizou um ataque rápido")
            print(
                f"{self.alcunha}{self.nome} tentou um ataque forte e perdeu {inimigo.atk} de vida"
            )
        elif inimigo.escolha == 1:
            inimigo.hp -= int(self.atk * 1.5)
            print(f"{self.alcunha}{self.nome} realizou um ataque forte")
            print(f"{inimigo.nome} perdeu {int(self.atk * 1.5)} de vida")
            self.hp -= int(inimigo.atk * 1.5)
            print(f"{inimigo.nome} realizou um ataque forte")
            print(f"{self.alcunha}{self.nome} perdeu {int(inimigo.atk * 1.5)} de vida")
        elif inimigo.escolha == 3:
            inimigo.hp -= self.atk - inimigo.dfs // 2
            print(f"{self.alcunha}{self.nome} realizou um ataque forte")
            print(
                f"{inimigo.nome} tentou defender mas perdeu {self.atk//2} de vida"
            )
        elif inimigo.escolha == 4:
            #ataque exclusivo do dragão
            print(f"{inimigo.nome} bradou chamas")
            print(
                f"{self.alcunha}{self.nome} tentou um ataque forte e perdeu {int(inimigo.atk * 1.5)} de vida"
            )
            self.hp -= int(inimigo.atk * 1.5)
        elif inimigo.escolha == 5:
            acerto = random.randint(1, 2)
            if acerto == 1:
                print(f"{inimigo.nome} deu um tiro mas errou")
                inimigo.hp -= int(self.atk * 1.5)
                print(f"{self.alcunha}{self.nome} realizou um ataque forte")
                print(f"{inimigo.nome} perdeu {int(self.atk * 1.5)} de vida")
            else:
                print(f"{inimigo.nome} deu um tiro")
                print(
                    f"{self.alcunha}{self.nome} tentou um ataque forte e perdeu 10 de vida")
                self.hp -= 10

    def defesa(self, inimigo):
        print("")
        if inimigo.escolha == 2:
            inimigo.hp -= inimigo.atk//2
            print(f"{inimigo.nome} tentou um ataque rápido")
            print(f"{self.alcunha}{self.nome} defendeu e o empurrou de volta")
        elif inimigo.escolha == 1 or inimigo.escolha == 6:
            self.hp -= inimigo.atk - self.dfs // 2
            print(f"{inimigo.nome} realizou um ataque forte")
            print(
                f"{self.alcunha}{self.nome} tentou defender mas perdeu {inimigo.atk//2} de vida"
            )
        elif inimigo.escolha == 3:
            print(f"{self.alcunha}{self.nome} defendeu")
            print(f"{inimigo.nome} defendeu")
        elif inimigo.escolha == 4:
            #ataque exclusivo do dragão
            print(f"{inimigo.nome} bradou chamas")
            print(
                f"{self.alcunha}{self.nome} tentou defender mas perdeu {int(inimigo.atk*1.5)} de vida"
            )
            self.hp -= int(inimigo.atk * 1.5)
        elif inimigo.escolha == 5:
            acerto = random.randint(1, 2)
            if acerto == 1:
                print(f"{inimigo.nome} deu um tiro mas errou")
            else:
                print(f"{inimigo.nome} deu um tiro")
                print(f"{self.alcunha}{self.nome} tentou defender mas perdeu 10 de vida")
                self.hp -= 10

    def acenar(self, inimigo):
      if inimigo.nome == "Kappa Maligno":
        print(f"{self.alcunha}{self.nome} acenou")
        print(f"{inimigo.nome} acenou deixando derramar a água em sua cabeça")
        inimigo.hp -= inimigo.hp
      elif inimigo.escolha == 2:
            self.hp -= inimigo.atk
            print(f"{inimigo.nome} tentou um ataque rápido")
            print(f"{self.alcunha}{self.nome} acenou e perdeu {inimigo.atk} de vida")
      elif inimigo.escolha == 1 or inimigo.escolha == 6:
            self.hp -= inimigo.atk
            print(f"{inimigo.nome} realizou um ataque forte")
            print(
                f"{self.alcunha}{self.nome} acenou e perdeu {inimigo.atk} de vida"
            )
      elif inimigo.escolha == 3:
            print(f"{self.alcunha}{self.nome} acenou")
            print(f"{inimigo.nome} defendeu")
      elif inimigo.escolha == 4:
            #ataque exclusivo do dragão
            print(f"{inimigo.nome} bradou chamas")
            print(
                f"{self.alcunha}{self.nome} acenou e perdeu {int(inimigo.atk*1.5)} de vida"
            )
            self.hp -= int(inimigo.atk * 1.5)
      elif inimigo.escolha == 5:
            acerto = random.randint(1, 3)
            if acerto == 1:
                print(f"{inimigo.nome} deu um tiro mas errou")
                print(f"{self.alcunha}{self.nome} acenou")
            else:
                print(f"{inimigo.nome} deu um tiro")
                print(f"{self.alcunha}{self.nome} acenou e perdeu 10 de vida")
                self.hp -= 10

def batalha(P1, E1):
    moves = "\n[Z] Ataque Rápido\n[X] Ataque forte\n[C] Defesa\n"
    if P1.historia >= 1:
      moves += "[V] Acenar\n"
    print(f"Você encontrou um {E1.nome} lv {E1.level}")
    if E1.nome == "Dragão":
        print(f"\n{E1.nome} devorou sua própria barra de HP")
    while E1.hp != 0 and P1.hp > 0:
        E1.escolha = random.choice(E1.ataques)
        if E1.nome == "Dragão":
            print(f"\n{E1.nome} lv {E1.level}")
        else:
            print(f"\n{E1.nome} lv {E1.level}\nHP: {E1.hp}/{E1.hp_max}")
        print(f"{P1.alcunha}{P1.nome} lv {P1.level}\nHP: {P1.hp}/{P1.hp_max}")
        movimento = input(moves)
        if movimento.upper() == 'Z':
            P1.ataque_rapido(E1)
        elif movimento.upper() == 'X':
            P1.ataque_forte(E1)
        elif movimento.upper() == 'C':
            P1.defesa(E1)
        elif movimento.upper() == 'V' and P1.historia >= 1:
            P1.acenar(E1)
        if E1.hp < 0:
            E1.hp = 0
    if P1.hp <= 0:
        P1.hp = 0
        print("GAME OVER")
        time.sleep(3)
        exit()
    else:
        E1.hp = 0
        print(f"\n{P1.alcunha}{P1.nome} derrotou {E1.nome}")
        P1.xp += E1.xp
        P1.upar()
        if P1.vitorias == 50:
            print(f"\n{E1.nome}: Nossa, você é bem forte...")
            print(f"\n{E1.nome}: Sabe, seguindo ao norte, não muito longe daqui há um monastério onde os monges lutam Jiu-Jitsu. Acho que eles podem te dar algum trabalho, haha")
            P1.ouviu_templo = True

def novo_jogo():
    nome = input("Digite seu nome: ")
    P1 = Samurai(nome, 1, 0, 20, 5, 5, 5)
    return P1


def nomeia_samurai():
    with open('surnames.txt') as sobrenomes:
        linhas_sobre = sobrenomes.readlines()
        sobrenome = random.choice(linhas_sobre)
    with open('names.txt') as nomes:
        linhas_nome = nomes.readlines()
        nome = random.choice(linhas_nome)
    nome = sobrenome[:-1] + ' ' + nome[:-1]
    return nome


def templo(P1):
    print("Seguindo as instruções de seu adversário, você segue ao norte em uma estrada íngreme e tortuosa. Seus pés já estão cansado e cheios de calos quando você avista")
    print("um prédio de aparência eclesiástica.")
    print("...")
    print("Monge A: Então lhe contaram de nossa força? Pois saiba que treinamos todos os dias aqui, lutar nos aproxima da iluminação. Agora o que lhe trás aqui? Queres lutar também?")
    print("Certo.")
    MongeA = Samurai("Monge A", 10, 1000, 80, 10, 10, 10, [1, 2, 3, 3, 6, 6])
    batalha(P1, MongeA)
    MongeB = Samurai("Monge B", 10, 1000, 80, 12, 12, 12, [1, 2, 3, 3, 6, 6])
    batalha(P1, MongeB)
    MongeC = Samurai("Monge C", 10, 1000, 80, 13, 13, 13, [1, 2, 3, 3, 6, 6])
    batalha(P1, MongeC)
    print("Monge C: Você é forte, de fato. Porém você não é páreo para Saito Benkei, nosso maior guerreiro.")
    print("Benkei: Derroto e capturo as espadas dos samurais indignos de carregá-las. Já tenho 999, será você digno, garoto?")
    SaitoBenkei = Samurai("Benkei", 18, 3000, 110, 15, 15, 15, [1, 2, 3, 6, 6, 6, 6])
    batalha(P1, SaitoBenkei)
    print("Benkei: Parabéns, garoto. Você se mostrou digno da espada que empunha.")
    print("Benkei: Você provou sua força, honra e dignidade mediante terríveis adversidades.")
    print("Benkei: Você concluiu sua missão e agora pode repousar ou continuar procurando desafios no campo de batalha.")

    P1.alcunha = "Kensei "
    P1.zerou = True
    P1.vitorias += 1

def jogo():
    print("\nHonra e Justiça\n")
    print("[1]NEW GAME")
    print("[2]CONTINUE")
    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
        P1 = novo_jogo()
        input(
            f"{P1.nome}, um bravo guerreiro samurai se encontra em desonra após a morte do seu mestre em estranhas condições, agora na condição de 'ronin', um samurai errante, {P1.nome} segue invicto após 30 duelos."
        )
        E1 = Samurai("Ladrão", 5, 100, 20, 5, 5, 5)
        batalha(P1, E1)
    elif opcao == '2':
        arquivo = open('save.bin', 'rb')
        P1 = pickle.load(arquivo)
        arquivo.close()
    jogo = True
    while jogo:
        texto = "\n[1]Explorar\n[2]Descansar\n[3]Stats\n"
        if P1.viu_dragao:
            texto += "[4]Dragão\n"
        if P1.ouviu_templo:
            texto += "[5]Templo budista\n"
        if P1.zerou:
            texto += "[6]Epílogo"
        escoha_jogo = input(f"{texto}\nEscolha: ")
        if escoha_jogo == "1":
            if P1.historia == 0:
                prob = random.choice(P1.escolhas_fase1)
                if prob == 1:
                    E1 = Samurai("Ladrão", 5, random.randint(50, 100),
                                 random.randint(20, 30), random.randint(6, 8),
                                 random.randint(6, 8), random.randint(6, 8))
                    batalha(P1, E1)
                elif prob == 2:
                    Oni = Samurai("Oni", 10, 150, 30, 5, 7, 3,
                                  [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3])
                    batalha(P1, Oni)
                elif prob == 3:
                    Arcabuzeiro = Samurai("Arcabuzeiro", 5,
                                          random.randint(80, 150), 20,
                                          random.randint(6, 8),
                                          random.randint(6, 8),
                                          random.randint(6, 8), [1, 5, 5])
                    batalha(P1, Arcabuzeiro)
                elif prob == 4:
                    P1.viu_dragao = True
                    P1.escolhas_fase1.remove(4)
                    arquivo = open('save.bin', 'wb')
                    pickle.dump(P1, arquivo)
                    arquivo.close()
                    print(
                        "Ao atravessar umna rochosa montanha, você chega a uma pequena vila em um vasto vale. Uma figura chama sua atenção, um ser gigantesco que bradava chamas contra a pacata aldeia."
                    )
                    Dragao = Samurai("Dragão", 15, 1000, 60, 10, 10, 10,
                                     [1, 1, 2, 3, 3, 4])
                    batalha(P1, Dragao)
                    P1.historia += 1
                    P1.viu_dragao = False
                elif prob == 5:
                    print(
                        "Andando pelas ruas de uma pacata vila, você passa por uma encruzilhada e avista uma mulher muito bela de longos cabelos pretos com o rosto parcialmente coberto por uma máscara vindo em sua direção."
                    )
                    print("- Você me acha bonita? - Ela pergunta a você.")
                    print("[1] Sim\n[2] Não")
                    opcao_mulher1 = input("\nEscolha uma opção: ")
                    if opcao_mulher1 == '1':
                        print(
                            "A mulher remove sua máscara revelando uma boca que se prolonga em um grande corte indo de orelha a orelha."
                        )
                        print("Ainda assim?")
                        print("[1] Sim\n[2] Não")
                        opcao_mulher2 = input("\nEscolha uma opção: ")
                        if opcao_mulher2 == '1':
                            print(
                                "A mulher corta a sua boca de forma que você fica igual a ela"
                            )
                            P1.alcunha = "Boca Cortada "
                            P1.escolhas_fase1.remove(5)
                        elif opcao_mulher2 == '2':
                            print("A mulher corta você ao meio")
                            print("GAME OVER")
                            exit()
                    elif opcao_mulher1 == '2':
                        print("A mulher corta você ao meio")
                        print("GAME OVER")
                        exit()
            elif P1.historia == 1:
              prob = random.choice(P1.escolhas_fase2)
              if prob == 1 or prob == 5:
                E1 = Samurai(nomeia_samurai(), 10, random.randint(300, 500), 50,
                         random.randint(9, 10), random.randint(9, 10),
                         random.randint(9, 10), [1, 2, 3, 6])
                batalha(P1, E1)
              elif prob == 2:
                  Oni = Samurai("Oni", 13, 500, 57, 7, 11, 4,
                                  [1, 1, 1, 1, 2])
                  batalha(P1, Oni)
              elif prob == 3:
                  Arcabuzeiro = Samurai("Arcabuzeiro", 8,
                                          random.randint(200, 400), 30,
                                          random.randint(8, 9),
                                          random.randint(8, 9),
                                          random.randint(9, 10), [1, 5, 5])
                  batalha(P1, Arcabuzeiro)
              elif prob == 4:
                Kappa = Samurai("Kappa Maligno", 7,
                                          400, 50,
                                          random.randint(9, 10),
                                          random.randint(9, 10),
                                          random.randint(9, 10), [1, 2, 2, 2, 2, 3, 3, 3])
                batalha(P1, Kappa)
        elif escoha_jogo == "2":
            P1.hp = P1.hp_max
            arquivo = open('save.bin', 'wb')
            pickle.dump(P1, arquivo)
            arquivo.close()
            print("Jogo salvo com sucesso.")
        
        elif escoha_jogo == "3":
            P1.imprime_stats()
            
        elif escoha_jogo == "4" and P1.viu_dragao:
            print(
                        "Ao atravessar umna rochosa montanha, você chega a uma pequena vila em um vasto vale. Uma figura chama sua atenção, um ser gigantesco que bradava chamas contra a pacata aldeia."
                    )
            Dragao = Samurai("Dragão", 15, 1000, 60, 10, 10, 10,
                                     [1, 1, 2, 3, 3, 4])
            batalha(P1, Dragao)
            P1.historia += 1
            P1.viu_dragao = False
            
        elif escoha_jogo == "5" and P1.ouviu_templo:
            templo(P1)

        elif escoha_jogo == "6" and P1.zerou:
            os.system('clear')
            print("Em uma humilde cabana numa vila do interior, repousa com glória um antigo herói que se fez conhecido pela lendas populares.")
            print("O sorriso inocente e os cabelos brancos ocultam os grandiosos feitos de sua vida antiga.")
            print("Um verdadeiro santo.")
            jogo = False
jogo()
