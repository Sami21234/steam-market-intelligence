# This file is responsible for parsing an individual Steam game detail page.

from bs4 import BeautifulSoup       

class SteamGameParser:
    """
    Responsible for parsing an individual Steam game page
    and extracting detailed game information.
    """
    def __init__(self, html: str):

        self.soup = BeautifulSoup(
            html,
            "lxml"
        )

    # Game Title
    def get_game_name(self):

        title = self.soup.select_one(
            "div.apphub_AppName"
        )

        return (
            title.get_text(strip=True)
            if title 
            else None
        )

    # Developer
    def get_developer(self):
        developers = []

        for row in self.soup.select("div.dev_row"):
            label = row.select_one(
                "div.subtitle"
            )

            if not label:
                continue

            if label.get_text(strip=True).startswith("Developer"):
                for developer in row.select("a"):
                    name = developer.get_text(strip=True)

                    if name:
                        developers.append(name)

        return developers


