CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct(salary) from Employee as emp1
      where N-1=(
      select count(distinct emp2.salary)
      from Employee as emp2
      where emp2.salary > emp1.salary)
      
  );
END
