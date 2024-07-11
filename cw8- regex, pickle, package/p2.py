import pickle

class FavoriteMovies:
    list_movies = []

    @classmethod
    def add_movie(cls, movie_name):
        cls.list_movies.append(movie_name)

    @classmethod
    def remove_movie(cls, movie_name):
        cls.list_movies.remove(movie_name)

    @classmethod
    def save(cls):
        with open('project2.pickle', 'wb') as w:
            pickle.dump(cls.list_movies, w)

    @classmethod
    def read(cls):
        with open('project2.pickle', 'rb') as r:
            a = pickle.load(r)
            print(a)

a = FavoriteMovies()
a.add_movie('deracula')
a.add_movie('seven')
a.add_movie('five')
a.remove_movie('five')
a.save()
a.read()