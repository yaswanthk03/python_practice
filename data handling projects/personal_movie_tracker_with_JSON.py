"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""
import os
import json

FILE_NAME = "movies.json"

def naming_convention(name):
    arr = name.split(" ")
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    name = " ".join(arr)
    return name

def load_movies():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_file(movies):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        writer = json.dump(movies, f, indent=4)

def add_movie(movies):
    title = input("Enter movie name: ").strip().lower()
    
    if not title:
        print("Movie title should not be empty.")
        return
    
    title = naming_convention(title)

    for movie in movies:
        if movie["title"] == title:
            print("Name already exists.")
            return
    genres = input("Enter genres in a comma separate (', ') form: \n")
    
    try:
        rating = float(input("Enter the rating in (0 - 10) range: "))
        if not 0 <= rating <= 10:
            raise ValueError
    except ValueError:
        print("Please enter a valid rating.")
    
    movies.append({'title': title, 'genres': genres, 'rating': rating})
    save_file(movies)

def view_movies(movies):
    if not movies:
        print("No movies🎥 logged.")
    for movie in movies:
        print('-' * 60)
        print("Title: {:<40} Rating: {:.2F}\nGenres: {}".format(movie['title'], movie['rating'], movie['genres']))
        
def search_movie_by_title(movies):
    title = input("Enter movie title to search: ").strip().lower()
    if not title:
        print("Movie title should not be empty.")
        return
    
    found_movies = [movie for movie in movies if title in movie['title'].lower()]
    if not found_movies:
        print("No movies found with the given title.")
    else:
        for movie in found_movies:
            print('-' * 60)
            print("Title: {:<40} Rating: {:.2F}\nGenres: {}".format(movie['title'], movie['rating'], movie['genres']))

def search_movie_by_genre(movies):
    genre = input("Enter movie genre to search: ").strip().lower()
    if not genre:
        print("Movie genre should not be empty.")
        return

    found_movies = [movie for movie in movies if genre in movie['genres'].lower()]
    if not found_movies:
        print("No movies found with the given genre.")
    else:
        for movie in found_movies:
            print('-' * 60)
            print("Title: {:<40} Rating: {:.2F}\nGenres: {}".format(movie['title'], movie['rating'], movie['genres']))

def edit_movie(movies):
    title = input("Enter movie title to edit: ").strip().lower()
    if not title:
        print("Movie title should not be empty.")
        return
    for movie in movies:
        if movie["title"].lower() == title:
            new_genres = input("Enter new genres (leave blank to keep current): ").strip()
            if new_genres:
                movie['genres'] = new_genres
            try:
                new_rating_input = input("Enter new rating (0-10) (leave blank to keep current): ").strip()
                if new_rating_input:
                    new_rating = float(new_rating_input)
                    if not 0 <= new_rating <= 10:
                        raise ValueError
                    movie['rating'] = new_rating
            except ValueError:
                print("Please enter a valid rating.")
                return
            save_file(movies)
            print("Movie updated successfully.")
            return
    print("Movie not found.")

def delete_movie(movies):
    title = input("Enter movie title to delete: ").strip().lower()
    if not title:
        print("Movie title should not be empty.")
        return
    for i, movie in enumerate(movies):
        if movie["title"].lower() == title:
            del movies[i]
            save_file(movies)
            print("Movie deleted successfully.")
            return
    print("Movie not found.")

def main():
     print("Welcome to Personal Movie Tracker.")
     movies = load_movies()

     while True:
          print("Options: ")
          print("1. Add a new movie \n2. View all movies \n3. Search for a movie by title")
          print("4. Search for a movie by genre")
          print("5. Edit a movie by title \n6. Delete a movie by title \n7. Exit")

          option = input("Print an option from (1 - 7): ")
          
          match option:
               case '1':
                    add_movie(movies)
               case '2':
                    view_movies(movies)
               case '3':
                    search_movie_by_title(movies)
               case '4':
                    search_movie_by_genre(movies)
               case '5':
                    edit_movie(movies)
               case '6':
                    delete_movie(movies)
               case '7':
                    break
               case _:
                    print("Please choose from only from given options.")
main()