from typing import List, Dict, Union
from .database_connnection import DatabaseConnection


Book = Dict(str,Union(str,int))


def create_book_table() -> None:
    # connection = sqlite3.connect('milestone2_project/data.db')
    with DatabaseConnection('milestone2_project/data.db') as connection: # This is the syntax with DatabaseConnection() 
                                             #create a new object of type database connection as the 'connection' variable can be used inside the context manager 
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
        


def add_book(name: str,author) -> None:
 with DatabaseConnection('milestone2_project/data.db') as connection:
     cursor = connection.cursor()
    
     cursor.execute(f'INSERT INTO books VALUES(?,?,0)',(name,author))
        
        
def get_all_books() -> List[Book]:
        with DatabaseConnection('milestone2_project/data.db') as connection:
            cursor = connection.cursor()
            
            cursor.execute('SELECT * FROM books')
            books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] 

        return books

def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('milestone2_project/data.db') as connection:
        cursor = connection.cursor()
    
        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))

def delete_book(name) -> None:
 with DatabaseConnection('milestone2_project/data.db') as connection:
     cursor = connection.cursor()
    
     cursor.execute('DELETE FROM books WHERE name=?',(name,))

    

