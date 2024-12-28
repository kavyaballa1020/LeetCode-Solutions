SELECT c.name as Customers
from Customers as c
LEFT JOIN Orders as o
ON c.id = o.customerId
WHERE o.customerId is NULL;