# from scraper.client import SteamClient
# from scraper.game_parser import SteamGameParser


# GAME_URL = "https://store.steampowered.com/app/730/CounterStrike_2/"


# def main():

#     client = SteamClient()

#     response = client.get(GAME_URL)

#     parser = SteamGameParser(response.text)

#     game_details = parser.parse_game_details()

#     print("\n===== GAME DETAILS =====")

#     print("Game:", game_details["game_name"])
#     print("Developers:", game_details["developers"])
#     print("Publishers:", game_details["publishers"])
#     print("Genres:", game_details["genres"])
#     print("Review Count:", game_details["review_count"])
#     print("Rating:", game_details["rating_value"])
#     print("Review Summary:", game_details["review_summary"])
#     print("Release Date:", game_details["release_date"])


# if __name__ == "__main__":
#     main()

from scraper.client import SteamClient
from scraper.game_parser import SteamGameParser


def main():

    url = "https://store.steampowered.com/app/553850/HELLDIVERS_2/"

    client = SteamClient()

    response = client.get(url)

    print("Status:", response.status_code)
    print("HTML length:", len(response.text))

    parser = SteamGameParser(response.text)

    parser.debug_html()
    parser.debug_keywords()


if __name__ == "__main__":
    main()