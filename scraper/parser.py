# This file is responsible for converting the HTML into Python data(Parsing)

from bs4 import BeautifulSoup

class SteamParser:
    """
    Responsible for parsing Steam HTML.
    """

    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "lxml")

    def get_game_cards(self):
        """
        Return all game containers.
        """
        return self.soup.select("a.search_result_row")      # Searching through CSS selector(more effiecient manner).

    
    def parse_game(self, game):
        """
        Extract one game's information.
        """
        steam_app_id = game.get("data-ds-appid")    # Gives the AppID.

        title = game.select_one("span.title")       # Gives the title of the Game.

        release_date = game.select_one("div.search_released")   # Gives the released date of the game.

        price = ( game.select_one("div.discount_final_price")     # Gives the price of the game.
                  or game.select_one("div.discount_original_price")
        )
        review = game.select_one("span.search_review_summary")  # Gives the reviews of the game.

        platforms = game.select(".search_platforms span")       # Gives the platform such as (Linux, Windows, Mac).

        return {
            "steam_app_id": steam_app_id,

            "game_name":
                title.get_text(strip=True)
                if title else None,     # If the title is not given, then use None.

            "release_date":
                release_date.get_text(strip=True)
                if release_date else None,

            "price":
                price.get_text(strip=True)
                if price else None,

            "review_summary":
                review.get(
                    "data-tooltip-html",
                    ""
                ).split("<br>")[0]
                if review else None,

            "windows":
                any("win" in p["class"]
                    for p in platforms),

            "mac":
                any("mac" in p["class"]
                    for p in platforms),

            "linux":
                any("linux" in p["class"]
                    for p in platforms),
        }