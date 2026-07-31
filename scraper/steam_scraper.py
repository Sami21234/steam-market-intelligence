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

        first_game = games[0]       # Takes first game
        print(first_game.prettify())    # Prints HTML