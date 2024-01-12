# These are the functions that accept other functions as 
# parameters and run them inside their own body.

def greet():
    print("Hello!")
     
def before_and_after(func):
    print("Before")
    func()
    print("After")

before_and_after(lambda: 9)


movies = [
    {"name": "The Matrix", "director" : "Wachowski"},
    {"name": "A beautiful day", "director" : "abcs"},
    {"name": "Catch me if you can", "director" : "wer"},
    {"name": "12th fail", "director" : "indian"},
]

def find_movie(expected,finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie
    
    
    
find_by = input("What property are you searching for?")
looking_for = input("What are you looking for? ")
movie = find_movie(looking_for,lambda movie: movie[find_by])
print(movie or "No movies found")
