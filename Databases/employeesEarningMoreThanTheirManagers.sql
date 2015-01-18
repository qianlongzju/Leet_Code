select 
emp.name
from Employee as emp join Employee as man on (emp.managerid=man.id)
where emp.salary > man.salary
;
