select distinct(ConsecutiveNums)
from 
(
    select Num as ConsecutiveNums,
    IF(@pre_pre = @pre and @pre = num, 1, 0) as flag,
    @pre_pre := @pre,
    @pre := Num
    from Logs, (select @pre_pre := null) p_p, (select @pre := null) p
) t
where flag = 1;
