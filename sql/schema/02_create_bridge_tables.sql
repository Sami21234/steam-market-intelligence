-- bridge_game_publishers
CREATE TABLE IF NOT EXISTS bridge_game_publishers
(
    game_id INT NOT NULL,

    publisher_id INT NOT NULL,

    PRIMARY KEY (game_id, publisher_id),

    CONSTRAINT fk_bridge_game
        FOREIGN KEY (game_id)
        REFERENCES dim_games(game_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bridge_publisher
        FOREIGN KEY (publisher_id)
        REFERENCES dim_publishers(publisher_id)
        ON DELETE CASCADE
);

-- bridge_game_developers
CREATE TABLE IF NOT EXISTS bridge_game_developers
(
    game_id INT NOT NULL,

    developer_id INT NOT NULL,

    PRIMARY KEY (game_id, developer_id),

    CONSTRAINT fk_bridge_game_developer
        FOREIGN KEY (game_id)
        REFERENCES dim_games(game_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bridge_developer
        FOREIGN KEY (developer_id)
        REFERENCES dim_developers(developer_id)
        ON DELETE CASCADE
);

-- bridge_game_genres
CREATE TABLE IF NOT EXISTS bridge_game_genres
(
    game_id INT NOT NULL,

    genre_id INT NOT NULL,

    PRIMARY KEY (game_id, genre_id),

    CONSTRAINT fk_bridge_game_genre
        FOREIGN KEY (game_id)
        REFERENCES dim_games(game_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bridge_genre
        FOREIGN KEY (genre_id)
        REFERENCES dim_genres(genre_id)
        ON DELETE CASCADE
);

-- bridge_game_platforms
CREATE TABLE IF NOT EXISTS bridge_game_genres
(
    game_id INT NOT NULL,

    genre_id INT NOT NULL,

    PRIMARY KEY (game_id, genre_id),

    CONSTRAINT fk_bridge_game_genre
        FOREIGN KEY (game_id)
        REFERENCES dim_games(game_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bridge_genre
        FOREIGN KEY (genre_id)
        REFERENCES dim_genres(genre_id)
        ON DELETE CASCADE
);