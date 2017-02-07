4) What category has the most products?

```sql
SELECT CategoryName, COUNT(categoryname)
FROM categories,products
WHERE Categories.CategoryID = Products.CategoryID
GROUP BY CategoryName
ORDER BY count(categoryname) DESC;
```

Which customers are from the UK?

```sql SELECT Country, COUNT(*) 
FROM [Customers]
WHERE Country='UK'
```
ANSWER=7

What is the name of the customer who has the most orders?
```sql
SELECT CustomerID,  COUNT(CustomerID)
FROM Orders, Customers
WHERE Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerID
ORDER BY COUNT(CustomerID) DESC;

or:
SELECT  COUNT(Orders.CustomerID),Customers.CustomerID
FROM Orders
LEFT JOIN Customers
ON Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerID
ORDER BY COUNT(CustomerID) DESC;
```
??

Which supplier has the highest average product price?
```sql
SELECT Suppliers.SupplierName, Suppliers.SupplierID, Products.SupplierID, AVG(Products.Price) AS AvgPrice
FROM Products 
LEFT JOIN Suppliers
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Price
ORDER BY AvgPrice DESC;
	
```
ANSWER = Aux joyeux ecclésiastiques




How many different countries are all the customers from?
```sql
SELECT DISTINCT Country 
FROM [Customers]
```
ANSWER = 21

What category appears in the most orders?


