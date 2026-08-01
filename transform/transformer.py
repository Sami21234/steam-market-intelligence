# This file is responsible for Cleaning the data, which is important to do, before loading it to the database(MySQL).

from models.game import Game
from datetime import datetime

class SteamTransformer:
    """
    Transform raw scraped data into database-ready data.
    """

    @staticmethod
    def transform(game: dict) -> dict:

        transformed = game.copy()       # Keeping the original record untouched and create a transformed version.

        # Steam App ID
        transformed["steam_app_id"] = (
            int(game["steam_app_id"])
            if game.get("steam_app_id") 
            else None
        )

        # price
        price = game["price"]

        if not price:
            transformed["price"] = None


        elif price.lower() == "free":
            transformed["price"] = 0.0

        else:
            price = (
                price.replace("₹", "")
                     .replace(",", "")
                     .strip()
            )

            transformed["price"] = float(price)

        # Release Date
        release_date = game.get("release_date")

        if release_date:
            try:
                transformed["release_date"] = datetime.strptime(
                    release_date,
                    "%d %b, %Y"
                ).date()
            except ValueError:
                transformed["release_date"] = None
        else:
            transformed["release_date"] = None

        return Game(        # Returning the transformed data as a Game object, which is a structured representation of the game data.
            steam_app_id = transformed["steam_app_id"],
            game_name = transformed["game_name"],
            release_date = transformed["release_date"],
            price = transformed["price"],
            review_summary = transformed["review_summary"],
            windows = transformed["windows"],
            mac = transformed["mac"],
            linux = transformed["linux"],
        )