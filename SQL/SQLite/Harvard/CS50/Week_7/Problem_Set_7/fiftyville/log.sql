-- I want to see the crime scene description.
    SELECT * FROM crime_scene_reports
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND street = "Humphrey Street";
    -- The thief stole a CS50 duck.
    -- The theft took place at 10:15 A.M at the Humphrey Street bakery.
    -- There are 3 witnesses, each one of them mentioned the bakery.


-- I want to see what the witnesses said on the interview.
    SELECT * FROM interviews
        WHERE year = 2021
        AND month = 7
        AND day = 28;
    -- The witnesses names are Ruth, Eugene and Raymond.
    -- Ruth said that the thief left the bakery by car sometime within ten minutes of the theft.
    -- Eugene said that she recognized the thief from the ATM on Leggett Street, he was withdrawing some money before the theft.
    -- Raymond said that the thief called someone who talked to them for less them a minute. In the call, Raymond heard the thief talking about his plan of taking the earliest flight out of Fiftyville tomorrow, at 7/29/2021, and the thief asked the person in the call to buy the flight ticket for him.


-- Investigating Ruth's interview.
    -- I want to see the license plates of the cars that left the bakery at around ten minutes after 10:15.
        SELECT * FROM  bakery_security_logs
            WHERE year = 2021
            AND month = 7
            AND day = 28
            AND hour = 10
            AND minute <= 25
            AND minute >= 15
            ORDER BY HOUR;
    -- Nothing very interesting for now, just some license plates.
    -- I'll use this information later.


-- Investigating Eugene's interview.
    -- I want to see the withdrawals that happened on the theft day.
        SELECT * FROM atm_transactions
            WHERE year = 2021
            AND month = 7
            AND day = 28
            AND atm_location = "Leggett Street"
            AND transaction_type = "withdraw";
    -- Nothing very interesting for now, just some account numbers.
    -- I'll use this information later.


-- Investigating Raymond's interview.
    -- I want to see all the calls that happened in the day with less than a minute of duration.
        SELECT * FROM phone_calls
            WHERE year = 2021
            AND month = 7
            AND day = 28
            AND duration < 60;
    -- Nothing very interesting for now, just some phone numbers.
    -- I'll use this information later.

    -- I want to see the earliest flight on Fiftyville airport.
        SELECT * FROM flights
            INNER JOIN airports
            ON airports.id = flights.origin_airport_id
            WHERE flights.year = 2021
            AND flights.month = 7
            AND flights.day = 29
            ORDER BY flights.hour
            LIMIT 1;
    -- The earliest flight was at 7/29/2021 at 8:20 A.M, the flight id is 36, and the destination airport id is 4.

    -- I want to see which airport has the id 4.
        SELECT * FROM airports
            WHERE id = 4;
    -- The name of the airport is LaGuardia Airport, at New York City.
    -- Probably the thief escaped to New York.

    -- I want to see all the passengers from the flight mentioned on the previous lines passport numbers.
        SELECT * FROM passengers
            INNER JOIN flights
            ON flights.id = passengers.flight_id
            WHERE flights.id = 36
            AND flights.destination_airport_id = 4;
    -- Nothing very interesting for now, just some passport numbers.
    -- I'll use this information later.


-- Time to put the evidences together.
    -- I want to see the name of the person who matches with the informations i have in order to find the thief.
        SELECT * FROM people
                WHERE phone_number IN (
                    SELECT phone_calls.caller FROM phone_calls
                        WHERE year = 2021
                        AND month = 7
                        AND day = 28
                        AND duration < 60
                )

                AND passport_number IN(
                    SELECT passengers.passport_number FROM passengers
                        INNER JOIN flights
                        ON flights.id = passengers.flight_id
                            WHERE flights.id = 36
                            AND flights.destination_airport_id = 4
                )

                AND license_plate IN (
                    SELECT bakery_security_logs.license_plate FROM bakery_security_logs
                        WHERE year = 2021
                        AND month = 7
                        AND day = 28
                        AND hour = 10
                        AND minute <= 25
                        AND minute >= 15
                )

                AND id IN (
                    SELECT bank_accounts.person_id FROM bank_accounts
                    INNER JOIN atm_transactions
                    ON bank_accounts.account_number = atm_transactions.account_number
                    WHERE atm_transactions.account_number IN (
                        SELECT atm_transactions.account_number FROM atm_transactions
                            WHERE atm_transactions.year = 2021
                            AND atm_transactions.month = 7
                            AND atm_transactions.day = 28
                            AND atm_transactions.atm_location = "Leggett Street"
                            AND atm_transactions.transaction_type = "withdraw"
                    )
                );
    -- The name of the person who matches with the informations i have is Bruce. His id is 686048, his phone number is (367) 555-5533, his passport number is 5773159633 and his license plate is 94Kl13X.
    -- Bruce escaped to New York, he went to LaGuardia Airport.
    -- Now it's time to find his accomplice.

    -- I want to see who Bruce called at the theft.
        SELECT * FROM people
            WHERE phone_number IN (
                SELECT phone_calls.receiver FROM phone_calls
                    WHERE year = 2021
                    AND month = 7
                    AND day = 28
                    AND duration < 60
                    AND caller = "(367) 555-5533"
            );
    -- Bruce called Robin, so Robin is his accomplice. His id is 864400, his phone number is (375) 555-8161, he doesn't have a passport number and his license plate is 4V16VO0.


-- The mystery is now solved!
