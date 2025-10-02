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
    
    def __str__(self):
        return f"{self.title} is a {self.genre} movie."
    
    def display_movie_title(self):
        return f"{self.title}"