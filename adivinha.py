import random

def jogo():
    print(f"""
    ╔══════════════════════════════════════╗
    ║         JOGO DE ADIVINHAÇÃO          ║
    ╚══════════════════════════════════════╝
    """)
    print("Tente adivinhar o número que estou pensando entre 1 e 100")
 
    dificuldade = int(input("Deseja jogar em qual dificuldade: 1, 2 ou 3? "))
    input_number = None
    limite = None
    if dificuldade == 1:
        limite = 50
        tentativas = 10
        print("Tente adivinhar o número que estou pensando entre 1 e 50")
    elif dificuldade == 2:
        limite = 100
        tentativas = 7
        print("Tente adivinhar o número que estou pensando entre 1 e 100")
    elif dificuldade == 3:
        limite = 500
        tentativas = 10
        print("Tente adivinhar o número que estou pensando entre 1 e 500")
    else:
        print("Entre um numero valido")
    
    numero_secreto = random.randint(1, limite)

    while numero_secreto != input_number and tentativas > 0:
        input_number = input("Digite um número: ")
        
        if input_number.isdigit() and 1 <= int(input_number) <= limite:
            tentativas -= 1
            input_number = int(input_number)
            if input_number == numero_secreto:
                print("Parabéns! Você acertou!")
            elif input_number < numero_secreto:
                print(f"O número secreto é maior do que {input_number}")
                print(f"Você tem {tentativas} tentativas restantes.")
            else:
                print(f"O número secreto é menor do que {input_number}")
                print(f"Você tem {tentativas} tentativas restantes.")
        else:
            print("Por favor, digite um número válido.")

    if tentativas == 0 and numero_secreto != input_number:
        print(f"Suas tentativas acabaram! O número secreto era: {numero_secreto}")
while True:
    jogo()

    jogar_novamente = input("Deseja jogar novamente? (s/n): ".lower())
    if jogar_novamente != "s":
        print("Obrigado por jogar!")
        break