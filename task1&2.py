import numpy as np
# define values
P3_P2 = 1.7
P1 = 100000
T1 = 300
k = 1.4
T_max = 2500
U = []
i = 0
c_v = 718
c_p = 1005

# loop for CR range
for CR in range(12, 19):
    T2 = T1 * (CR) ** (1.4 - 1)
    P2 = P1 * (CR) ** k
    T3 = T2 * P3_P2
    P3 = P2 * P3_P2
    r_c = (CR - 1) * 0.05 + 1
    T4 = r_c * T3
    P4 = P3
    T5 = T4 * ((CR / r_c) ** (-0.4))
    P5 = P4 * ((CR / r_c) ** (1.4))
    # calculate heat
    q1 = c_v * (T3 - T2)
    q2 = c_p * (T4 - T3)
    q_in = q1 + q2
    q_out = c_v * (T5 - T1)
    etta = 1 - (q_out / q_in)
    # check T4 condition
    if T4 < 2500:
        # append values to U matrix
        U.append([CR,(T2*287/P2),P2,(T3*287/P3),P3,(T4*287/P4),P4,(T5*287/P5),P5])
        i += 1
# Values for Otto cycle
q_in1 = 1.343844130880061e+06
CR = 17
# Otto cycle
T2_otto = T1 * (CR) ** (1.4 - 1)
P2_otto = P1 * (CR) ** k
T3_otto = T2_otto + q_in1 / c_v
P3_otto = P2_otto * (T3_otto / T2_otto)
P4_otto = P3_otto * ((1 / CR) ** 1.4)
T4_otto = T3_otto * ((1 / CR) ** (0.4))
q_out_otto = c_v * (T4_otto - T1)
etta_otto = 1 - (q_out_otto / q_in1)
# Diesel cycle
T2_diesel = T1 * (CR) ** (1.4 - 1)
P2_diesel = P1 * (CR) ** k
P3_diesel = P2_diesel
T3_diesel = T2_diesel + q_in1 / c_p
r_c_diesel = T3_diesel / T2_diesel
T4_diesel = T3_diesel * ((CR / r_c_diesel) ** (-0.4))
P4_diesel = P3_diesel * ((CR / r_c_diesel) ** (-1.4))
q_out_diesel = c_v * (T4_diesel - T1)
etta_diesel = 1 - (q_out_diesel / q_in1)
# Output results for U
print(np.array(U))
print('etta_diesel = ', etta_diesel)
print('etta_otto = ' , etta_otto)
print(T2_otto,P2_otto/1000,'\n',T3_otto,P3_otto/1000,'\n',T4_otto,P4_otto/1000,'\n -------------')
print(T2_diesel,P2_diesel/1000,'\n',T3_diesel,P3_diesel/1000,'\n',T4_diesel,P4_diesel/1000,'\n -------------')