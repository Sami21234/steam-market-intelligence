-- Publisher table
CREATE TABLE IF NOT EXIST dim_publishers (
    publisher_id INT AUOT_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Developer table
CREATE TABLE IF NOT EXIST dim_developers (
    developer_id INT AUTO_INCREMENT PRIMARY KEY,
    developer_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Genre table
CREATE TABLE IF NOT EXISTS dim_genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Platform table   (instead of storing text repeatedly, use Boolean Columns)
CREATE TABLE IF NOT EXISTS dim_platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    windows BOOLEAN NOT NULL DEFAULT FALSE,
    mac BOOLEAN NOT NULL DEFAULT FALSE,
    linux BOOLEAN NOT NULL DEFAULT FALSE
);

