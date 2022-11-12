SELECT Users.name, IFNULL(travelled_distance, 0) AS travelled_distance
FROM Users
LEFT JOIN (
        SELECT Rides.user_id, SUM(distance) AS travelled_distance
        FROM Rides
        GROUP BY Rides.user_id
        ) AS TotalDistance ON Users.id = TotalDistance.user_id
ORDER BY travelled_distance DESC, Users.name ASC