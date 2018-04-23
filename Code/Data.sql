SELECT    EmployeeID, FirstName, LastName, HireDate, City
FROM      Employees
WHERE     HireDate NOT BETWEEN '1-june-1992' AND '15-december-1993'