# Write your MySQL query statement below
select score , rank from 
(select score, 
@currank := @currank + IF(@pre_score = score, 0, 1) as rank,
@pre_score := score
from Scores, (select @currank := 0) r, (select @pre_score := null) p
order by Score desc) t
;
