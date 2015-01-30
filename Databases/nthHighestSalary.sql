CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select distinct(Salary) from Employee as emp1
      where N-1=(
          select count(distinct emp2.Salary)
          from Employee as emp2
          where emp2.Salary > emp1.Salary
      )
  );
END
