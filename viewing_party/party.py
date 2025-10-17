# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    """
    Create a movie dictionary with title, genre, and rating.
    Return None if any field is missing.
    """
    if not title or not genre or not rating:
        return None
    
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

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
    """
    Finds a movie by title in the user_data's watchlist and "moves" it from watchlist to watched.

    Args:
        title (str): Title of movie.
        genre (str): Gener of movie.
        rating (float): Rating given to movie.

    Returns:
        dict: represents user_data with updated movie lists.
    """
    # List of movie dictionaries in user watchlist
    list_movies = user_data["watchlist"]

    # Makes a filtered list that contains the movies NOT being watched
    filtered_movies = []
    for movie in list_movies:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            continue

        # This only runs if the movie is not the one being watched
        filtered_movies.append(movie)
    
    # Updates the watchlist to reflect that the movie with provided title is removed
    user_data["watchlist"] = filtered_movies

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
    """
    Return the genre that the user has watched most often.
    Args:
        user_data (dict): A dictionary representing a user's movie data. Expected to contain
            a "watched" key mapping to a list of movie dictionaries, each with a "genre" key whose value is a string.
    Returns:
        str or None: The genre with the highest watch count, or None if the user has no watched movies. If multiple genres are tied for the highest count, one of them is returned (selection depends on iteration order).
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
        if title not in friends_title and title not in watched:
            unique_movies.append(movie)
            watched.add(title)
    return unique_movies  

def get_friends_unique_watched(user_data):
    '''
    Return a list of movies that any of the user's friends have watched but the user has not.
    Args:
        user_data (dict): A dictionary describing the user and their friends. Expected keys:
            - "watched": list of movie dictionaries the user has watched.
            - "friends": list of friend dictionaries, each with a "watched" key containing a list of movie dictionaries.
    Returns:
        list: A list of movie dictionaries representing movies that appear in at least one friend's "watched" list but do not appear in the user's "watched" list. Each movie appears at most once in the returned list (duplicate friend entries are not included).
    Example:
        >>> user_data = {
        ...     "watched": [{"title": "A"}, {"title": "B"}],
        ...     "friends": [
        ...         {"watched": [{"title": "B"}, {"title": "C"}]},
        ...         {"watched": [{"title": "C"}, {"title": "D"}]}
        ...     ]
        ... }
        >>> get_friends_unique_watched(user_data)
        [{"title": "C"}, {"title": "D"}]
    '''
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
    """
    Return friend-recommended movies (that the user hasn't seen) in the user's top genre.

    Args:
        user_data (dict): User data containing "watched" and "friends" lists.

    Returns:
        list: Movie dicts from friends matching the user's most-watched genre.
    """
    watched_by_friends = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    movie_recs = []

    for movie in watched_by_friends:
        if movie["genre"] == most_watched_genre:
            movie_recs.append(movie)

    return movie_recs

def get_rec_from_favorites(user_data):
    """Return the user's favorite movies that none of their friends have watched.

    Args:
        user_data (dict): Should include keys "favorites", "watched", and "friends".
    Returns:
        list: Favorite movie dicts not found in any friend's watched lists.
    """
    friends_not_watched = get_unique_watched(user_data)
    movie_recs = []

    for movie in user_data["favorites"]:
        if movie in friends_not_watched:
            movie_recs.append(movie)
    
    return movie_recs