from scraper.steam_scraper import SteamScraper

def main():
    scraper = SteamScraper()
    scraper.scrape(max_pages=25)

if __name__ == "__main__":
    main()