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

    # Adding the validation method
    def has_game_details(self):
        """
        Check whether the downloaded page actually contains
        the expected Steam game-detail information or not.
        """
        return bool(
            self.soup.select_one("div.apphub_AppName")
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
    def get_developers(self):
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

        for publisher in self.soup.select(
            'a[href*="/publisher/"]'
        ):

            name = publisher.get_text(strip=True)

            if name:
                publishers.append(name)

        return list(dict.fromkeys(publishers))


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

    # Release Date
    def get_release_date(self):
        release_date = self.soup.select_one(
            "div.release_date div.date"
        )

        return (
            release_date.get_text(strip=True)
            if release_date
            else None
        )

    # Genres
    def get_genres(self):
        genres = []

        for genre in self.soup.select(
            "div.details_block a[href*='/genre/']"
        ):
            name = genre.get_text(strip=True)

            if name:
                genres.append(name)

        # Remove duplicates while preserving order
        return list(dict.fromkeys(genres))

    # Now, Parse All Details
    def parse_game_details(self):
        return {

            "game_name":
                self.get_game_name(),

            "developers":
                self.get_developers(),

            "publishers":
                self.get_publishers(),

            "genres":
                self.get_genres(),

            "review_count":
                self.get_review_count(),

            "rating_value":
                self.get_rating_value(),

            "review_summary":
                self.get_review_summary(),

            "release_date":
                self.get_release_date(),

        }
    