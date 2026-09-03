#plates.py
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numbers_used = False
    if 2 <= len(s) <= 6 and s.isalnum() and s[0].isalpha() and s[1].isalpha():
        for c in s:
            if c.isdigit():
                if not numbers_used:
                    if c == "0":
                        return False
                numbers_used = True
            else:
                if numbers_used:
                    return False
        return True
    return False
        


main()