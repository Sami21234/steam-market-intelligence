import pymysql  
from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

# Now, creating the MYSQL database connection function.
def get_connection():
    """
    Create and return a MySQL database connection.
    """
    connection = pymysql.connect(
        host = DB_HOST,
        port = DB_PORT,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME,
        charset = "utf8mb4",    # Steam game names may contain: Japanese, Chinese, Korean, Emojis, etc.. (utf8mb4 supports full Unicode.)
        cursorclass = pymysql.cursors.DictCursor,
        autocommit = False,  # This keeps the database consistent.
    )

    return connection