print("jogo de adivinhação")
print("Tente adivinhar o número que estou pensando entre 1 e 100")
import random

numero_secreto = random.randint(1, 100)
input_number = None
while input_number != numero_secreto:
    input_number = input("Digite um número: ")
    if input_number.isdigit() and 1 <= int(input_number) <= 100:
        input_number = int(input_number)
        if input_number == numero_secreto:
            print("Parabéns! Você acertou!")
        elif input_number < numero_secreto:
            print("O número secreto é maior do que", input_number)
        else:
            print("O número secreto é menor do que", input_number)
        
    else:
        print("Por favor, digite um número válido.")


