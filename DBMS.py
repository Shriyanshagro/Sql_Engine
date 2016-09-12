# Author = Shriyansh Agrawal

import engine
import itertools

def main():
    Database = engine.Database(name = 'Assignment 1', tables=[])

    Database.create_database()

    Database.load_contents()

    # Database.print_database()

    # Database.delete_table('table1')
    Database.get_table('table1')

if __name__ == "__main__":
    main()
