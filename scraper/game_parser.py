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

    # Publisher
    def get_publishers(self):

        
        publishers = []

        for row in self.soup.select("div.dev_row a"):

            label = row.select_one(
                "div.subtitle"
            )

            if not label:
                continue

            if label.get_text(strip=True).startswith("Publisher"):
                for publisher in row.select("a"):
                    name = publisher.get_text(strip=True)

                    if name:
                        publishers.append(name)

        return publishers


    # Review Count
    def get_review_count(self):

        review_count = self.soup.select_one(
            'meta[itemprop="reviewCount"]'
        )

        if not review_count:
            return None

        content = review_count.get("content")

        if not content:
            return None

        try:
            return int(content)

        except ValueError:
            return None

    # Rating Value
    def get_rating_value(self):
        rating = self.soup.select_one(
            'meta[itemprop="ratingValue"]'
        )

        if not rating:
            return None

        content = rating.get("content")

        if not content:
            return None

        try:
            return float(content)

        except ValueError:
            return None

    # Review Summary
    def get_review_summary(self):
        review = self.soup.select_one(
            "span.game_review_summary"
        )

        return (
            review.get_text(strip=True)
            if review
            else None
        )