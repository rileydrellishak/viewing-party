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
    
    def stringify_movie_lists(self):
        watched_movies = []
        to_watch_movies = []
        for i in range(len(self.watched)):
            watched_movies.append(self.watched[i].display_movie_title())
        for i in range(len(self.to_watch)):
            to_watch_movies.append(self.to_watch[i].display_movie_title())
        watched_output = ", ".join(watched_movies)
        to_watch_output = ", ".join(to_watch_movies)
        return watched_output, to_watch_output

    def display_movie_lists(self):
        tuple_of_movie_lists = self.stringify_movie_lists()
        return f"{self.name}'s movie lists!\nWatched: {tuple_of_movie_lists[0]}\nTo Watch: {tuple_of_movie_lists[1]}"
    
    def swap_movie_from_to_watch_to_watched(self, movie):
        """
        Moves a movie from a user's to watch list to their watched list.

        Args:
            movie: An instance of the class Movie. Represents the movie the user wants to move.
        """
        self.to_watch.remove(movie)
        self.watched.append(movie)
        return f"{self.display_movie_lists()}"

    def get_most_watched_genre(self):
        genre_frequency_map = {}
        for movie in self.watched:
            genre_frequency_map[movie.genre] = genre_frequency_map.get(movie.genre, 0) + 1
        
        for genre, frequency in genre_frequency_map.items():
            if frequency == max(genre_frequency_map.values()):
                return genre