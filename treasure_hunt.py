import random

def choose_position(row_size, column_size):
    #Function to get a guess from the user
    
    while True: 
        try:
            guess = input("Where is the treasure? Input as row/column\n> ")
            position = guess.split("/")

            guess_row = int(position[0])
            guess_column = int(position[1])

            if 1<= guess_row <= row and 1 <= guess_column <= column:
                return guess_row, guess_column
                
            else:
                print("Please insert a valide answer")
        except ValueError:
            print("Please insert a valide answer")
        except IndexError:
            print("Please insert a valide answer")

def choose_dificulty():
    #Function to get a dificulty from the user, wich defines the amount of tries and the size of the square

    while True:

        difficulty = input("Do you want to play at which dificulty?\nE, M or H\n> ")
        
        if difficulty not in ("E", "M", "H"):
                print("Please insert a valid answer")
                continue
                
        if difficulty == "E":
                tries = 10
                row_size = 5
                column_size = 5

        elif difficulty == "M":
                tries = 7
                row_size = 7
                column_size = 7

        elif difficulty == "H":
                tries = 5
                row_size = 10
                column_size = 10

        return row_size, column_size, tries

def game():
    row_size, column_size, tries = choose_dificulty()
    
    treasure_row = random.randint(1, row)
    treasure_column = random.randint(1, column)
    
    while tries > 0:
        guess_row, guess_column = choose_position(row_size, column_size)
        if treasure_column == guess_column  and treasure_row == guess_row:
            print("Congratulations you've won!")
            return
        if treasure_row > guess_row:
            print("The treasure is south of your guess")
            tries -= 1
            continue    
        elif treasure_row < guess_row:
            print("The treasure is north of your guess")
            tries -= 1
            continue
        elif treasure_column > guess_column:
            print("The treasure is east of your guess")
            tries -= 1
            continue
        elif treasure_column < guess_column:
            print("The treasure is west of your guess")
            tries -= 1
            continue
        
game()