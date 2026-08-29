-- Combines game dimension data with historical game metrics.
-- One row represents one game snapshot.

CREATE OR REPLACE VIEW vw_game_performance AS

SELECT
    g.game_id,
    g.steam_app_id,
    g.game_name,
    g.release_date,

    m.price,
    m.discount_percent,
    m.review_count,
    m.positive_percent,
    m.snapshot_date

FROM dim_games g

INNER JOIN fact_game_metrics m
    ON g.game_id = m.game_id;