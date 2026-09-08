/*
Steam Market Intelligence
Analytical Dataset View

Purpose:
    Create a clean denormalized dataset for:
        - CSV export
        - SQL Case Study
        - Python EDA
        - Kaggle dataset
        - Power BI

Uses the latest available snapshot.
*/

CREATE OR REPLACE VIEW vw_steam_analytical_dataset AS

SELECT 
    g.game_id,
    g.steam_app_id,
    g.game_name,
    g.release_date,

    d.developer_name,
    p.publisher_name,
    ge.genre_name,
    pl.platform_name,

    m.price,
    m.discount_percent,
    m.review_count,
    m.positive_percent,
    m.snapshot_date

FROM dim_games AS g

LEFT JOIN bridge_game_developers AS gd
    ON g.game_id = gd.game_id

LEFT JOIN dim_developers AS d
    ON gd.developer_id = d.developer_id

LEFT JOIN bridge_game_publishers AS gp
    ON g.game_id = gp.game_id

LEFT JOIN dim_publishers AS p
    ON gp.publisher_id = p.publisher_id

LEFT JOIN bridge_game_genres AS gg
    ON g.game_id = gg.game_id

LEFT JOIN dim_genres AS ge
    ON gg.genre_id = ge.genre_id

LEFT JOIN bridge_game_platforms AS gpl
    ON g.game_id = gpl.game_id

LEFT JOIN dim_platforms AS pl
    ON gpl.platform_id = pl.platform_id

LEFT JOIN fact_game_metrics AS m
    ON g.game_id = m.game_id

WHERE m.snapshot_date = (
    SELECT MAX(snapshot_date)
    FROM fact_game_metrics
);