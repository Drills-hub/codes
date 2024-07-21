select food_type, rest_id, rest_name, favorites 
from rest_info RI
where favorites = 
(
    select max(favorites) 
    from rest_info 
    where food_type=RI.food_type
)
group by food_type
order by food_type desc;