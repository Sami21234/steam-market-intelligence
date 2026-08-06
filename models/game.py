# This file is responsible for defining the Game data model.(data model means how the data is structured and represented in the code.)

from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass      # This decorator is used to automatically generate special methods like __init__(), __repr__(), and __eq__() for the class based on its attributes. It simplifies the creation of classes that primarily store data.
class Game:
    """
    Represents one Steam game.
    """
    steam_app_id: int       # The unique identifier for the game on Steam.
    game_name: str          # The name of the game.
    release_date: Optional[date]  # The date the game was released.
    publisher: list[str]    # Publisher of the game.
    developer: list[str]    # Developer of the game.
    genres: list[str]       # List of genres.
    price: Optional[float]  # The price of the game.
    review_summary: Optional[str]   # A summary of the game's reviews.
    review_count: Optional[int]     # Reviews of the Games.
    positive_percent: Optional[float]   # percentage of the positive reviews.
    windows: bool           # Indicates if the game is available on Windows.
    mac: bool               # Indicates if the game is available on Mac.
    linux: bool               # Indicates if the game is available on Linux.

