from db.migrations.Movies import CreateMoviesTable
from db.migrations.MovieTags import CreateMovieTagsTable
from db.migrations.MovieEntries import CreateMovieEntriesTable


class MigartionConfig:
    tables: list = [
        CreateMoviesTable,
        CreateMovieTagsTable,
        CreateMovieEntriesTable
    ]
