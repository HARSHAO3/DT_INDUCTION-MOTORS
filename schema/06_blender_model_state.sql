CREATE TABLE blender_model_state (
    model_state_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    motor_status VARCHAR(50),
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
