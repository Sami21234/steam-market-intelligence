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

    
