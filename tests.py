#!./venv/bin/python

from migrate import migrate
from db.models.Movie import Movie
from db.models.MovieEntry import MovieEntry
from db.models.MovieTag import MovieTag


def run_tests():

    # migrate(drop=True)

    print('--------------------------------------------------')
    print('Auto table detection')
    print()
    print('Movie: ' + Movie.getTable())
    print('Movie: ' + MovieEntry.getTable())
    print('Movie: ' + MovieTag.getTable())

    print('--------------------------------------------------')
    print('Create DB query')
    print()
    Movie.create({'title': 'First movie', 'rate': 4.7})
    Movie.create({'title': 'second movie', 'rate': 8.9})

    print('--------------------------------------------------')
    print('DB Info')
    print()
    print(f'Columns: {Movie.columns()}')
    print(f'Total Movie count: {len(Movie.all())}')

    print('--------------------------------------------------')
    print('DB Query')
    print()
    id = 1
    movie = Movie.find(id)
    if movie is not None:
        print(f"Find model with [id = {id}]: {movie['title']}")
    else:
        print(f'Find model with [id = {id}]: [Nothing]')
    like_cond = '%First%'
    like_cond_model_count = len(Movie.where(['title', 'LIKE', like_cond]))
    print(f"Count of model [title LIKE {like_cond}]: {like_cond_model_count}")


if __name__ == '__main__':

    run_tests()
