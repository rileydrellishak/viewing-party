# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    if not user_data["watched"]:
        user_data["watched"] = [movie]
    else:
        user_data["watched"].append(movie)    
    return user_data


def add_to_watchlist(user_data, movie):
    if not user_data["watchlist"]:
        user_data["watchlist"] = [movie]
    else:
        user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    list_movies = user_data["watchlist"]
    for movie in list_movies[:]:
        if movie["title"] == title:
            list_movies.remove(movie)
            user_data["watched"].append(movie)
            break 
    return user_data

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

