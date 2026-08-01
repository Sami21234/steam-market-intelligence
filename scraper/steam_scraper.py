# This file is responsible for connecting everything.

from database import connection
from scraper.client import SteamClient      # Responsible for downloading the HTML structure of the Steam search page.
from scraper.constants import STEAM_SEARCH_URL      # Constant that holds the URL of the Steam search page to be scraped.
from scraper.parser import SteamParser      # Responsible for parsing the HTML structure and extracting relevant game information.
from transform.transformer import SteamTransformer      # Responsible for transforming the parsed game data into a format suitable for database insertion.
from database.connection import get_connection        # Function that establishes a connection to the database.
from database.repository import GameRepository      # Class that handles database operations related to the Game model.

class SteamScraper:

    def __init__(self):
        self.client = SteamClient()     # Downloads the Html Structure(DOM) and parse to BeautifulSoup

    def scrape_first_game(self):

        response = self.client.get(STEAM_SEARCH_URL)    # Find all game cards 

        parser = SteamParser(response.text)

        games = parser.get_game_cards()

        connection = get_connection()       

        repository = GameRepository(connection)

        print(f"Found {len(games)} games on page")

        saved = 0       

        try:    

            for game in games:

                    parsed_game = parser.parse_game(game)

                    # print(parsed_game)

                    # validation for missing values.
                    if parsed_game["steam_app_id"] is None:
                        continue

                    transformed_game = SteamTransformer.transform(parsed_game)

                    repository.save_game(transformed_game)
                    saved += 1

        finally:

            connection.close()      # Close the database connection

        print(f"Successfully saved {saved} games")

