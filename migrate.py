#!./venv/bin/python

import sys
from functools import reduce

from db.Database import Database
from config.Migration import MigartionConfig


def is_drop_table():
    drop_parameter_index: int = 1
    drop_parameter_value: str = '--drop'

    return (0 < drop_parameter_index < len(
        sys.argv)) and (sys.argv[drop_parameter_index] == drop_parameter_value)


if __name__ == '__main__':

    db: Database = Database()
    drop_tables: bool = is_drop_table()

    print("--------------------------------------------------")
    print("Migration Started")

    if drop_tables:
        print("!!! All Tables will be dropped !!!")

    print("--------------------------------------------------")

    for migration in MigartionConfig.tables:
        migration(db).create_table(drop=drop_tables)

    print("--------------------------------------------------")
    print("Migration Done")
    print("--------------------------------------------------")
