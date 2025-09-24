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
    list_movies = user_data["watchlist"]
    for movie in list_movies[:]:
        if movie["title"] == title:
            list_movies.remove(movie)
            user_data["watched"].append(movie)
            break 
    return user_data



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
    
    sum = 0
    list_movies = user_data["watched"]
    if not list_movies:
        return 0.0
    for movie in list_movies:
        sum += movie["rating"]
    return sum / len(list_movies)    


def get_most_watched_genre(user_data):
    """Finds the most frequently occurring genre in the watched movie list.

    Args:
        user_data: A dictionary with a "watched" list of movie dictionaries. Key is "watched" and value is a list of dictionaries. Each watched movie has a genre, represented by a string.

    Returns:
        genre (float): Determines the most frequently occurring genre among the dictionaries of watched movies. Returns None if value of "watched" is an empty list.
    """
    if not user_data["watched"]:
        return None
    
    genre_frequency_dict = {}
    for i in range(0, len(user_data["watched"])):
        if user_data["watched"][i]["genre"] not in genre_frequency_dict:
            genre_frequency_dict[user_data["watched"][i]["genre"]] = 1
        else:
            genre_frequency_dict[user_data["watched"][i]["genre"]] += 1
    
    genres = list(genre_frequency_dict.keys())
    counts = list(genre_frequency_dict.values())
    most_frequent_count = counts[0]
    index_of_most_frequent = 0
    
    for i in range(1, len(counts)):
        if counts[i] > most_frequent_count:
            most_frequent_count = counts[i]
            index_of_most_frequent = i
    
    return genres[index_of_most_frequent]
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    list_unique_movies = []
    list_movies_user_watched = user_data["watched"]
    list_movies_friends_watched = user_data["friends"]

    title_set_user_watched = set()
    title_set_friends_watched = set()

    for movie in list_movies_user_watched:
        title_set_user_watched.add(movie["title"])

    
    for watched_dict in list_movies_friends_watched:
        for movie in watched_dict["watched"]:
            title_set_friends_watched.add(movie["title"])

    unique_title_list = list(title_set_user_watched - title_set_friends_watched)   

    for title in unique_title_list:
        for movie in list_movies_user_watched:
            if movie["title"] == title:
                list_unique_movies.append(movie)
    return list_unique_movies            



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

