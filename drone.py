class Drone:
    def __init__(self):
        self.altitude = 0.0
        self.velocity = 0.0
        self.battery = BatteryManager(100, 80)
        self.thrust = 0.0
    
    def update(self, dt):
        gravity = -9.8      # m/s²
        max_thrust = 15.0   # m/s² (thrust เต็มที่)

        acceleration = (self.thrust * max_thrust) + gravity
        self.velocity += acceleration * dt
        self.altitude += self.velocity * dt

        # ไม่ให้จมดิน
        if self.altitude < 0:
            self.altitude = 0
            self.velocity = 0

class BatteryManager:
    def __init__(self, capacity = 100, current = 0):
        self.capacity = capacity
        self.current = current
    
    def discharge(self, amount):
        if self.current - amount < 0:
            self.current = 0
        else:
            self.current -= amount
    
    def charge(self, amount):
        if self.current + amount > self.capacity:
            self.current = self.capacity
        else:
            self.current += amount

    def status(self):
        return f"Battery: {self.current}/{self.capacity} ({(self.current/self.capacity)*100:.1f}%)"
