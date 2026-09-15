import random

def choose_position():
    while True: 
        try:
            guess = input("Where is the treasure? (input as row/column): ")
            position = guess.split("/")

            row = int(position[0])
            column = int(position[1])

            if 1<= row <= 5 and 1 <= column <= 5:
                return row, column
                
            else:
                print("Please insert a valide answer")
        except ValueError:
            print("Please insert a valide answer")
        except IndexError:
            print("Please insert a valide answer")

def game():
    
    treasure_column = random.randint(1, 5)
    treasure_row = random.randint(1, 5)
    row, column = choose_position()

    if treasure_column == column  and treasure_row == row:
        print("Congratulations you've won!")
    elif treasure_column > column:
        print("")
    
