# This file is resposible only for the dim_games table in the database. It contains the GameRepository class, which provides methods for interacting with the dim_games table, such as inserting and retrieving game data.

from pymysql.connections import Connection     # Importing the connect function from the pymysql library, which is used to establish a connection to a MySQL database.
from models.game import Game    # Importing the Game class from the models.game module, which defines the structure of a game object.

class GameRepository:       
    """
    Repository responsible for all database operations related to the dim_games table.    
    """

    INSERT_GAME_SQL = """
    INSERT INTO dim_games 
    (
        steam_app_id, 
        game_name, 
        release_date, 
        steam_url
    )
    VALUES
    (
        %s, 
        %s, 
        %s,
        %s
    )
    ON DUPLICATE KEY UPDATE
        game_name = VALUES(game_name),
        release_date = VALUES(release_date),
        steam_url = VALUES(steam_url);
    """

    GET_GAME_BY_APP_ID_SQL = """
    SELECT game_id
    FROM dim_games
    WHERE steam_app_id = %s;
    """

    def __init__(self, connection: Connection):
        """
        Initializes the GameRepository with a database connection.
        """
        self.connection = connection

    def save(self, game: Game) -> None:     
        """
        Saves a Game object to the dim_games table. If the game already exists (based on steam_app_id), it updates the existing record.
        Returns the game_id of the inserted or updated game.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.INSERT_GAME_SQL, 
                (
                    game.steam_app_id, 
                    game.game_name, 
                    game.release_date,
                    game.steam_url,
                ),
            )
        self.connection.commit()

    def get_by_steam_app_id(self, steam_app_id: int):       
        """
        Retrieves a game_id from the dim_games table based on the provided steam_app_id.
        Returns the game_id if found, otherwise returns None.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.GET_GAME_BY_APP_ID_SQL, 
                (steam_app_id,),
            )
            result =  cursor.fetchone()      # fetchone() retrieves the first row of the result set from the executed query. If no rows are found, it returns None.
            return result

    def save_and_get_id(self, game: Game) -> int:     
        """
        Saves a Game object to the dim_games table and retrieves its game_id.
        If the game already exists (based on steam_app_id), it updates the existing record.
        Returns the game_id of the inserted or updated game.
        """
        self.save(game)
        result =  self.get_by_steam_app_id(game.steam_app_id)

        if not result:
            raise RuntimeError(
                f"Game not found after save: {game.steam_app_id}"
            )

        return result["game_id"]

