select a.Id from Weather a, Weather b where DATEDIFF(a.Date, b.Date) = 1 and a.Temperature > b.Temperature;
