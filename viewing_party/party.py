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


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

