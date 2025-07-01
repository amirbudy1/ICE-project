import numpy as np
import matplotlib.pyplot as plt

# داده‌های اصلی شما
T = [300, 931.753, 2803.402, 902.622]  # دما (K)
P = [100, 5279.934, 15885.946, 300.874]  # فشار (kPa)
R = 0.287  # ثابت گاز هوا (kJ/kg·K)
v = [R * T_i / P_i for T_i, P_i in zip(T, P)]  # حجم ویژه (m³/kg)

# --- تنظیمات نمودار ---
plt.figure(figsize=(10, 6))
#plt.title('نمودار P-v با فرآیندهای آیزنتروپیک و اتصالات', fontfamily='B Nazanin', fontsize=14)
plt.xlabel('v (m³/kg)', fontfamily='B Nazanin')
plt.ylabel('P (kPa)', fontfamily='B Nazanin')
plt.grid(True, linestyle='--', alpha=0.7)

# --- رنگ یکسان برای تمام خطوط (آبی) ---
line_color = 'blue'  # رنگ خطوط
point_color = 'red'   # رنگ نقاط

# --- رسم نقاط اصلی ---
plt.scatter(v, P, color=point_color, s=100, label=' ', zorder=5)

# --- فرآیند آیزنتروپیک ۱→۲ ---
gamma = 1.4
v_1to2 = np.linspace(v[0], v[1], 100)
P_1to2 = P[0] * (v[0] ** gamma) / (v_1to2 ** gamma)
plt.plot(v_1to2, P_1to2, color=line_color, label=' ۱→۲')

# --- فرآیند آیزنتروپیک ۳→۴ ---
v_3to4 = np.linspace(v[2], v[3], 100)
P_3to4 = P[2] * (v[2] ** gamma) / (v_3to4 ** gamma)
plt.plot(v_3to4, P_3to4, color=line_color, label=' ۳→۴')

# --- اتصال نقاط ۲→۳ و ۴→۱ ---
plt.plot([v[1], v[2]], [P[1], P[2]], color=line_color, linewidth=2, label=' ۲→۳')
plt.plot([v[3], v[0]], [P[3], P[0]], color=line_color, linewidth=2, label=' ۴→۱')

# --- افزودن داده‌های جدید (در صورت نیاز) ---
# مثال: داده‌های جدید به شکل T_new و P_new
# T_new = [...] 
# P_new = [...]
# v_new = [R * T_i / P_i for T_i, P_i in zip(T_new, P_new)]
# plt.scatter(v_new, P_new, color='green', s=100, label='داده‌های جدید')

# نمایش نمودار
plt.legend()

plt.show()