from app import books

USER_CHOICE = '''
Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalouge
- 'q' to exit


Enter your choice
'''

def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating*-1)[:10]
    for book in best_books:
        print(book)
        
books_generator = (x for x in books)

def get_next_book():
    print(next(books_generator))

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q' :
        if user_input == 'b':
            print_best_books
        else:
            print('Please select valid input!')
        user_input = input(USER_CHOICE)
        