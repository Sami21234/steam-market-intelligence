from scraper.steam_scraper import SteamScraper

def main():
    scraper = SteamScraper()
    scraper.scrape_first_game()

if __name__ == "__main__":
    main()