peso = float(input("Qual seu peso? "))
altura= float(input("Qual sua altura? "))

imc = peso / (altura * altura)

print(imc)
if imc < 22:
    print("Magro")
if imc >= 22 and imc <= 26:
    print("Ideal")
if imc > 26:
    print("Acima do peso")
