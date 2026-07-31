# This file is responsible for connecting everything.

from scraper.client import SteamClient
from scraper.constants import STEAM_SEARCH_URL
from scraper.parser import SteamParser

class SteamScraper:

    def __init__(self):
        self.client = SteamClient()     # Downloads the Html Structure(DOM) and parse to BeautifulSoup

    def scrape_first_game(self):
        response = self.client.get(STEAM_SEARCH_URL)    # Find all game cards 

        parser = SteamParser(response.text)

        games = parser.get_game_cards()

        print(f"Found {len(games)} games on page")

        parsed_games = []    # List of games

        for game in games:
            parsed_game = parser.parse_game(game)

            # validation for missing values.
            if parsed_game["steam_app_id"] is None:
                continue

            parsed_games.append(parsed_game)

        print(f"Successfully parsed {len(parsed_games)} games")
        # print(parsed_games[0])

        for game in parsed_games[:10]:
            print(game)