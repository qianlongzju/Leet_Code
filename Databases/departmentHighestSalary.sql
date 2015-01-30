select dep.name as Department, emp.Name as Employee, emp.Salary as Salary
from Employee as emp,
(
    select d.Id as id, max(e.Salary) as max_salary, d.Name as name  from Employee as e, Department as d  
    where d.Id = e.DepartmentId group by Id) as dep
where emp.DepartmentId = dep.id and emp.Salary=dep.max_salary;
