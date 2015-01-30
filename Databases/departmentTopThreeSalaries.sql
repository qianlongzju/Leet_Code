select Department, Employee, Salary
from 
(
    select Department, Employee, Salary,
    @cur_rank := IF(@pre_dep = Department, @cur_rank + IF(@pre_salary = Salary, 0, 1), 1) as rank,
    @pre_dep := Department,
    @pre_salary := Salary
    from (select @cur_rank := 0) r, (select @pre_dep := null) d, (select @pre_salary := null) s,
         (
         select dep.Name as Department, emp.Name as Employee, emp.Salary as Salary from Employee as emp, Department as dep 
         where emp.DepartmentId = dep.Id order by dep.Name, emp.Salary desc) q
) as t
where rank <= 3;
