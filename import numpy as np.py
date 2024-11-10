import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Нелинейная емкость
def system1(t, y, L, R, C):
    V, I = y
    dV_dt = I / C(V)
    dI_dt = -R * I / L - V / L
    return [dV_dt, dI_dt]

def C(V):
    # Пример функции нелинейной емкости
    return 1 + 0.1 * V**2

L = 1.0
R = 0.5
y0 = [1.0, 0.0]  # Начальные условия

sol = solve_ivp(system1, [0, 10], y0, args=(L, R, C), method='RK45', t_eval=np.linspace(0, 10, 1000))

plt.plot(sol.y[0], sol.y[1])
plt.xlabel('Voltage (V)')
plt.ylabel('Current (I)')
plt.title('Фазовый портрет системы с нелинейной емкостью')
plt.grid()
plt.show()

# Для случая с нелинейной индуктивностью — аналогичный код, где определена функция L(I)