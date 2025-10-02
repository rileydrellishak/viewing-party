from viewing_party.user import User
from viewing_party.movie import Movie

movie_a = Movie("The Hunger Games", "Action", 5.0)
movie_b = Movie("Twilight", "Romance", 5.0)
movie_c = Movie("Superman", "Action", 3.5)
movie_d = Movie("The Shining", "Horror", 4.0)
movie_e = Movie("Legally Blonde", "Comedy", 5.0)

# Riley is a generic instance of the class User
riley = User("Riley", [movie_a, movie_b, movie_c], [movie_d, movie_e])

# Gene can test get most watched genre
gene = User("Gene", [movie_a, movie_b, movie_c, movie_d, movie_e])

# Sam can test the swap movie from to watch to watched list
sam = User("Sam", [movie_a], [movie_b, movie_c])