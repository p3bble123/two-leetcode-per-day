SELECT Visits.customer_id, count(Visits.visit_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE amount is NULL
GROUP BY Visits.customer_id