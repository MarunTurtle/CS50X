-- Find the accomplice by tracking the phone call and the flight reservation made by the thief.




SELECT DISTINCT p.name
FROM people p
JOIN phone_calls pc ON pc.caller = p.phone_number
WHERE p.phone_number = (
    SELECT DISTINCT pc.receiver
    FROM people p
    JOIN phone_calls pc ON pc.caller = p.phone_number
    WHERE pc.year = 2023
    AND pc.month = 7
    AND pc.day = 28
    AND pc.caller = (
        SELECT p.phone_number
        FROM people p
        WHERE p.name = 'Diana'
    )
)




