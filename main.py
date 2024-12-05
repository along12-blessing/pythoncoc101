distance = float(input("Enter the distance (in meters):"))
time = float(input("Enter the time (in seconds):"))
speed = distance / time
print(f"speed = {speed} m/s")

mass = float(input("Enter the mass (in kg): "))
acceleration = float(input("Enter the acceleration (in m/s^2): "))
force = mass * acceleration
print(f"force = {force} N")

height = float(input("Enter the height (in meters): "))
gravity = 9.8 # Acceleration due to gravity (in m/s^2)
potential_energy = mass * gravity * height
print(f"Gravitational Potential Energy = {potential_energy} J")

mass = float(input("Enter the mass (in kg): "))
velocity = float(input("Enter the velocity (in m/s): "))
kinetic_energy = 0.5 * mass * velocity**2
print(f"Kinetic Energy = {kinetic_energy} J")

current = float(input("Enter the current(in amperes):"))
resistance = float(input("enter the resistance (in ohms):"))
volatge = current * resistance
print(f"voltage = {volatge} J")
