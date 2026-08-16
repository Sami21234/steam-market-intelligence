# This file is responsible only for managing the dim_developers table, which will tell what to insert into dim_developers table.

from pymysql.connections import Connection

class DeveloperRepository:
    """
    Repository responsible for all operations on dim_developers.
    """

    GET_DEVELOPER_SQL = """
    SELECT developer_id 
    FROM dim_developers
    WHERE developer_name = %s;
    """

    INSERT_DEVELOPER_SQL = """
    INSERT INTO dim_developers
    (
        developer_name
    )
    VALUES
    (
        %s
    );
    """

    def __init__(self, connection: Connection):
        self.connection = connection

    def get_by_name(self, developer_name: str):
        """
        Retrieve a developer by name.
        """
        with self.connection.cursor() as cursor:

            cursor.execute(
                self.GET_DEVELOPER_SQL,
                (developer_name,)
            )
            return cursor.fetchone()

    def create(self, developer_name: str) -> int:
        """
        Insert a new developer and return its developer_id.
        """

        with self.connection.cursor() as cursor:
            cursor.execute(
                self.INSERT_DEVELOPER_SQL,
                (developer_name,)
            )
            self.connection.commit()
            return cursor.lastrowid

    def get_or_create(self, developer_name: str) -> int:
        """
        Return an existing developer_id or create one.
        """

        developer = self.get_by_name(developer_name)

        if developer:
            return developer["developer_id"]

        return self.create(developer_name)