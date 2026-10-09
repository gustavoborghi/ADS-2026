books = []
import json


def show_menu():
    while True:
        print("""
=================================
        LIBRARY
=================================

1 - Add book
2 - Listar livros
3 - Buscar livro
4 - Remover livro
5 - Sair
""")

        try:
            answer = int(input("Choose: "))

            if 1 <= answer <= 5:
                if answer == 1:
                    add_book()
                elif answer == 2:
                    list_books()
                elif answer == 3:
                    search_books()
                elif answer == 4:
                    remove_books()
                elif answer == 5:
                    break
            else:
                print("Por favor, escolha uma opção entre 1 e 5.")

        except ValueError:
            print("Por favor, digite um número válido.")


def add_book():
    book = {}

    book["title"] = input("Title?: ")
    book["author"] = input("Author?: ")

    while True:
        try:
            book["year"] = abs(int(input("Publication year?: ")))
            break
        except ValueError:
            print("Please enter a valid year")

    books.append(book)


def list_books():
    for book in books:
        print(book)


def search_books():

    while True:
        print('''=================================
        SEARCH BOOKS
=================================

1 - Search by title
2 - Search by author
3 - Search by year
4 - Back to menu)''')

        try:
            answer = int(input("Choose: "))

            if 1 <= answer <= 4:

                if answer == 1:
                    search = input("Search: ").lower()
                    for book in books:
                        if  search in book["title"].lower():
                            print(book)
                        else:
                            print("No books found")

                elif answer == 2:
                    search = input("Search: ").lower()
                    for book in books:
                        if  search in book["author"].lower():
                            print(book)
                        else:
                            print("No books found")

                elif answer == 3:
                    try:
                        search = abs(int(input("Search: ")))
                        for book in books:
                            if  search == book["year"]:
                                print(book)
                            else:
                            print("No books found")

                    except ValueError:
                        print("Please enter a valid year")

                elif answer == 4:
                    break

            else:
                print("Please enter a number between 1 and 4")

        except ValueError:
            print("Por favor, digite um número válido.")


def remove_books():
    print("Função remove_books")


show_menu()
