CREATE OR REPLACE FUNCTION insert_motor_data(
    uid INT, sid INT, volt FLOAT, curr FLOAT, temp FLOAT
) RETURNS VOID AS $$
BEGIN
    INSERT INTO motor_sensor_data (user_id, sensor_id, voltage, current, temperature)
    VALUES (uid, sid, volt, curr, temp);
END;
$$ LANGUAGE plpgsql;
