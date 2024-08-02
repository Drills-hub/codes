SELECT P.ID, P.NAME, PS.HOST_ID
FROM PLACES P JOIN(
                    SELECT HOST_ID
                    FROM PLACES
                    GROUP BY 1
                    HAVING COUNT(HOST_ID) >= 2
                    ) PS ON P.HOST_ID = PS.HOST_ID
ORDER BY 1;