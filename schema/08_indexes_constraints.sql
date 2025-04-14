
CREATE INDEX idx_sensor_reading_time ON sensor_readings(reading_time);
CREATE INDEX idx_prediction_time ON ml_predictions(prediction_time);

ALTER TABLE motor_sensor_data
    ADD CONSTRAINT chk_voltage CHECK (voltage >= 0),
    ADD CONSTRAINT chk_current CHECK (current >= 0),
    ADD CONSTRAINT chk_temp CHECK (temperature >= -40 AND temperature <= 150);
