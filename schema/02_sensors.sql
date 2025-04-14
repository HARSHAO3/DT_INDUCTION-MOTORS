CREATE TABLE sensors (
    sensor_id SERIAL PRIMARY KEY,
    sensor_type VARCHAR(50) NOT NULL,
    sensor_name VARCHAR(50) NOT NULL,
    unit VARCHAR(20),
    location VARCHAR(100),
    installation_date DATE
);
