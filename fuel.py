# Exercício: Fuel Gauge
#
# Crie um programa que peça ao usuário uma fração no formato X/Y,
# onde X representa a quantidade de combustível disponível e Y
# representa a capacidade total do tanque.
#
# O programa deve:
#
# 1. Solicitar ao usuário uma fração no formato X/Y.
#
# 2. Converter X e Y para números inteiros.
#
# 3. Calcular a porcentagem de combustível:
#
#       X / Y * 100
#
# 4. Exibir:
#       - "E" se o tanque estiver praticamente vazio (1% ou menos).
#       - "F" se o tanque estiver praticamente cheio (99% ou mais).
#       - A porcentagem normalmente nos demais casos.
#
# 5. Se X ou Y não forem números inteiros, ou se X for maior que Y,
#    solicitar a entrada novamente.
#
# 6. Se Y for 0, também solicitar a entrada novamente.
#
# Exemplo:
#
# Input: 1/4
# Output: 25%
#
# Input: 1/100
# Output: E
#
# Input: 99/100
# Output: F
def tanque():
    resultado = x/y*100
    if resultado <= 1:
        return f"E"
    elif resultado >= 99:
        return f"F"
    else:
        return f"{resultado}%"
    
try:
    fuel_status = input("Please insert the amount of fuel in fractions: ")
    split = fuel_status.split("/")
    x = int(split[0])
    y = int(split[1])
    if y == 0:
       print("You cant divide by zero")
    else: 
        print(tanque())
    
except IndexError:
    print("Please input a fraction as 'x/y'")

