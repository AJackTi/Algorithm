SELECT
    S.Score,
    DENSE_RANK() OVER(
        ORDER BY S.Score DESC
    ) 'Rank'
FROM Scores S