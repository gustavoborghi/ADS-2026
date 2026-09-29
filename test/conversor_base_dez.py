# Pega os valores do usuário
basedez = int(input("Entre a base 10: "))
sisnum = int(input("Entre o sistema numérico que deseja (2, 8 ou 16): "))

# Converte
resultado = []
digitos = "0123456789ABCDEF"

if sisnum not in (2, 8, 16):
    print("Base inválida!")

elif basedez < 0:
    print("Digite um número positivo!")

elif basedez == 0:
    print("Resultado: 0")

else:
    while basedez > 0:
        resto = basedez % sisnum
        resultado.append(digitos[resto])
        basedez = basedez // sisnum

    resultado.reverse()
    resultado = "".join(resultado)

    print(f"Resultado: {resultado}")