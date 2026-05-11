# jogo de adinhaçao
import random
numero_secreto = random.randint(1, 10)
tentativas = 3
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 10.")
while tentativas > 0:
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero_secreto:
        print("Parabéns! Você adivinhou o número secreto!")
        break
    else:
        tentativas -= 1
        print(f"Errado! Você tem {tentativas} tentativas restantes.")

if tentativas == 0:
    print(f"Game over! O número secreto era {numero_secreto}.")

