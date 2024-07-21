SELECT CATEGORY, price as MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
where (CATEGORY, price)
in
(
SELECT CATEGORY, max(price)
from FOOD_PRODUCT
where CATEGORY IN ('과자','국','김치','식용유')
group by CATEGORY
)
order by MAX_PRICE DESC;