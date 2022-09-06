-- Prints the number of records within a group in a table in the database
SELECT score, COUNT(score) AS number FROM second_table
    GROUP BY score
    ORDER BY number DESC;
