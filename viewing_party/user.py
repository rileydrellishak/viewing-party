class User:

    def __init__(self, name="User", watched=None, to_watch=None):
        """
        Initializes an instance of User.

        Args:
            name (str): A string literal representing the user's name
            watched: A list of instances of the class Movie, representing movies the user has watched.
            to_watch: A list of instances of the class Movie, representing movies the user wants to watch.
        """
        self.name = name
        self.watched = watched if watched is not None else []
        self.to_watch = to_watch if watched is not None else []
    
    def swap_movie_from_to_watch_to_watched(self, movie):
        """
        Moves a movie from a user's to watch list to their watched list.

        Args:
            movie: An instance of the class Movie. Represents the movie the user wants to move.
        """
        self.to_watch.remove(movie)
        self.watched.append(movie)

    def display_watched_movie_list(self):
        watched = [movie.title for movie in self.watched]
        return f"{self.name}'s watchlist: {watched}"
    
    def display_to_watch_movie_list(self):
        to_watch = [movie.title for movie in self.to_watch]
        return f"{self.name}'s watchlist: {to_watch}"