# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Create a movie dictionary with title, genre, and rating.
    Return None if any field is missing.
    """
    if not title or not genre or not rating:
        return None
    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    """
    Add a movie to the user's watched list and return updated user_data.
    """
    if not user_data["watched"]:
        user_data["watched"] = [movie]
    else:
        user_data["watched"].append(movie)    
    return user_data


def add_to_watchlist(user_data, movie):
    """
    Add a movie to the user's watchlist and return updated user_data.
    """
    if not user_data["watchlist"]:
        user_data["watchlist"] = [movie]
    else:
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

        user_data = {"watched":
            [{title:"", genre:"", rating: float}, 
            {title:"", genre:"", rating: float}]
            }

    Returns:
        genre (str): Determines the most frequently occurring genre among the dictionaries of watched movies. Returns None if value of "watched" is an empty list.
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
    """
    Return movies watched only by the user, not by any friends.

    Args:
        user_data (dict): Contains "watched" (list of movies) and "friends" (list of friends with their watched movies).
        user_data = {"watched":
            [{title:"", genre:"", rating: float}, 
            {title:"", genre:"", rating: float}],
            "friends":[{"watched": {title:"", genre:"", rating: float}},
            {"watched": {title:"", genre:"", rating: float}}]
            }

    Returns:
        list of dict: Movies unique to the user.
        list_unique_movies = [
            {title:"", genre:"", rating: float},
            {title:"", genre:"", rating: float},
            {title:"", genre:"", rating: float}
        ]
    """
    list_unique_movies = []
    list_movies_user_watched = user_data["watched"]
    list_movies_friends_watched = user_data["friends"]

    titles_set_friends_watched = set()
    for watched_dict in list_movies_friends_watched:
        for movie in watched_dict["watched"]:
            title = movie["title"]
            if title:
                titles_set_friends_watched.add(title)

    watched = set()
    for movie in list_movies_user_watched:
        title = movie["title"]
        if title and title not in titles_set_friends_watched and title not in watched:
            list_unique_movies.append(movie)
            watched.add(title)
    return list_unique_movies  

def get_friends_unique_watched(user_data): 
    """Synthesizes all the movies a group of friends have watched into a single list of movies (dictionaries) that the user has not watched and at least one of the user's friends has watched.

    Args:
        user_data: A dictionary with a three key-value pairs.
            user_data = {"watched":
                [{title:"", genre:"", rating: float}, 
                {title:"", genre:"", rating: float}],
                "friends":[{"watched": {title:"", genre:"", rating: float}},
                {"watched": {title:"", genre:"", rating: float}}]
            }

    Returns:
        list: Each item in the list is a dictionary of a movie that the user has not watched but at least one of the user's friends has watched.
        yes_friend_no_user = [
            {title:"", genre:"", rating: float},
            {title:"", genre:"", rating: float},
            {title:"", genre:"", rating: float}
        ]
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
    """Determine a list of recommended movies where the user has not watched it, at least one of the user's friends has watched, and the host of the movie is a service that is in the user's subscriptions.

    Args:
        user_data: A dictionary with a three key-value pairs.
            Key "watched" whose value is a list of movie dictionaries
            Key "friends" where the value of "friends" is a list. Each item in the list is a dictionary. Each dictionary has a key "watched" and a value of the list of movie dictionaries the friend has watched. Each movie dictionary has a value for the keys "title", "genre", "rating", and "host".
            Key "subscription" is a list of strings representing the streaming subscription the user has

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
    """Determine a list of recommended movies based on user's most frequently watched genre. Movies in the list should not be in the user's watched movies, at least one of the user's friends has watched it,  and the genre of the movie is the user's most frequent genre.

    Args:
        user_data: Three key-value pairs.
            Key "watched" whose value is a list of movie dictionaries
            Key "friends" where the value of "friends" is a list. Each item in the list is a dictionary. Each dictionary has a key "watched" and a value of the list of movie dictionaries the friend has watched. Each movie dictionary has a value for the keys "title", "genre", "rating", and "host".
            Key "subscription" has a value of a list of strings representing the streaming subscription the user has

    Returns:
        list of dictionaries: A list of movies that the user has not watched, at least one of their friends has watched, and the genre matches the user's most frequented genre
    """
    movie_recs = []
    
    watched_by_friends = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    for movie in watched_by_friends:
        if movie["genre"] == most_watched_genre:
            movie_recs.append(movie)

    return movie_recs

def get_rec_from_favorites(user_data):
    """Determine a list of recommended movies from movies that none of the user's friends have watched and the movie is in the user's favorites.

    Args:
        user_data: Four key-pair values
            Key "watched" whose value is a list of movie dictionaries
            Key "friends" where the value of "friends" is a list. Each item in the list is a dictionary. Each dictionary has a key "watched" and a value of the list of movie dictionaries the friend has watched. Each movie dictionary has a value for the keys "title", "genre", "rating", and "host".
            Key "subscription" has a value of a list of strings representing the streaming subscription the user has.
            Key "favorites" has a value of a list of movie dictionaries, representing the user's favorite movies.
    Returns:
        list of dictionaries: A list of movies that the user has not watched, at least one of their friends has watched, and the genre matches the user's most frequented genre
    """
    movie_recs = []
    friends_not_watched = get_unique_watched(user_data)


    for movie in user_data["favorites"]:
        if movie in friends_not_watched:
            movie_recs.append(movie)
    
    return movie_recs