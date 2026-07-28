-- Game table
CREATE TABLE IF NOT EXISTS dim_games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,

    steam_app_id INT NOT NULL UNIQUE,

    game_name VARCHAR(255) NOT NULL,

    publisher_id INT NOT NULL,

    developer_id INT NOT NULL,

    genre_id INT NOT NULL,

    platform_id INT NOT NULL,

    release_date DATE,

    steam_url VARCHAR(500),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_game_publisher
        FOREIGN KEY (publisher_id)
        REFERENCES dim_publishers(publisher_id),

    CONSTRAINT fk_game_developer
        FOREIGN KEY (developer_id)
        REFERENCES dim_developers(developer_id),

    CONSTRAINT fk_game_genre
        FOREIGN KEY (genre_id)
        REFERENCES dim_genres(genre_id),

    CONSTRAINT fk_game_platform
        FOREIGN KEY (platform_id)
        REFERENCES dim_platforms(platform_id)
);

-- Fact table for measurments

CREATE TABLE IF NOT EXISTS fact_game_metrics (

    metric_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    game_id INT NOT NULL,

    snapshot_date DATE NOT NULL,

    price DECIMAL(10,2),

    discount_percent DECIMAL(5,2),

    final_price DECIMAL(10,2),

    positive_reviews INT,

    negative_reviews INT,

    total_reviews INT,

    review_score DECIMAL(5,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_metrics_game
        FOREIGN KEY (game_id)
        REFERENCES dim_games(game_id),

    CONSTRAINT uq_game_snapshot
    UNIQUE (game_id, snapshot_date);
);