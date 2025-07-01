import numpy as np
import matplotlib.pyplot as plt

# داده‌های ورودی
T = [300, 931.753, 2268.911, 1042.905]  # دما (K)
P = [100, 5279.934, 5279.934, 347.635]    # فشار (kPa)

# محاسبه حجم ویژه (v = RT/P)
R = 0.287  # ثابت گاز هوا (kJ/kg·K)
v = [R * T_i / P_i for T_i, P_i in zip(T, P)]  # m³/kg

# تنظیمات نمودار
plt.figure(figsize=(10, 6))
#plt.title', fontfamily='B Nazanin', fontsize=14)
plt.xlabel('v(m³/kg)', fontfamily='B Nazanin')
plt.ylabel('P (kPa)', fontfamily='B Nazanin')
plt.grid(True, linestyle='--', alpha=0.7)

# رنگ‌بندی
process_colors = {
    'isentropic': 'red',
    'isobar': 'green',
    'isochor': 'blue'
}

# --- رسم نقاط اصلی ---
plt.scatter(v, P, color='black', s=100, zorder=5)

# --- فرآیند 1→2 (آیزنتروپیک) ---
gamma = 1.4
v_1to2 = np.linspace(v[0], v[1], 100)
P_1to2 = P[0] * (v[0] ** gamma) / (v_1to2 ** gamma)
plt.plot(v_1to2, P_1to2, '-', label='1→2 ')

# --- فرآیند 2→3 (ایزوبار) ---
v_2to3 = np.linspace(v[1], v[2], 100)
P_2to3 = np.full_like(v_2to3, P[1])  # فشار ثابت
plt.plot(v_2to3, P_2to3, '-', label='2→3 ()')

# --- فرآیند 3→4 (آیزنتروپیک) ---
v_3to4 = np.linspace(v[2], v[3], 100)
P_3to4 = P[2] * (v[2] ** gamma) / (v_3to4 ** gamma)
plt.plot(v_3to4, P_3to4, '-', label='3→4 ()')

# --- فرآیند 4→1 (ایزوکور) ---
v_4to1 = np.linspace(v[3], v[0], 100)
P_4to1 = np.linspace(P[3], P[0], 100)  # حجم ثابت (خط عمودی در نمودار v-P)
plt.plot([v[3], v[0]], [P[3], P[0]], '-', label='4→1 ()')

# نمایش نمودار
plt.legend()

plt.show()

# محاسبات تکمیلی
print("حجم ویژه در هر نقطه:")
for i, (v_i, P_i) in enumerate(zip(v, P)):
    print(f"نقطه {i+1}: v = {v_i:.4f} m³/kg, P = {P_i:.2f} kPa")