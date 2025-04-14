SELECT
    u.username,
    m.timestamp,
    p.predicted_fault,
    p.confidence_score
FROM users u
JOIN motor_sensor_data m ON u.user_id = m.user_id
JOIN ml_predictions p ON m.data_id = p.data_id
ORDER BY p.prediction_time DESC;
