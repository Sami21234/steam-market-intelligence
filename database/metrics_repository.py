# This file is responsible for managing the data which changes over time(fact table data), this repository pouplates the fact table.

from pymysql.connections import Connection

class MetricsRepository:
    """
    Repository responsible for inserting records into fact_game_metrics.
    """

    INSERT_METRICS_SQL = """
    INSERT INTO fact_game_metrics
    (
        game_id,
        price,
        discount_percent,
        review_count,
        positive_percent,
        snapshot_date
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
    ON DUPLICATE KEY UPDATE
        price = VALUES(price),
        discount_percent = VALUES(discount_percent),
        review_count = VALUES(review_count),
        positive_percent = VALUES(positive_percent);
    """

    def __init__(self, connection: Connection):
        self.connection = connection

    def save(
        self,
        game_id: int,
        snapshot_date,
        review_count,
        positive_percent,
        price,
        discount_percent=None
    ):
        
        """
        Insert a game metric snapshot.
        """

        with self.connection.cursor() as cursor:
            cursor.execute(
                self.INSERT_METRICS_SQL,
                (
                    game_id,
                    price,
                    discount_percent,
                    review_count,
                    positive_percent,
                    snapshot_date,
                )
            )
            lastrowid = cursor.lastrowid
        self.connection.commit()
        return lastrowid