from datetime import date       
from database.connection import get_connection
from database.game_repository import GameRepository
from database.developer_repository import DeveloperRepository
from database.publisher_repository import PublisherRepository
from database.genre_repository import GenreRepository
from database.platform_repository import PlatformRepository
from database.metrics_repository import MetricsRepository
from database.bridge_repository import BridgeRepository
from models.game import Game

def main():
    connection = get_connection()

    try:
        print("Database connected successfully!\n")

        # Initializing repositories
        game_repo = GameRepository(connection)
        developer_repo = DeveloperRepository(connection)
        publisher_repo = PublisherRepository(connection)
        genre_repo = GenreRepository(connection)
        platform_repo = PlatformRepository(connection)
        metrics_repo = MetricsRepository(connection)
        bridge_repo = BridgeRepository(connection)

        print("Repositories initialized successfully.\n")

        # Test Game
        test_game = Game(
            steam_app_id=999999999,
            game_name="Repository Test Game",
            release_date=date(2026, 8, 16),
            steam_url="https://store.steampowered.com/app/999999999/",

            price=19.99,
            discount_percent=10.00,

            review_summary="Very Positive",
            review_count=1000,
            positive_percent=95.00,

            windows=True,
            mac=True,
            linux=False,
            
            publishers=["Test Publisher"],
            developers=["Test Developer"],
            genres=["Test Genre"],
        )

        print("Testing GameRepository...")

        game_id = game_repo.save_and_get_id(test_game)

        print(f"Game created successfully. game_id = {game_id}\n")

        # Test DeveloperRepository
        print("Testing DeveloperRepository...")
        developer_id = developer_repo.get_or_create(
            "Test Developer"
        )

        # Test PublisherRepository
        print("Testing PublisherRepository...")

        publisher_id = publisher_repo.get_or_create(
            "Test Publisher"
        )

        print(
            f"Publisher created/found successfully. "
            f"publisher_id = {publisher_id}\n"
        )

        # Test GenreRepository
        print("Testing GenreRepository...")

        genre_id = genre_repo.get_or_create(
            "Test Genre"
        )

        print(
            f"Genre created/found successfully. "
            f"genre_id = {genre_id}\n"
        )

        # Test PlatformRepository
        print("Testing PlatformRepository...")

        platform_id = platform_repo.get_or_create(
            "Windows"
        )

        print(
            f"Platform created/found successfully. "
            f"platform_id = {platform_id}\n"
        )

        # Test BridgeRepository
        print("Testing BridgeRepository...")

        bridge_repo.link_game_developer(
            game_id,
            developer_id
        )

        bridge_repo.link_game_publisher(
            game_id,
            publisher_id
        )

        bridge_repo.link_game_genre(
            game_id,
            genre_id
        )

        bridge_repo.link_game_platform(
            game_id,
            platform_id
        )

        print("All game relationships created successfully.\n")

        # Test MetricsRepository
        print("Testing MetricsRepository...")

        metrics_repository_id = metrics_repo.save(
            game_id=game_id,
            snapshot_date=date(2026, 8, 16),
            review_count=1000,
            positive_percent=95.5,
            price=19.99,
            discount_percent=20.0,
        )

        print(
            f"Metrics saved successfully. "
            f"lastrowid = {metrics_repository_id}\n"
        )

        # Final results
        print("=" * 50)
        print("ALL REPOSITORY TESTS PASSED")
        print("=" * 50)

    except Exception as e:

        connection.rollback()

        print("\n❌ REPOSITORY TEST FAILED")
        print(f"Error: {e}")

        raise

    finally:

        connection.close()

        print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()