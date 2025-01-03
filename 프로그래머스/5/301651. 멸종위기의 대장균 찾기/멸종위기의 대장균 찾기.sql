WITH RECURSIVE GENERATION_TREE AS (
    -- 최초 세대(Generation 1) 설정
    SELECT 
        ID,
        PARENT_ID,
        1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 재귀적으로 세대 확장
    SELECT 
        E.ID,
        E.PARENT_ID,
        G.GENERATION + 1 AS GENERATION
    FROM ECOLI_DATA E
    JOIN GENERATION_TREE G
    ON E.PARENT_ID = G.ID
)
-- 세대별 자식 없는 개체 계산
SELECT 
    COUNT(*) AS COUNT,
    GENERATION
FROM GENERATION_TREE G
WHERE G.ID NOT IN (SELECT PARENT_ID FROM ECOLI_DATA WHERE PARENT_ID IS NOT NULL)
GROUP BY GENERATION
ORDER BY GENERATION ASC;
