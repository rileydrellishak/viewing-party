# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    """
    Create a movie dictionary with title, genre, and rating.
    Return None if any field is missing.
    """
    if not title or not genre or not rating:
        return None
    movie = {"title": title,
            "genre": genre,
            "rating": rating}
    return movie

def add_to_watched(user_data, movie):
    """
    Add a movie to the user's watched list and return updated user_data.
    """
    user_data["watched"].append(movie)    
    return user_data

def add_to_watchlist(user_data, movie):
    """
    Add a movie to the user's watchlist and return updated user_data.
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """Create a dictionary that represents a single movie. If any inputs are falsy, return None.
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
    """
    Return the average rating of all movies in the user's watched list.
    If the list is empty, return 0.0.
    """
    rating_total = 0.0
    list_movies = user_data["watched"]
    if not list_movies:
        return 0.0
    for movie in list_movies:
        rating_total += movie["rating"]
    return rating_total / len(list_movies)    


def get_most_watched_genre(user_data):
    """Finds the most frequently occurring genre in the watched movie list.

    Args:
        user_data (dictionary):
            "watched": List of dictionaries that represent movies the user has watched.
                Movie dictionaries has the following key-value pairs:
                    title (str)
                    genre (str)
                    rating (float)

    Returns:
        genre (str): Determines the most frequently occurring genre among the dictionaries of watched movies. Returns None if value of "watched" is an empty list.
    """
    if not user_data["watched"]:
        return None
    
    genre_frequency = {}
    for movie in user_data["watched"]:
        genre_frequency[movie["genre"]] = genre_frequency.get(movie["genre"], 0) + 1
    
    most_watched_genre = ""
    most_watched_genre_count = 0
    for genre, count in genre_frequency.items():
        if count > most_watched_genre_count:
            most_watched_genre = genre
            most_watched_genre_count = count
    
    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    """
    Return a list of movies that appear in the user's watched list
    but are not present in any friend's watched list.
    Each movie is represented as a dictionary with title, genre, and rating.
    """
    unique_movies = []
    user_watched = user_data["watched"]
    friends = user_data["friends"]

    friends_title = set()
    for watched_dict in friends:
        for movie in watched_dict["watched"]:
            title = movie["title"]
            if title:
                friends_title.add(title)

    watched = set()
    for movie in user_watched:
        title = movie["title"]
        if title and title not in friends_title and title not in watched:
            unique_movies.append(movie)
            watched.add(title)
    return unique_movies  

def get_friends_unique_watched(user_data):
    """Synthesizes all the movies a group of friends have watched into a single list of movies (dictionaries) that the user has not watched and at least one of the user's friends has watched.

    Args:
        user_data (dictionary):
            "watched": List of dictionaries that represent movies the user has watched.
                Movie dictionaries has the following key-value pairs:
                    title (str)
                    genre (str)
                    rating (float)
            "friends": A list of dictionaries. Each dictionary is a friend.
                Friend dictionaries have the following key-value pairs:
                    "watched": List of dictionaries that represent movies the friend has watched.
                        Movie dictionaries has the following key-value pairs:
                            title (str)
                            genre (str)
                            rating (float)

    Returns:
        list of dict: Movies unique to the friends (movies the user has not watched). Each dictionary represents a movie. The movie dictionaries has the following key-value pairs:
            title (str)
            genre (str)
            rating (float)
    """ 
    user_watched_movies = []
    friends_watched_movies = []
    yes_friend_no_user = []

    for movie in user_data["watched"]:
        user_watched_movies.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)

    for movie in friends_watched_movies:
        if movie not in user_watched_movies:
            yes_friend_no_user.append(movie)
    
    return yes_friend_no_user
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """
    Return a list of movies recommended to the user.
    A movie is recommended if at least one friend has watched it,
    the user has not, and its host matches the user's subscriptions.
    """
    recommend_movies = []
    subscriptions = user_data["subscriptions"]

    yes_friend_no_user = get_friends_unique_watched(user_data)
    for movie in yes_friend_no_user:
        if movie["host"] in subscriptions:
            recommend_movies.append(movie)
    return recommend_movies        
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    """Determine a list of recommended movies based on user's most frequently watched genre. Movies in the list should not be in the user's watched movies, at least one of the user's friends has watched it, and the genre of the movie is the user's most frequent genre.

    Args:
        user_data (dictionary):
            "watched": List of dictionaries that represent movies the user has watched.
                Movie dictionaries has the following key-value pairs:
                    title (str)
                    genre (str)
                    rating (float)
            "friends": A list of dictionaries. Each dictionary is a friend.
                Friend dictionaries have the following key-value pairs:
                    "watched": List of dictionaries that represent movies the friend has watched.
                        Movie dictionaries has the following key-value pairs:
                            title (str)
                            genre (str)
                            rating (float)

    Returns:
        list of dictionaries: A list of movies that the user has not watched, at least one of their friends has watched, and the genre matches the user's most frequented genre
    """
    watched_by_friends = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    movie_recs = []

    for movie in watched_by_friends:
        if movie["genre"] == most_watched_genre:
            movie_recs.append(movie)

    return movie_recs

def get_rec_from_favorites(user_data):
    """Determine a list of recommended movies from movies that none of the user's friends have watched and the movie is in the user's favorites.

    Args:
        user_data (dictionary):
            "watched": List of dictionaries that represent movies the user has watched.
                Movie dictionaries has the following key-value pairs:
                    title (str)
                    genre (str)
                    rating (float)
            "friends": A list of dictionaries. Each dictionary is a friend.
                Friend dictionaries have the following key-value pairs:
                    "watched": List of dictionaries that represent movies the friend has watched.
                        Movie dictionaries has the following key-value pairs:
                            title (str)
                            genre (str)
                            rating (float)
            "favorites": A list of dictionaries. Each dictionary is a movie, representing the user's favorite movies.
    Returns:
        list of dictionaries: A list of movies that the user has not watched, at least one of their friends has watched, and the genre matches the user's most frequented genre
    """
    friends_not_watched = get_unique_watched(user_data)
    movie_recs = []

    for movie in user_data["favorites"]:
        if movie in friends_not_watched:
            movie_recs.append(movie)
    
    return movie_recs