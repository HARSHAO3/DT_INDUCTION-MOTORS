CREATE OR REPLACE FUNCTION log_prediction()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO logs (user_id, action)
    VALUES (
        (SELECT user_id FROM motor_sensor_data WHERE data_id = NEW.data_id),
        'ML prediction logged with confidence: ' || NEW.confidence_score
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_prediction
AFTER INSERT ON ml_predictions
FOR EACH ROW EXECUTE FUNCTION log_prediction();
