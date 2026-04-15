/* Write your PL/SQL query statement below */
/*
LEFT JOIN
*/

SELECT employeeUNI.unique_id as unique_id, employees.name as name
FROM employees
LEFT JOIN employeeUNI
ON employees.id = employeeUNI.id;