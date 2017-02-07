4) What category has the most products?

'''
SELECT CategoryName, COUNT(categoryname)
FROM categories,products
WHERE Categories.CategoryID = Products.CategoryID
GROUP BY CategoryName
ORDER BY count(categoryname) DESC;
'''

Which customers are from the UK?
>>> SELECT Country, COUNT(*) 
FROM [Customers]
WHERE Country='UK'


What is the name of the customer who has the most orders?
```sql
SELECT CustomerID,  COUNT(CustomerID)
FROM Orders, Customers
WHERE Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerID
ORDER BY COUNT(CustomerID) DESC;
```
??
