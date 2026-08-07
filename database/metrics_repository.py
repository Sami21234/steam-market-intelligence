# This file is responsible for managing the data which changes over time(fact table data), this repository pouplates the fact table.

from pymysql.connections import Connection
from models.game import Game
from datetime import date

class MetricsRepository:
    """
    Repository responsible for inserting records into fact_game_metrics.
    """

    INSERT_METRICS_SQL = """
    INSERT INTO fact_game_metrics
    (
        game_id,
        price,
        review_summary,
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
        review_summary = VALUES(review_summary),
        review_count = VALUES(review_count),
        positive_percent = VALUES(positive_percent);
    """

    def __init__(self, connection: Connection):
        self.connection = connection

    def save(
        self,
        game_id: int,
        game: Game
    ):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.INSERT_METRICS_SQL,
                (
                    game_id,
                    game.price,
                    game.review_summary,
                    game.review_count,
                    game.positive_percent,
                    date.today()
                )
            )
        self.connection.commit()