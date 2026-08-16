# This file is responsible for inserting relationships between dimension tables in the database. It contains the BridgeRepository class, which provides methods for inserting data into the dim_bridge table, which represents the relationships between games and platforms.
from pymysql.connections import Connection      # Importing the Connection class from the pymysql library, which is used to establish a connection to a MySQL database.

class BridgeRepository:
    """
    Repository responsible for inserting
    relationships between dimension tables.
    """

    INSERT_GAME_DEVELOPER_SQL = """
    INSERT IGNORE INTO bridge_game_developers
    (
        game_id,
        developer_id
    )
    VALUES
    (
        %s,
        %s
    );
    """

    INSERT_GAME_PUBLISHER_SQL = """
    INSERT IGNORE INTO bridge_game_publishers
    (
        game_id,
        publisher_id
    )
    VALUES
    (
        %s,
        %s
    );
    """

    INSERT_GAME_GENRE_SQL = """
    INSERT IGNORE INTO bridge_game_genres
    (
        game_id,
        genre_id
    )
    VALUES
    (
        %s,
        %s
    );
    """

    INSERT_GAME_PLATFORM_SQL = """
    INSERT IGNORE INTO bridge_game_platforms
    (
        game_id,
        platform_id
    )
    VALUES
    (
        %s,
        %s
    );
    """

    def __init__(self, connection: Connection):
        self.connection = connection


    # Function to link the relation between dim_game & publisher.
    def link_game_publisher(self, game_id: int, publisher_id: int):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.INSERT_GAME_PUBLISHER_SQL,     # Execute the SQL query to insert a relationship between a game and a publisher into the bridge_game_publishers table.
                (
                    game_id, 
                    publisher_id,
                )
            )
        self.connection.commit()        # Commit the transaction to save the changes to the database.

    # Function to link the relation between dim_game & developer.
    def link_game_developer(
            self,
            game_id: int,
            developer_id: int
    ):
        # Connect a game with a developer.
        with self.connection.cursor() as cursor:

            cursor.execute(
                self.INSERT_GAME_DEVELOPER_SQL,     # Execute the SQL query to insert a relationship between a game and a developer into the bridge_game_developers table.
                (
                    game_id, 
                    developer_id,
                )
            )
        self.connection.commit()        # Commit the transaction to save the changes to the database.

    # Function to link the relation between dim_game & genre.
    def link_game_genre(
            self,
            game_id: int,
            genre_id: int
    ):

        with self.connection.cursor() as cursor:

            cursor.execute(
                self.INSERT_GAME_GENRE_SQL,     # Execute the SQL query to insert a relationship between a game and a genre into the bridge_game_genres table.
                (
                    game_id, 
                    genre_id,
                )
            )
        self.connection.commit()        # Commit the transaction to save the changes to the database.

    # Function to link the relation between dim_game & platform.
    def link_game_platform(
            self,
            game_id: int,
            platform_id: int
    ):

        with self.connection.cursor() as cursor:

            cursor.execute(
                self.INSERT_GAME_PLATFORM_SQL,     # Execute the SQL query to insert a relationship between a game and a platform into the bridge_game_platforms table.
                (
                    game_id, 
                    platform_id,
                )
            )
            self.connection.commit()        # Commit the transaction to save the changes to the database.