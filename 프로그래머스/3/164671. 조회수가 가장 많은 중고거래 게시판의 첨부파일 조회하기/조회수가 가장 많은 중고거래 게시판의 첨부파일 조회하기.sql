SELECT CONCAT('/home/grep/src/',UB.BOARD_ID,'/',UF.FILE_ID,UF.FILE_NAME,UF.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD AS UB JOIN USED_GOODS_FILE AS UF ON
     UB.BOARD_ID = UF.BOARD_ID
WHERE UB.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY UF.FILE_ID DESC;

