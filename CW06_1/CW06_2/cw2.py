class Movie:
    def __init__(self, title, director, duration):
        self._title = title
        self._director = director
        self._duration = duration

        
    def display_detail(self):
        return f"make: {self.title}, model: {self._director}, year: {self._duration}"
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if title=='':
            raise ValueError("Make must be a non-empty string.")
        self._make = title
    
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, director):
        if director=='':
            raise ValueError("Model must be a non-empty string.")
        self._director = director

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if duration <= 0:
            raise ValueError("Year must be a positive integer.")
        self._duration = duration



movie = Movie("raw", "jim ", 120)
print(movie.display_detail())

    
movie.title = "hello"
movie.director = "bob"
movie.duration = 190
print(movie.display_detail())
