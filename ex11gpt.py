def first_number_index(s):
    for i in range(len(s)):
       if s[i].isdigit():
            return i
    
    return "não tem"


def main():
    string=input("?")
    first_number_index(string)
    print(first_number_index(string))
if __name__ == "__main__":
    main()