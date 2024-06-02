-- Find the accomplice by tracking the phone call and the flight reservation made by the thief.

-- Select distinct names from the people table
SELECT DISTINCT p.name
FROM people p
-- Join with phone_calls table to match caller's phone number
JOIN phone_calls pc ON pc.caller = p.phone_number
-- Filter to find the phone number of the receiver of a specific call
WHERE p.phone_number = (
    -- Subquery to find the receiver of the call made on a specific date
    SELECT DISTINCT pc.receiver
    FROM people p
    JOIN phone_calls pc ON pc.caller = p.phone_number
    WHERE pc.year = 2023
    AND pc.month = 7
    AND pc.day = 28
    -- Subquery to find the phone number of 'Diana'
    AND pc.caller = (
        SELECT p.phone_number
        FROM people p
        WHERE p.name = 'Diana'
    )
)