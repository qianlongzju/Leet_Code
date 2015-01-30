select distinct(Email)
from
(
    select Email, count(Id) as cnt
    from Person
    group by Email
) t
where cnt > 1;
