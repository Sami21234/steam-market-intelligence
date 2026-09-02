SELECT COUNT(*) AS total_games
FROM dim_games;

SELECT COUNT(*) AS total_metrics
FROM fact_game_metrics;

SELECT COUNT(*) AS total_developers
FROM dim_developers;

SELECT COUNT(*) AS total_publishers
FROM dim_publishers;

SELECT COUNT(*) AS total_genres
FROM dim_genres;

SELECT COUNT(*) AS total_platforms
FROM dim_platforms;

SELECT
    COUNT(*) AS total_snapshots,
    COUNT(DISTINCT snapshot_date) AS snapshot_days,
    MIN(snapshot_date) AS first_snapshot,
    MAX(snapshot_date) AS latest_snapshot
FROM fact_game_metrics;