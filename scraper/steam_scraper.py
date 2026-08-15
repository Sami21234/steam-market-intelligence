# This file is responsible for connecting the complete scraping pipeline.

from scraper.client import SteamClient      # Responsible for downloading the HTML structure of the Steam search page.
from scraper.constants import STEAM_SEARCH_URL      # Constant that holds the URL of the Steam search page to be scraped.
from scraper.game_parser import SteamGameParser
from scraper.parser import SteamParser      # Responsible for parsing the HTML structure and extracting relevant game information.
from transform.transformer import SteamTransformer      # Responsible for transforming the parsed game data into a format suitable for database insertion.
from database.connection import get_connection        # Function that establishes a connection to the database.
from database.game_repository import GameRepository      # Responsible for interacting with the dim_games table in the database.
from database.publisher_repository import PublisherRepository       # Responsible for interacting with the dim_publishers table in the database.
from database.developer_repository import DeveloperRepository       # Responsible for interacting with the dim_developers table in the database.
from database.genre_repository import GenreRepository       # Responsible for interacting with the dim_genres table in the database.
from database.platform_repository import PlatformRepository     # Responsible for interacting with the dim_platforms table in the database.
from database.bridge_repository import BridgeRepository     # Responsible for inserting relationships between dimension tables in the database.
from database.metrics_repository import MetricsRepository       # Responsible for inserting records into the fact_game_metrics table in the database.

class SteamScraper:

    def __init__(self):
        self.client = SteamClient()     # Downloads the Html Structure(DOM) and parse to BeautifulSoup

    def scrape_first_game(self):
        # Step 1 - download HTML
        response = self.client.get(STEAM_SEARCH_URL)    # Find all game cards 

        # Step 2 - parse HTML
        parser = SteamParser(response.text)

        games = parser.get_game_cards()

        print(f"Found {len(games)} games on page")

        # Step 3 -  Database Connection
        connection = get_connection()       

        game_repository = GameRepository(connection)

        publisher_repository = PublisherRepository(connection)

        developer_repository = DeveloperRepository(connection)

        genre_repository = GenreRepository(connection)

        platform_repository = PlatformRepository(connection)

        bridge_repository = BridgeRepository(connection)

        metrics_repository = MetricsRepository(connection)

        saved = 0  
        age_gated = 0
        invalid_details = 0     

        try:   
            # Step 5 - Process Every Game. 

            for game in games:
                    # Parse Search Result
                    parsed_game = parser.parse_game(game)

                    # print(parsed_game)

                    # validation for missing values.
                    if not parsed_game["steam_app_id"]:
                        continue

                    # Get Game URL
                    steam_url = parsed_game["steam_url"]
                    if not steam_url:
                        continue

                    # Step 6 - Download Game Detail Page
                    detail_response = self.client.get(
                        steam_url
                    )

                    # Check HTTP response

                    if detail_response.status_code != 200:

                        print(
                            f"⚠️ Failed to download: "
                            f"{parsed_game['game_name']} "
                            f"(HTTP {detail_response.status_code})"
                        )

                        continue

                    # Step 7 - Parse Game Detail Page
                    detail_parser = SteamGameParser(
                        detail_response.text
                    )

                    # Step 8 - check age-gated
                    if detail_parser.is_age_gate():

                        print(
                            f"⚠️ Age-gated page: "
                            f"{parsed_game['game_name']}"
                        )

                        age_gated += 1

                        continue

                    # Step 9 - Parse details
                    details = detail_parser.parse_game_details()

                    # Step 10 - Validate details
                    if not details["developers"] and not details["publishers"] and not details["game_name"]:

                        print(
                            f"⚠️ No game/developer/publisher found: "
                            f"{parsed_game['game_name']}"
                        )

                        invalid_details += 1

                        print(
                            f"Details returned: {details}"
                        )

                        continue


                    # Step 11 - Merge Search + Deatail Data
                    parsed_game.update(details
                        # {
                        #     "developers": details["developers"],

                        #     "publishers": details["publishers"],

                        #     "genres": details["genres"],

                        #     "review_count": details["review_count"],

                        #     "rating_value": details["rating_value"],

                        # }
                    )

                    # Step 12 - Transform
                    transformed_game = (
                        SteamTransformer.transform(
                            parsed_game
                        )
                    )

                    # Step 13 - Print Result
                    print(
                    f"\nProcessing: "
                    f"{transformed_game.game_name}"
                )

                    print(
                        f"Developers: "
                        f"{transformed_game.developers}"
                    )

                    print(
                        f"Publishers: "
                        f"{transformed_game.publishers}"
                    )

                    print(
                        f"Genres: "
                        f"{transformed_game.genres}"
                    )

                    print(
                        f"Review Count: "
                        f"{transformed_game.review_count}"
                    )

                    # Database Loading
                    # Not adding the repository operations yet.
                    # First verifying that the complete data is correctly Collected.

                    saved += 1

            # Commit
            connection.commit()

        except Exception:
            connection.rollback()      # Rollback the transaction in case of an error

            raise  # Re-raise the exception to propagate the error

        finally:

            connection.close()      # Close the database connection

        print(f"Successfully saved/processed {saved} games")
        
        print(f"Successfully processed: {saved}")
        print(f"Age-gated pages: {age_gated}")
        print(f"Invalid detail pages: {invalid_details}")

# scrape_first_game() should now follow this order:

"""

            Create HTTP Client
                    │
              Download HTML
                    │
              Create Parser
                    │
             Find Game Cards
                    │
            Create MySQL Connection
                    │
            Create Repository
                    │
            Loop Through Games
                    │
                  Parse
                    │
                Validate
                    │
                Transform
                    │
               Save to Database
                    │
               Close Connection

"""
