# This file is responsible for defining the Game data model.(data model means how the data is structured and represented in the code.)

from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass      # This decorator is used to automatically generate special methods like __init__(), __repr__(), and __eq__() for the class based on its attributes. It simplifies the creation of classes that primarily store data.
class Game:
    """
    Represents the complete data collected for one Steam game.
    """
    # Basic game information
    steam_app_id: int       # The unique identifier for the game on Steam.
    game_name: str          # The name of the game.
    release_date: Optional[date]  # The date the game was released.

    # Steam information
    steam_url: Optional[str]           # The URL of the game's page on Steam.

    # Market information
    price: Optional[float]  # The price of the game.

    # Review information
    review_summary: Optional[str]   # A summary of the game's reviews.
    review_count: Optional[int]     # Reviews of the Games.
    rating_value: Optional[float]   

    # platform information
    windows: bool
    mac: bool
    linux: bool

    # Relationships
    publishers: list[str]    # Publisher of the game.
    developers: list[str]    # Developer of the game.
    genres: list[str]       # List of genres.

    
    # positive_percent: Optional[float]   # percentage of the positive reviews.
    # platforms: list[str]           # List of platforms the game is available on.

