class Movie:
    
    def __init__(self, title, genre, rating):
        """
        Initializes an instance of Movie.

        Args:
            title (str): Title of the movie.
            genre (str): Genre of the movie.
            rating (float): Rating given to the movie.
        """
        self.title = title
        self.genre = genre
        self.rating = rating