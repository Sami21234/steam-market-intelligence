# This file is responsible to manage the dim_publishers table, what it will store in the dim_publishers table. 

from pymysql.connections import Connection      # Importing the Connection class from the pymysql library, which is used to establish a connection to a MySQL database.

class PublisherRepository:
    """
    Repository responsible for all operations on dim_publishers.
    """

    GET_PUBLISHER_SQL = """
    SELECT publisher_id
    FROM dim_publishers
    WHERE publisher_name = %s;
    """

    INSERT_PUBLISHER_SQL = """
    INSERT INTO dim_publishers
    (
        publisher_name
    )
    VALUES
    (
        %s
    );
    """
    def __init__(self, connection: Connection):     # The constructor method initializes the GameRepository class with a database connection. It takes a Connection object as an argument, which is used to interact with the MySQL database.
            self.connection = connection        # Storing the database connection for use in other methods.

    # finding the Existing Publisher
    def get_by_name(self, publisher_name: str):
        """
        Retrieve a publisher by its name.
        """

        with self.connection.cursor() as cursor:
             cursor.execute(
                 self.GET_PUBLISHER_SQL,
                 (publisher_name,)
              )
             
             return cursor.fetchone()

    # Now, Inserting the Publishers if it is not already present.
    def create(self, pubisher_name: str) -> int:
        """
        Create a new publisher and return its ID.
        """

        with self.connection.cursor() as cursor:
             
            cursor.execute(
                self.INSERT_PUBLISHER_SQL, 
                (pubisher_name,)
            )

            self.connection.commit()
            return cursor.lastrowid        # lastrowid returns the integer.

    # Now, Combining both methods.
    def get_or_create(self, publisher_name: str) -> int:
        """
        Return an existing publisher_id or create one.
        """
        publisher = self.get_by_name(publisher_name)

        if publisher:
            return publisher["publisher_id"]

        return self.create(publisher_name)

    # Complete Workflow:
    """
          Valve
            │
          Search
            │
          Exists?
            │
           Yes
            │
    Return publisher_id = 1

    """
