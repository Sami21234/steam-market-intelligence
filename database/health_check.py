# Before Scraping first verifying the database connection

from database.connection import get_connection

# Now, creating the Check database function
def check_database():       
    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            result = cursor.fetchone()

        connection.close()

        print("Database connected successfully!")
        print(result)

    except Exception as error:
        print(f"Connection failed: {error}")

if __name__ == "__main__":
    check_database()