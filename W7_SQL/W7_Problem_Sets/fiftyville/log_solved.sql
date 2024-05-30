-- Retrieve the crime scene report mentioning the CS50 Duck
SELECT c.description
FROM crime_scene_reports c
WHERE c.description LIKE '%CS50 duck%';

-- Retrieve interviews conducted on July 28, 2023, mentioning the bakery
SELECT p.name, i.transcript
FROM interviews i
JOIN people p on p.name = i.name
WHERE i.transcript LIKE '%bakery%'
AND i.year = 2023
AND i.month = 7
AND i.day = 28;

-- Identify people who match specific criteria related to the crime
WITH ParkingLotExits AS (
    -- People who exited the bakery parking lot between 10:15 and 10:25 on July 28, 2023
    SELECT DISTINCT p.name, bl.hour, bl.minute
    FROM people p
    JOIN bakery_security_logs bl ON p.license_plate = bl.license_plate
    WHERE bl.activity = 'exit'
    AND bl.year = 2023
    AND bl.month = 7
    AND bl.day = 28
    AND bl.hour = 10
    AND 15 <= bl.minute AND bl.minute <= 25
), ATMUsers AS (
    -- People who used the ATM on Leggett Street before 10:15 on July 28, 2023
    SELECT DISTINCT p.name
    FROM people p
    JOIN bank_accounts ba ON p.id = ba.person_id
    JOIN atm_transactions at ON at.account_number = ba.account_number
    WHERE at.transaction_type = 'withdraw'
    AND at.atm_location = 'Leggett Street'
    AND at.year = 2023
    AND at.month = 7
    AND at.day = 28
), Callers AS (
    -- People who made a call immediately after the theft at 10:15 on July 28, 2023
    SELECT DISTINCT p.name
    FROM people p
    JOIN phone_calls pc ON pc.caller = p.phone_number
    WHERE pc.year = 2023
    AND pc.month = 7
    AND pc.day = 28
    AND pc.duration <= 60
), EarliestFlight AS (
    -- People who booked the earliest flight on July 29, 2023
    SELECT p.name
    FROM people p
    JOIN passengers psg ON p.passport_number = psg.passport_number
    WHERE psg.flight_id IN (
        SELECT fl.id
        FROM flights fl
        WHERE fl.year = 2023
        AND fl.month = 7
        AND fl.day = 29
        ORDER BY fl.hour ASC, fl.minute ASC
        LIMIT 1
    )
)

-- Combine all criteria to find the suspect
SELECT p.name
FROM people p
WHERE p.name IN (SELECT name FROM ParkingLotExits)
AND p.name IN (SELECT name FROM ATMUsers)
AND p.name IN (SELECT name FROM Callers)
AND p.name IN (SELECT name FROM EarliestFlight);

-- Identify the accomplice by tracking the phone call made by the thief
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
        WHERE p.name = 'Bruce'
    )
);

-- Determine the destination by tracking the flight booked by the thief
SELECT ap.city
FROM airports ap
JOIN flights fl ON fl.destination_airport_id = ap.id
WHERE fl.id = (
    SELECT fl.id
    FROM flights fl
    WHERE fl.year = 2023
    AND fl.month = 7
    AND fl.day = 29
    ORDER BY fl.hour ASC, fl.minute ASC
    LIMIT 1
);