select Name from Customers where Id not in (select CustomerId from Orders);
