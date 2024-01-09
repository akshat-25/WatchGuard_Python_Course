MENU_PROPMT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find movie by title or 'q' to quit" 
movies = []

def add_movies():
    title = input("Enter the title of the movie")
    director = input("Enter the director of the movie")
    year = input("Enter the releasing year of the movie")
     
    movies.append({
        "title" : title,
        "director" : director,
        "year" : year
    })
    
def show_movies():
    for movie in movies:
        print_movie(movie)
 
def print_movie(movie):
    print(f"Title : {movie['title']} ")
    print(f"Director : {movie['director']}")
    print(f"Year : {movie['year']}")
    
def find_movies():
    search_title = input("Enter movie title")
    
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)
        

user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": find_movie
}

def menu():
    selection = input(MENU_PROPMT)
    while selection != 'q':
        if selection in user_options:
            selection_function = user_options[selection]
            selection_function()
        else:
            print("Invalid Input! Please try again")
            selection = input(MENU_PROPMT)
        
menu()