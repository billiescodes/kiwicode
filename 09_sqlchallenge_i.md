# Challenge Set 9
## Part I: W3Schools SQL Lab

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?

``` sql
SELECT CustomerName, Country
FROM Customers
WHERE Country = 'UK'
```

2. What is the name of the customer who has the most orders?

```sql
SELECT  CustomerName, count(*) as orders 
FROM Customers join orders
ON Customers.CustomerID = Orders.CustomerID
GROUP BY 1
ORDER BY 2  DESC;
```

3. Which supplier has the highest average product price?
```sql
SELECT Suppliers.SupplierName, Suppliers.SupplierID, Products.SupplierID, AVG(Products.Price) AS AvgPrice
FROM Products 
LEFT JOIN Suppliers
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Price
ORDER BY AvgPrice DESC;
	
```
4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
```sql
SELECT count(DISTINCT Country)  
FROM [Customers]
```

5. What category appears in the most orders

Order of joining variables with Tables
[Orders] - order ID -- [OrderDetails] - prodcutID - [Producets] - Category ID [Categgories]
```sql
SELECT Orders.OrderID, OrderDetails.OrderID, Categories.CategoryID,
		COUNT(DISTINCT Categories.CategoryID)
FROM Orders
LEFT JOIN OrderDetails ON Orders.OrderID =OrderDetails.OrderID
LEFT JOIN Products ON OrderDetails.ProductID =  Products.ProductID
LEFT JOIN Categories ON Products.CategoryID = Categories.CategoryID
GROUP BY Orders.OrderID
ORDER BY COUNT(DISTINCT Categories.CategoryID) DESC
```
ANSWER =  2& 7

6. What was the total cost for each order?
[Orders] - order ID -- [OrderDetails] - prodcutID - [Products] --> get price

```sql
SELECT Sum(PRICE), Orders.OrderID
FROM [Products]
LEFT JOIN OrderDetails on Products.ProductID= OrderDetails.ProductID
LEFT JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
Group BY Orders.OrderID 
ORDER BY Sum(Price) DESC
```

7. Which employee made the most sales (by total price)?
[products]-- productID-- [OrderDetailID] orderdetail, OrderID [Orders] Employee ID [Employees]

```sql
SELECT Employees.LastName, Employees.FirstName, 
	Products.Price As PRICE
FROM [Employees]
LEFT JOIN  ORDERS ON employees.EmployeeID=Orders.EmployeeID
LEFT JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY LastName, FirstName
Order BY Sum(Price)
```


8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
```sql
SELECT LastName, FirstName
FROM [Employees]
WHERE NOTES LIKE '%BS%  
```


9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

[supplier] -- 	SupplierID -- [Product]

```sql
SELECT Products.ProductID, Suppliers.SupplierName, AVG(Products.Price) as AvgPrice
FROM Products
LEFT JOIN Suppliers ON Products.SupplierID=Suppliers.SupplierID
Group By SupplierName
HAVING Sum(DISTINCT ProductID)  > 2
ORDER BY AvgPrice DESC
```
