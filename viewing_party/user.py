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
        return f"{self.name} just watched {movie.title}.\nNow their watched movie list is {self.watched}."

    def display_watched_movies(self):
        pass

    def display_movie_lists(self):
        watched_movies = []
        to_watch_movies = []
        for i in range(len(self.watched)):
            watched_movies.append(self.watched[i].title)
        for i in range(len(self.to_watch)):
            to_watch_movies.append(self.to_watch[i].title)
        watched_output = ", ".join(watched_movies)
        to_watch_output = ", ".join(to_watch_movies)
        return f"{self.name}'s movie lists!\nWatched: {watched_output}\nTo Watch: {to_watch_output}"