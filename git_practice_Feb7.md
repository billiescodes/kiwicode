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
