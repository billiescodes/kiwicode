4) What category has the most products?

```sql
SELECT CategoryName, COUNT(categoryname)
FROM categories,products
WHERE Categories.CategoryID = Products.CategoryID
GROUP BY CategoryName
ORDER BY count(categoryname) DESC;
```

Which customers are from the UK?

```sql 
SELECT Country, COUNT(*) 
FROM [Customers]
WHERE Country='UK'
```
ANSWER=7

What is the name of the customer who has the most orders?
```sql
SELECT  CustomerName, count(*) as orders 
FROM Customers join orders
ON Customers.CustomerID = Orders.CustomerID
GROUP BY 1
ORDER BY 2  DESC;
```
ANSWER = Ernest Handle

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
SELECT count(DISTINCT Country)  
FROM [Customers]
```
ANSWER = 21

What category appears in the most orders?


7. What was the total cost for each order?
8. Which employee made the most sales (by total cost)?
9. Which employees have BS degrees? (Hint: look at the LIKE operator.)
10. Which supplier of three or more products has the highest average product price? (Hint: look at the HAVING operator.)

