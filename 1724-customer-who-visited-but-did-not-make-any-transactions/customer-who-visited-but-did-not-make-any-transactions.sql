/* Write your PL/SQL query statement below */
SELECT customer_id, COUNT(*) AS count_no_trans
FROM (
    SELECT visits.customer_id, transactions.visit_id  /*COUNT(*) AS count_no_trans*/
    FROM visits
    LEFT JOIN transactions
    ON visits.visit_id = transactions.visit_id
)t
WHERE visit_id IS null
GROUP BY customer_id;