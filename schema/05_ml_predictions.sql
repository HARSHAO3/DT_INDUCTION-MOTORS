CREATE TABLE ml_predictions (
    prediction_id SERIAL PRIMARY KEY,
    data_id INTEGER REFERENCES motor_sensor_data(data_id),
    predicted_fault VARCHAR(100),
    confidence_score FLOAT,
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
