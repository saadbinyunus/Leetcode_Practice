/* Write your PL/SQL query statement below */
SELECT name
FROM Customer
WHERE referee_id IS null OR referee_id != 2;

/*In SQL, NULL means "unknown", not an actual value.
When u use = Null
SQL reads it as:
"Is this value equal to unknown?"
But SQL cannot determine if something equals an unknown value — so the result is UNKNOWN, not TRUE*/