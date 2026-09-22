import random

def jogo():
    print("""
    ╔══════════════════════════════════════╗
    ║         JOGO DE ADIVINHAÇÃO          ║
    ╚══════════════════════════════════════╝
    """)
 
    input_number = None
    limite, tentativas = escolher_dificuldade()

    numero_secreto = random.randint(1, limite)
    numeros_usados = []

    while numero_secreto != input_number and tentativas > 0:
        input_number = input("Digite um número: ")

        if input_number.isdigit() and 1 <= int(input_number) <= limite:
            input_number = int(input_number)

            if input_number in numeros_usados:
                print("Você já tentou esse número")
                print(f"Você tem {tentativas} tentativas restantes.")
                continue

            numeros_usados.append(input_number)
            tentativas -= 1

            print(f"Histórico: {numeros_usados}")

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

def escolher_dificuldade():
    
    while True:
        try:
            dificuldade = int(input("Deseja jogar em qual dificuldade: 1, 2 ou 3? "))       
            
            if dificuldade == 1:
                limite = 50
                tentativas = 10
                print("Tente adivinhar o número que estou pensando entre 1 e 50")
                return limite, tentativas
            elif dificuldade == 2:
                limite = 100
                tentativas = 7
                print("Tente adivinhar o número que estou pensando entre 1 e 100")
                return limite, tentativas
            elif dificuldade == 3:
                limite = 500
                tentativas = 5
                print("Tente adivinhar o número que estou pensando entre 1 e 500")
                return limite, tentativas
            else:
                print("Entre um numero valido")
        except ValueError:
            print("Por favor insira um numero valido")

def main():
    while True:
        jogo()
        while True:
            jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
            if jogar_novamente == "s":
                print("Vamos de novo!")
                break

            elif jogar_novamente == "n":
                print("Obrigado por jogar!")
                return False

            else:
                print("Entre uma resposta válida, (s/n)")
            

main()