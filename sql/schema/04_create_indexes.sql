-- Now, creating the indexes for efficiently scanning the entire table, which reduces the execution time on a large datasets.

-- for games creating the index
CREATE INDEX idx_games_name
ON dim_games(game_name);

-- for release_date creating the index

CREATE INDEX idx_games_release_date
ON dim_games(release_date);

-- fact_game_metrics
CREATE INDEX idx_metrics_snapshot
ON fact_game_metrics(snapshot_date);

-- for snapshot_date and game_id creating the composite index
CREATE INDEX idx_game_snapshot
ON fact_game_metrics(game_id, snapshot_date);






