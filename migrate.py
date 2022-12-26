#!./venv/bin/python

import sys
from functools import reduce

from db.migrations.tables.movies import CreateMoviesTable
from db.migrations.tables.movie_tags import CreateMovieTagsTable
from db.migrations.tables.movie_entries import CreateMovieEntriesTable
from db.database import Database


def is_drop_table():
    drop_parameter_index: int = 1
    drop_parameter_value: str = 'drop'

    return (0 < drop_parameter_index < len(
        sys.argv)) and (sys.argv[drop_parameter_index] == drop_parameter_value)


if __name__ == '__main__':

    print("--------------------------------------------------")
    print("Migration Started")
    db: Database = Database()
    drop_tables: bool = is_drop_table()

    if drop_tables:
        print(">>> All Tables will be dropped")
    print("--------------------------------------------------")

    CreateMoviesTable(db).create_table(drop=drop_tables)
    CreateMovieTagsTable(db).create_table(drop=drop_tables)
    CreateMovieEntriesTable(db).create_table(drop=drop_tables)

    print("--------------------------------------------------")
    print("Migration Done")
    print("--------------------------------------------------")
