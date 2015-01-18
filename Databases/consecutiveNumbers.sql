# Write your MySQL query statement below
select distinct(ConsecutiveNums)
from 
(
select 
num as ConsecutiveNums,
IF(@old_old = @old and @old = num, 1, 0) as flag,
@old_old := @old,
@old := num
from Logs, (select @old_old := null) t, (select @old := null) s
) o
where flag = 1;
