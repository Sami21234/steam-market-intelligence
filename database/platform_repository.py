# This file is responsible for connecting and managing the dim_platforms table in the database. It contains the PlatformRepository class, which provides methods for interacting with the dim_platforms table, such as inserting and retrieving platform data.
from pymysql.connections import Connection      # Importing the Connection class from the pymysql library, which is used to establish a connection to a MySQL database.

class PlatformRepository:       # it is a class that is responsible for managing the dim_platforms table in the database. It provides methods to retrieve and insert platform data.
    """
    Repository responsible for all operations on dim_platforms.
    """

    GET_PLATFORM_SQL = """
    SELECT platform_id
    FROM dim_platforms
    WHERE platform_name = %s;
    """

    INSERT_PLATFORM_SQL = """
    INSERT INTO dim_platforms
    (
        platform_name
    )
    VALUES
    (
        %s
    );
    """

    def __init__(self, connection: Connection):     # The constructor method initializes the PlatformRepository class with a database connection. It takes a Connection object as an argument, which is used to interact with the MySQL database.
        self.connection = connection        # Storing the database connection for use in other methods.

    def get_by_name(self, platform_name: str):
        """
        Retrieve a platform by its name.
        """

        with self.connection.cursor() as cursor:        # Establish a cursor to execute SQL queries on the database connection.
            cursor.execute(
                self.GET_PLATFORM_SQL,     # Execute the SQL query to retrieve the platform_id based on the provided platform_name.
                (platform_name,)
            )
            return cursor.fetchone()        # fetchone() retrieves a single row from the result.

    def create(self, platform_name: str) -> int:
        """
        Create a new platform and return its ID.
        """

        with self.connection.cursor() as cursor:
            cursor.execute(
                self.INSERT_PLATFORM_SQL,     # Execute the SQL query to insert a new platform into the dim_platforms table.
                (platform_name,)
            )
            self.connection.commit()      # Commit the transaction to save the changes to the database.

            return cursor.lastrowid        # lastrowid returns the integer value of the last inserted row's ID, which is the platform_id of the newly created platform.

    def get_or_create(self, platform_name: str):
        """
        Return an existing platform_id or create one.
        """
        platform = self.get_by_name(platform_name)      # Check if the platform already exists in the database by calling the get_by_name method.

        if platform:        # If the platform exists, return its platform_id.
            return platform["platform_id"]

        return self.create(platform_name)       # If the platform does not exist, create a new one and return its platform_id.