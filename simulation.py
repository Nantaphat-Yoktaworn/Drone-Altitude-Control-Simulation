import numpy as np
import random
from drone import Drone
from pid import PIDController

drone = Drone()
pid = PIDController(kp=0.3, ki=0.05, kd=5.0)

target_altitude = 10.0
dt = 0.1

for step in range(100):
    ramp_target = min(10.0, step * 0.3)
    
    if step > 50:
        drone.velocity += random.uniform(-1.0, 1.0)  # ลมกระโชก
    
    output = pid.compute(ramp_target, drone.altitude)
    drone.thrust = np.clip(output, 0.0, 1.0)
    drone.update(dt)
    print(f"Step {step+1:03d} | Alt: {drone.altitude:6.2f}m | Vel: {drone.velocity:5.2f}m/s | Thrust: {drone.thrust:.2f}")