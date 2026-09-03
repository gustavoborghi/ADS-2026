print("jogo de adivinhação")
print("Tente adivinhar o número que estou pensando entre 1 e 100")
import random

numero_secreto = random.randint(1, 100)
input_number = None
tentativas = 7
while numero_secreto != input_number and tentativas > 0:
    input_number = input("Digite um número: ")
    tentativas -= 1 
    if input_number.isdigit() and 1 <= int(input_number) <= 100:
        input_number = int(input_number)
        if input_number == numero_secreto:
            print("Parabéns! Você acertou!")
        elif input_number < numero_secreto:
            print("O número secreto é maior do que", input_number)
            print("Você tem", tentativas, "tentativas restantes.")
        else:
            print("O número secreto é menor do que", input_number)
            print("Você tem", tentativas, "tentativas restantes.")
    else:
        print("Por favor, digite um número válido.")

if tentativas == 0:
    print("Suas tentativas acabaram! O número secreto era:", numero_secreto)
