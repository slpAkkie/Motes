from abc import ABC

from db.migrations.Movies import CreateMoviesTable
from db.migrations.MovieTags import CreateMovieTagsTable
from db.migrations.MovieEntries import CreateMovieEntriesTable


class MigartionConfig(ABC):
    tables: list = [
        CreateMoviesTable,
        CreateMovieTagsTable,
        CreateMovieEntriesTable
    ]
