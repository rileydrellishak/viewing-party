from viewing_party.user import User
from viewing_party.movie import Movie

movie_a = Movie("The Hunger Games", "Action", 5.0)
movie_b = Movie("Twilight", "Romance", 5.0)
movie_c = Movie("Superman", "Action", 3.5)
movie_d = Movie("The Shining", "Horror", 4.0)
movie_e = Movie("Legally Blonde", "Comedy", 5.0)

riley = User("Riley", [movie_a, movie_b, movie_c], [movie_d, movie_e])

# print(riley.display_movie_lists())

print(riley.swap_movie_from_to_watch_to_watched(movie_e))