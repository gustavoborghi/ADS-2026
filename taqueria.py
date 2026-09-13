# Exercício — Felipe's Taqueria
#
# Crie um programa que registre os pedidos de uma taqueria.
#
# O programa deve:
#
# 1. Criar um dicionário contendo os itens do menu e seus preços:
#
#    Baja Taco: $4.25
#    Burrito: $7.50
#    Bowl: $8.50
#    Nachos: $11.00
#    Quesadilla: $8.50
#    Super Burrito: $8.50
#    Super Quesadilla: $9.50
#    Taco: $3.00
#    Tortilla Salad: $8.00
#
# 2. Solicitar ao usuário o nome de um item.
#
# 3. Se o item existir no dicionário, adicionar seu preço ao total.
#
# 4. Se o item não existir, ignorar a entrada e continuar.
#
# 5. Continuar solicitando pedidos até que o usuário pressione
#    Ctrl+D, gerando uma exceção EOFError.
#
# 6. Ao finalizar, exibir o total da conta no formato:
#
#    Total: $12.75
#
# O programa deve aceitar os itens independentemente de o usuário
# digitá-los com letras maiúsculas ou minúsculas.
#
# Tema principal:
# dicionários, while, try/except, EOFError e formatação de valores.


menu = {
"Baja Taco" : "$4.25",
"Burrito" : "$7.50",
"Bowl" : "$8.50",
"Nachos" : "$11.00",
"Quesadilla" : "$8.50",
"Super Burrito" : "$8.50",
"Super Quesadilla" : "$9.50",
"Taco" : "$3.00",
"Tortilla Salad" : "$8.00"
}
for key, value in menu.items():
    print(key, value)