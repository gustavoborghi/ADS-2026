#Exercício 13 — valid_password versão 2
#Um username é válido se:
    #tiver entre 3 e 12 caracteres;
    #começar com uma letra;
    #tiver apenas letras e números.

def valid_username(username):
    if len(username) < 3 or len(username) > 12:
        return False
    for caractere in range(len(username)):
        if not username[caractere].isalpha():
            return False
        if not username[caractere].isalnum():
            return False
    
    return True
            
def main():
    username = input("Username: ")
    print(valid_username(username))
main()