-- Now, creating the indexes for efficiently scanning the entire table, which reduces the execution time on a large datasets.

-- for games creating the index
CREATE INDEX idx_games_name
ON dim_games(game_name);

-- for release_date creating the index

CREATE INDEX idx_games_release_date
ON dim_games(release_date);

-- for fact table game_metrics creating the index
CREATE INDEX idx_metrics_snapshot
ON fact_game_metrics(snapshot_date);

-- for price creating the index
CREATE INDEX idx_metrics_price
ON fact_game_metrics(price);

SHOW INDEX FROM dim_games;
SHOW INDEX FROM fact_game_metrics;


-- Now, for the composite indexes

