CREATE TABLE sensor_readings (
    reading_id SERIAL PRIMARY KEY,
    sensor_id INTEGER REFERENCES sensors(sensor_id),
    reading_value FLOAT NOT NULL,
    reading_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
