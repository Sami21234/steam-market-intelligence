# This file is responsible for handling all database operations related to the Game model. It provides methods to save game records to the database, ensuring that data is inserted or updated as needed.

from pymysql.connections import Connection      # Importing the Connection class from the pymysql library, which is used to establish a connection to a MySQL database.
from models.game import Game        # Importing the Game class from the models.game module, which represents the structure of a game record in the database.

# SQL query to insert or update a game.
# %s is used for parameterized queries in MySQL. It acts as a placeholder for the actual values that will be inserted into the database. This helps prevent SQL injection attacks and allows for dynamic data insertion.

INSERT_GAME_SQL = """
INSERT INTO dim_games
(
    steam_app_id,
    game_name,
    release_date
)
VALUES
(
    %s,     
    %s,
    %s
)
ON DUPLICATE KEY UPDATE

    game_name = VALUES(game_name),

    release_date = VALUES(release_date)
"""

class GameRepository:
    """
    Repository that Handles all database operations for Game.
    """

    def __init__(self, connection: Connection):     # The constructor method initializes the GameRepository class with a database connection. It takes a Connection object as an argument, which is used to interact with the MySQL database.
        self.connection = connection        # Storing the database connection for use in other methods.

    # Save a game record to the database. If a record with the same steam_app_id already exists, it will update the existing record instead of creating a new one.
    def save_game(self, game: Game):
        """
        Insert or update a game record in the database.
        """

        with self.connection.cursor() as cursor:      # Using a context manager to create a cursor object for executing SQL queries. The cursor is automatically closed after the block of code is executed.

            cursor.execute(
                INSERT_GAME_SQL,      # Executing the SQL query defined earlier to insert or update a game record in the database.
                (
                    game.steam_app_id,     # Passing the values from the Game object to be inserted into the database.
                    game.game_name,
                    game.release_date,
                ),
            )
        self.connection.commit()      # Committing the transaction to save changes to the database. This ensures that the inserted or updated data is permanently stored.