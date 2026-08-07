# This file is responsible for connecting and managing the dim_genres table in the database. It contains the GenreRepository class, which provides methods for interacting with the dim_genres table, such as inserting and retrieving genre data.
from pymysql.connections import Connection      # Importing the Connection class from the pymysql library, which is used to establish a connection to a MySQL database.

class GenreRepository:
    """
    Repository responsible for all operations on dim_genres.
    """

    GET_GENRE_SQL = """
    SELECT genre_id
    FROM dim_genres
    WHERE genre_name = %s;
    """

    INSERT_GENRE_SQL = """
    INSERT INTO dim_genres
    (
        genre_name
    )
    VALUES
    (
        %s
    );
    """

    def __init__(self, connection: Connection):
        self.connection = connection

    def get_by_name(self, genre_name: str):
        """
        Retrieve a genre by its name.
        """
        with self.connection.cursor() as cursor:        # Establish a cursor to execute SQL queries on the database connection.
            cursor.execute(
                self.GET_GENRE_SQL,     # Execute the SQL query to retrieve the genre_id based on the provided genre_name.
                (genre_name,)
            )
            return cursor.fetchone()        # fetchone() retrieves a single row from the result.

    def create(self, genre_name: str) -> int:
        """
        Create a new genre and return its ID.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.INSERT_GENRE_SQL,
                (genre_name,)
            )
            self.connection.commit()

            return cursor.lastrowid     # lastrowid returns the integer value of the last inserted row's ID, which is the genre_id of the newly created genre.

    def get_or_create(self, genre_name: str) -> int:    
        """
        Return an existing genre_id or create one.
        """
        genre = self.get_by_name(genre_name)
        if genre:
            return genre["genre_id"]        # If the genre already exists in the database, return its genre_id.
        return self.create(genre_name)