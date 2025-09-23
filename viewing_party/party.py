# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """Create a dictionary with key-value pairs. A dictionary represents a single movie.
    Keys are title, genre, and rating (str).
    Values are respective titles (str), genres (str), and ratings (float) for a movie.
    If any inputs are falsy, return None.
    Args:
        title (str): Title of movie.
        genre (str): Gener of movie.
        rating (float): Rating given to movie.

    Returns:
        dict: represents a movie with information about its title, genre, and rating.
    """
    # check: if not title or not movie or not rating: return None
    # create a dictionary called movie = {}
    # movie["title"] = title
    # movie["genre"] = genre
    # movie["rating"] = rating
    # return movie
    pass

def add_to_watched(user_data, movie):
    """Adds a dictionary of movie data to a list of user's watched movies.

    Args:
        user_data: A  dictionary where key is "watched" and value is a list of dictionaries that represent movies user has watched.
        movie: A dictionary with key-value pairs representing the title, genre, and rating of a watched movie.

    Returns:
        list: user_data with the movie dictionary appended to the value of the "watched" key in user_data..
    """
    # movie is a pre-made dictionary. must append the dictionary to the list that is the value of the key "watched" in the list 
    # user_data["watched"] results in a list of movies
    # append movie to user_data["watched"]
    # return user_data
    pass

def add_to_watchlist(user_data, movie):
    """Adds a dictionary of movie data to a list of user's movies they want to watch.

    Args:
        user_data: A list of dictionaries where dictionaries represent movies user wants to watch.
        movie: A dictionary with key-value pairs representing the title, genre, and rating of a movie the user wants to watch.

    Returns:
        list: user_data with the movie dictionary appended.
    """
    pass

def watch_movie(user_data, title):
    """Given a movie title, find the movie title in the "watchlist" value (list of movies as dictionaries). Moves a movie from "watchlist" to "watched."

    Args:
        user_data: A dictionary with two keys - "watchlist" and "watched." Respective values are lists of movies (dictionaries).
        title (str): The title of the movie the user has watched

    Return:
        user_data: A dictionary where the values of "watchlist" and "watched" are updated to reflect a movie has passed from watchlist to watched. 
    """
    pass
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """Calculates the average rating of all the movies in the "watched" movie list.

    Args:
        user_data: A dictionary with a "watched" list of movie dictionaries. Key is "watched" and value is a list of dictionaries. Each movie has a rating, represented by a float.

    Returns:
        average (float): Calculates the average rating of all the movies in the watched list. Returns 0.0 if value of "watched" is an empty list.
    """
    pass

def get_most_watched_genre(user_data):
    """Finds the most frequently occurring genre in the watched movie list.

    Args:
        user_data: A dictionary with a "watched" list of movie dictionaries. Key is "watched" and value is a list of dictionaries. Each watched movie has a genre, represented by a string.

    Returns:
        genre (float): Determines the most frequently occurring genre among the dictionaries of watched movies. Returns None if value of "watched" is an empty list.
    """
    pass
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

