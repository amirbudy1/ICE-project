import numpy as np
import matplotlib.pyplot as plt

opening_intake  = -270  # deg
opening_exhaust = -90
duration = 360  # deg


def lift_cal(theta_opening, theta_duration):
    l        = 8  # mm

    theta_values = np.arange(theta_opening, theta_opening + theta_duration)
    lift = []

    for theta in theta_values:
        lift_stationary = l * abs(np.sin(np.pi * (theta - theta_opening) / duration))
        lift.append(lift_stationary)
    return lift
theta_intake = np.arange(-270, 90)
theta_exhuast = np.arange(-90, 270)



plt.figure(figsize=(10, 5))
plt.plot(theta_intake, lift_cal(opening_intake, duration), label=f'Lift (max={8}mm)')
plt.plot(theta_exhuast, lift_cal(opening_exhaust, duration))
plt.xlabel('Theta (degrees)')
plt.ylabel('Lift (mm)')
plt.title('Lift as a function of Theta')
plt.xlim(-360, 360)
plt.xticks(np.arange(-360, 361, 45))  # Tick marks every 45 degrees

# Add vertical line at 0
plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)

plt.grid(True)
plt.legend()
plt.show()