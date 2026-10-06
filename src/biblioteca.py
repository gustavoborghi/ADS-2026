books = []
def show_menu():
    while True:
        print("""
    =================================
        BOOK LIBRARY    
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
    book["year"] = input("Publication year?: ")
    books.append(book)
    return book

def list_books():
    
show_menu()
print(books)