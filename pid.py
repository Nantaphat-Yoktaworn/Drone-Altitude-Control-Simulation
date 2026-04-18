import numpy as np

class PIDController:
    def __init__(self, kp, ki, kd, max_integral=10.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max_integral = max_integral
        self.prev_error = 0
        self.integral = 0

    def compute(self, target, current, max_output=5.0):
        error = target - current
        self.integral += error
        self.integral = np.clip(self.integral, -10.0, 10.0)
        
        derivative = error - self.prev_error
        self.prev_error = error

        output = (self.kp * error +
                self.ki * self.integral +
                self.kd * derivative)
        
        # จำกัด output ไม่ให้เกิน max
        output = np.clip(output, -max_output, max_output)
        return output