-- Fact table for measurments

CREATE TABLE IF NOT EXISTS fact_game_metrics (

    metric_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    game_id INT NOT NULL,

    price DECIMAL(10, 2),

    discount_percent DECIMAL(5, 2),

    review_count INT,

    positive_percent DECIMAL(5, 2),

    snapshot_date DATE NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_fact_game
        FOREIGN KEY (game_id)
        REFERENCES dim_games(game_id)
        ON DELETE CASCADE,

    CONSTRAINT uq_game_snapshot
        UNIQUE (game_id, snapshot_date)

);