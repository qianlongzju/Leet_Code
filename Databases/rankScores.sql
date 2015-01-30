select Score , rank from 
(
    select Score, 
    @cur_rank := @cur_rank + IF(@pre_score = Score, 0, 1) as rank,
    @pre_score := Score
    from Scores, (select @cur_rank := 0) as r, (select @pre_score := null) as s
    order by Score desc
) t
;
