import pandas as pd
from database.connection import get_connection

OUTPUT_FILE = "steam_market_intelligence.csv"

def export_dataset():
    # Establish a connection to the database
    connection = get_connection()

    # Query to fetch data from the database
    query = """
        SELECT
            game_id,
            steam_app_id,
            game_name,
            release_date,
            developers,
            publishers,
            genres,
            platforms,
            price,
            discount_percent,
            review_count,
            positive_percent,
            snapshot_date
        FROM vw_steam_final_dataset
        ORDER BY game_id;
    """

    columns = [
        "game_id",
        "steam_app_id",
        "game_name",
        "release_date",
        "developers",
        "publishers",
        "genres",
        "platforms",
        "price",
        "discount_percent",
        "review_count",
        "positive_percent",
        "snapshot_date",
    ]

    try:
        with connection.cursor() as cursor:
            # Execute the query
            cursor.execute(query)

            # Fetch all rows from the executed query
            rows = cursor.fetchall()

            # Create a DataFrame from the fetched data
            df = pd.DataFrame(rows, columns=columns)

            # Export the DataFrame to a CSV file
            df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

            print("CSV exported successfully!")
            print(f"File: {OUTPUT_FILE}")
            print(f"Rows: {len(df)}")
            print(f"Columns: {len(df.columns)}")

    finally:
        # Close the database connection
        connection.close()

if __name__ == "__main__":      # dunder name check to ensure the script is being run directly
    export_dataset()