def first_number_is_zero(s):
    for caractere in s:
       if caractere.isdigit():
            if caractere == "0":
                return True
            else:
                return False
    return False         
def main():
    string=input("?")
    print(first_number_is_zero(string))
if __name__ == "__main__":
    main()