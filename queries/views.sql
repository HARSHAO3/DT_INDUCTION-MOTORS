CREATE VIEW recent_sensor_activity AS
SELECT
    s.sensor_name,
    sr.reading_value,
    sr.reading_time
FROM sensors s
JOIN sensor_readings sr ON s.sensor_id = sr.sensor_id
ORDER BY sr.reading_time DESC
LIMIT 100;
