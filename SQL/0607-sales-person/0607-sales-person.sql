SELECT SalesPerson.name
FROM SalesPerson
WHERE SalesPerson.sales_id NOT IN
    (
        SELECT SalesPerson.sales_id
        FROM SalesPerson
        LEFT JOIN Orders
        ON SalesPerson.sales_id = Orders.sales_id
        WHERE Orders.com_id = (SELECT Company.com_id from Company WHERE Company.name = 'RED')
    )