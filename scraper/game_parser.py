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
        Check whether the page contains Steam game details.

        We use multiple signals instead of depending on
        one specific CSS selector.
        """

        game_name = self.soup.select_one(
            "div.apphub_AppName"
        )

        developers = self.soup.select(
            "div.dev_row a"
        )

        genres = self.soup.select(
            "div.glance_tags a"
        )

        review_summary = self.soup.select_one(
            "span.nonresponsive_hidden"
        )

        return bool(
            game_name
            or developers
            or genres
            or review_summary
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

    # debugging method
    def debug_html(self):
        print("\n===== DEBUG HTML =====")

        print("Title:")
        print(self.soup.title.get_text(strip=True) if self.soup.title else None)

        print("\nApp Name:")
        app_name = self.soup.select_one("div.apphub_AppName")
        print(app_name.get_text(strip=True) if app_name else None)

        print("\nDeveloper links:")
        for element in self.soup.select("div.dev_row a"):
            print(element.get_text(strip=True))

        print("\nPublisher links:")
        for element in self.soup.select("div.dev_row a"):
            print(element.get_text(strip=True))

        print("\nGenre links:")
        for element in self.soup.select("div.glance_tags a"):
            print(element.get_text(strip=True))

    def debug_keywords(self):

        html = self.soup.prettify()

        keywords = [
            "Developer",
            "Developers",
            "Publisher",
            "Publishers",
            "Genre",
            "Genres",
            "Review",
            "Release Date",
        ]

        for keyword in keywords:

            print(f"\n===== {keyword} =====")

            index = html.lower().find(keyword.lower())

            if index == -1:
                print("NOT FOUND")
                continue

            start = max(0, index - 500)
            end = min(len(html), index + 1000)

            print(html[start:end])

    def is_age_gate(self):
        """
        Check whether Steam returned an age-gate page
        instead of the actual game details page.
        """

        return bool(
            self.soup.select_one(".agegate_text_container")
            or self.soup.select_one("#ageYear")
            or self.soup.find(
                string=lambda text:
                text and "Please enter your birth date" in text
            )
        )
    