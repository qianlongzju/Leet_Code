# Write your MySQL query statement below
select dep.name as Department, emp.name as Employee, emp.Salary as Salary
from Employee as emp, 
(select d.Id as id, max(e.Salary) as max_salary, d.name as name  from Department as d , Employee as e where d.Id = e.DepartmentId group by Id) as dep
where emp.departmentid = dep.id and emp.salary=dep.max_salary;
