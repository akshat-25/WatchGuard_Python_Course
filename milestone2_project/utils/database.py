import json
# Concerned with storing and retrieving books from a list
"""
[
    {
        'name' : 'Clean Code',
        'author' : 'Robert',
        'read' : True
    }
]
"""

books_file = 'milestone2_project/books.json'

def create_book_table():
    with open(books_file,'w') as file:
        json.dump([],file)
       

def _save_all_books(books):
    with open(books_file,'w') as file:
        json.dump(books,file)

         
def get_all_books():
    with open(books_file,'r') as file:
       return json.load(file)

   
def add_book(name,author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)
    
def mark_book_as_read(name):
    books = get_all_books()
    for book in books: 
        if book['name'] == name :
            book['read'] = True
    _save_all_books(books) 
 

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
        
       
        
            
            