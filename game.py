import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limite_tentativas = 15

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while tentativas < limite_tentativas:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
        else:
            diferenca = abs(numero_secreto - palpite)
            if diferenca <= 10:
                print("Você está quente!")
            else:
                print("Você está frio!")

            if tentativas == limite_tentativas:
                print(f"Você atingiu o limite de {limite_tentativas} tentativas. O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()
