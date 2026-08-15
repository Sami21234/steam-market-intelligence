# This file is responsible only for downloading pages.

import requests
import time
from scraper.constants import DEFAULT_HEADERS

class SteamClient:
    """
    Handles HTTP communication with Steam.
    """
    def __init__(self):

        # Creates one reusable HTTP session.
        # This improves performance because connections can be reused.
        self.session = requests.Session()       # Creates one reusable HTTP session, this improves the performance.
        self.session.headers.update(DEFAULT_HEADERS)    # This gets the User-Agent and Accept-Language contents.

    def get(self, url: str, retries: int = 3, delay: int = 3):
        """
        Download a webpage with retry handling.

        retries:
            Number of additional attempts if the request temporarily fails.

        delay:
            Number of seconds to wait between attempts.

        """
        for attempt in range(1, retries + 1):
            try:

                response = self.session.get(
                    url,
                    timeout = 30
                )


                response.raise_for_status()
                return response
            
            except requests.exceptions.RequestException as e:

                print(
                    f"⚠️ Request failed "
                    f"(attempt {attempt}/{retries}): {e}"
                )

                # If this wasn't the final attempt, wait before trying again.
                if attempt < retries:
                    print(
                        f"Retrying in {delay} seconds..."
                    )
                    time.sleep(delay)

                else:
                    # All attempts failed.
                    print(
                        "❌ All request attempts failed."
                    )

                    raise