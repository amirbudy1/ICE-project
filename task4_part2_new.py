import numpy as np
import matplotlib.pyplot as plt

R   = 0.287
k   = 1.4
T_t = 300
T_u = 1000
P_t = 105
CdAt = 0.0004
P_u = np.arange(105,401)
V_t = []
m_dot = []

sonic_border = P_t * ((k+1)/2) ** (k/(k-1))
for p in P_u:
    if p <= sonic_border:
        first    = 2000 * R * T_u
        second   = k / (k-1)
        third    = 1 - (P_t / p) ** ((k-1)/k)
    # print(first * second * third)
        velocity = np.sqrt(first* second * third)
        V_t.append(velocity)
    else :
        velocity = np.sqrt((2000 * k / (k + 1)) * R * T_u)
        V_t.append(velocity)

for p in P_u:
   # if p < sonic_border :
        A = CdAt * p
        B = np.sqrt(2 / (R * T_t) * (k/(k-1)) * (P_t / p) ** ((3-k)/k))
        C = np.sqrt(1 - (P_t / p) ** ((k-1)/k))
        m_dot.append(A*B*C)
   # else:
        # A = CdAt * p
        # B = np.sqrt(k/(R*T_t) * (P_t / p)**(k/(k-1)) )
        # C = np.sqrt((2 / (k+1))**((k+1)/(k-1)))
        # m_dot.append(A*B*C)

plt.figure(figsize=(10, 5))
plt.plot(P_u, V_t, label='Velocity')

plt.axvline(x=sonic_border, color='r', linestyle='--')
plt.axvline(x=P_t, color='r', linestyle='--')

plt.text(sonic_border - 20, max(V_t)/2, 'Subsonic Region',
         horizontalalignment='right', verticalalignment='center', fontsize=12)
plt.text(sonic_border + 20, max(V_t)/2, 'Sonic Region',
         horizontalalignment='left', verticalalignment='center', fontsize=12)

plt.grid(True)
plt.legend()
plt.xlabel('Pressure (kPa)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Pressure ')
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(P_u, m_dot, label='m_dot')

plt.axvline(x=sonic_border, color='r', linestyle='--')
#plt.axvline(x=P_t, color='r', linestyle='--')

#plt.text(sonic_border - 20, max(V_t)/2, 'Subsonic Region',
#         horizontalalignment='right', verticalalignment='center', fontsize=12)
#plt.text(sonic_border + 20, max(V_t)/2, 'Sonic Region',
#         horizontalalignment='left', verticalalignment='center', fontsize=12)

plt.grid(True)
plt.legend()
plt.xlabel('Pressure (kPa)')
plt.ylabel('mass flow rate s (kg/s)')
plt.title('mass flow rate vs Pressure ')
plt.show()