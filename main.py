from viewing_party.user import User
from viewing_party.movie import Movie

the_hunger_games = Movie("The Hunger Games", "Action", 5.0)
twilight = Movie("Twilight", "Romance", 5.0)
superman = Movie("Superman", "Action", 3.5)
the_shining = Movie("The Shining", "Horror", 4.0)
legally_blonde = Movie("Legally Blonde", "Comedy", 5.0)

riley = User("Riley", [the_hunger_games, legally_blonde, twilight], [superman, the_shining])

print(riley.swap_movie_from_to_watch_to_watched(the_shining))