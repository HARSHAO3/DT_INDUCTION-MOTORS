-- Average temperature by day
SELECT
    DATE(timestamp) AS day,
    AVG(temperature) AS avg_temp
FROM motor_sensor_data
GROUP BY day
ORDER BY day DESC;

-- Fault prediction frequency
SELECT
    predicted_fault,
    COUNT(*) AS fault_count
FROM ml_predictions
GROUP BY predicted_fault
ORDER BY fault_count DESC;
