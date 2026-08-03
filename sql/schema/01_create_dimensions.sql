-- Games table
CREATE TABLE IF NOT EXISTS dim_games
(
    game_id INT AUTO_INCREMENT PRIMARY KEY,

    steam_app_id INT NOT NULL UNIQUE,

    game_name VARCHAR(255) NOT NULL,

    release_date DATE,

    steam_url VARCHAR(500),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Publisher table
CREATE TABLE IF NOT EXISTS dim_publishers 
(
    publisher_id INT AUTO_INCREMENT PRIMARY KEY,

    publisher_name VARCHAR(255) NOT NULL UNIQUE
);

-- Developer table
CREATE TABLE IF NOT EXISTS dim_developers 
(
    developer_id INT AUTO_INCREMENT PRIMARY KEY,

    developer_name VARCHAR(255) NOT NULL UNIQUE
);

-- Genre table
CREATE TABLE IF NOT EXISTS dim_genres 
(
    genre_id INT AUTO_INCREMENT PRIMARY KEY,

    genre_name VARCHAR(100) NOT NULL UNIQUE
);

-- Platform table   (instead of storing text repeatedly, use Boolean Columns)
CREATE TABLE IF NOT EXISTS dim_platforms 
(
    platform_id INT AUTO_INCREMENT PRIMARY KEY,

    windows BOOLEAN NOT NULL DEFAULT FALSE,

    mac BOOLEAN NOT NULL DEFAULT FALSE,

    linux BOOLEAN NOT NULL DEFAULT FALSE
);


