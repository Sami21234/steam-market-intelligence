# This file is responsible only for downloading pages.

import requests

from scraper.constants import DEFAULT_HEADERS

class SteamClient:
    """
    Handles HTTP communication with Steam.
    """
    def __init__(self):
        self.session = requests.Session()       # Creates one reusable HTTP session, this improves the performance.
        self.session.headers.update(DEFAULT_HEADERS)    # This gets the User-Agent and Accept-Language contents.

    def get(self, url: str):
        """
        Download a webpage.
        """

        response = self.session.get(
            url,
            timeout = 30
        )

        response.raise_for_status()
        return response