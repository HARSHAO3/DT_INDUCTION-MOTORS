CREATE TABLE motor_sensor_data (
    data_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    sensor_id INTEGER REFERENCES sensors(sensor_id),
    voltage FLOAT,
    current FLOAT,
    temperature FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
