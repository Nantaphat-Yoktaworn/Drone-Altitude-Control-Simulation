# Drone-Altitude-Control-Simulation
Try to control drone height with PID

## Features
- Physics simulation (gravity + thrust)
- PID Controller พร้อม integral windup protection
- Setpoint ramping สำหรับ smooth takeoff
- Wind disturbance simulation

## Results
- Stable at 10m target altitude
- Handles random wind disturbance ±1.0 m/s
- Tuned: kp=0.3, ki=0.05, kd=5.0