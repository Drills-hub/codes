SELECT J.FLAVOR
FROM
    (
    SELECT  SUM(TOTAL_ORDER) AS JULY_TOTAL,FLAVOR
    FROM JULY
    GROUP BY FLAVOR
    ) AS J JOIN FIRST_HALF AS F ON J.FLAVOR = F.FLAVOR
GROUP BY J.FLAVOR
HAVING SUM(J.JULY_TOTAL +F.TOTAL_ORDER)
ORDER BY SUM(J.JULY_TOTAL +F.TOTAL_ORDER) DESC
LIMIT 3;