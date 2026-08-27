# This file is responsible for Cleaning the data, which is important to do, before loading it to the database(MySQL).

from models.game import Game
from datetime import datetime

class SteamTransformer:
    """
    Transform raw scraped data into database-ready data.
    """

    @staticmethod
    def parse_release_date(value):
        """
        Convert Steam release date into a Python date object.

        Example:
            "21 Aug, 2012" -> date(2012, 8, 21)
    """
        if not value:
            return None

        try:
            return datetime.strptime(
                value.strip(),
                "%d %b, %Y"
            ).date()
        except ValueError:
            return None


    def transform(game: dict) -> dict:

        transformed = game.copy()       # Keeping the original record untouched and create a transformed version.

        # Steam App ID
        transformed["steam_app_id"] = (
            int(game["steam_app_id"])
            if game.get("steam_app_id") 
            else None
        )

        # price
        price = game.get("price")

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


        # Steam URL
        transformed["steam_url"] = game.get("steam_url")

        transformed["discount_percent"] = game.get("discount_percent")

        # Review Count
        transformed["review_count"] = game.get("review_count")

        # positive_percent
        transformed["positive_percent"] = game.get("positive_percent")

        # discount_percent
        transformed["discount_percent"] = game.get("discount_percent")

        # Developers
        transformed["developers"] = game.get("developers", [])

        # Publishers
        transformed["publishers"] = game.get("publishers", [])

        # Genres
        transformed["genres"] = game.get("genres", [])

        # Platform values
        transformed["windows"] = game.get("windows", False)

        transformed["mac"] = game.get("mac", False)

        transformed["linux"] = game.get("linux", False)

        # Return Game object

        return Game(        # Returning the transformed data as a Game object, which is a structured representation of the game data.
            steam_app_id = transformed["steam_app_id"],
            game_name = transformed["game_name"],
            release_date = SteamTransformer.parse_release_date(transformed["release_date"]),
            steam_url = transformed["steam_url"],

            price = transformed["price"],
            discount_percent = transformed["discount_percent"],
            review_summary = transformed["review_summary"],
            review_count = transformed["review_count"],
            positive_percent = transformed["positive_percent"],

            windows = transformed["windows"],
            mac = transformed["mac"],
            linux = transformed["linux"],

            publishers = transformed["publishers"],
            developers = transformed["developers"],
            genres = transformed["genres"]
        )