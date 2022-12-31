#!./venv/bin/python

import migrate
from db.models.Movie import Movie
from db.models.MovieEntry import MovieEntry
from db.models.MovieTag import MovieTag


def run_tests():

    # migrate.migrate(drop=True)

    print(Movie.getTable())
    print(MovieEntry.getTable())
    print(MovieTag.getTable())

    Movie.create({'title': 'First movie', 'rate': 4.7})
    Movie.create({'title': 'second movie', 'rate': 8.9})

    print("--------------------------------------------------")
    print(f"Columns: {Movie.columns()}")
    print(f"Length of all movies: {len(Movie.all())}")

    id = 1
    movie = Movie.find(id)
    if movie is not None:
        print(f"Found model id: {movie['id']}")
    else:
        print(f"Model with id {id} not found")

    like_cond = '%First%'
    print(f"{like_cond}: {len(Movie.where(['title', 'LIKE', like_cond]))}")


if __name__ == '__main__':

    run_tests()
