# # Mass (in kg): 5
# # Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
# # Time (in seconds): 10
# # Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
# # Cross sectional area (in m^2): 0.01
# # Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5

# # The inner value of c is: 0.003
# # The velocity after 10.0 seconds is: 67.512 m/s

# in terminal install the dependency: pip3 install matplotlib

import math
from matplotlib import pyplot as plt
import numpy as np

m = float(input("Mass (in kg):\t"))
g = float(input("What's gravity? (9.8 for earth) (24 for jupiter)):\t"))
t = float(input("Time (in seconds):\t"))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water):\t"))
A = float(input("Cross sectional area (in m^2)\t"))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder):\t"))

# formulas:
c = (1 / 2) * p * A * C

velocity = math.sqrt((m * g) / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))



# output:
print(f"The inner value of c is: {round(c, 3)}")
print(f"Velocity after {t} seconds is: {velocity: .3f} m/s")

# graph it for the user:
figure, axes = plt.subplots()

axes.set_title("Gravity Differences")

plt.xlabel("Time")
plt.ylabel("Velocity")

# start, stop
line = np.linspace(0, t)

bowling_ball = 3.14 * 8 ** 2
bread = 3.14 * 5 ** 2

axes.plot(line, line * bowling_ball, label="Bowling Ball")
axes.plot(line, line * bread, label="Bread")


axes.legend()
plt.show()