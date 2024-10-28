import numpy as np
import matplotlib.pyplot as plt


def simulate_spring_oscillations(m, k, c, x0, v0, t_max=20, dt=0.01):
    """
    Моделирует энергетические превращения при колебании груза на пружине с учетом сопротивления среды.

    Параметры:
    m : float  - масса груза (кг)
    k : float  - коэффициент жесткости пружины (Н/м)
    c : float  - коэффициент сопротивления среды
    x0 : float - начальное смещение (м)
    v0 : float - начальная скорость (м/с)
    t_max : float - максимальное время моделирования (с)
    dt : float - шаг по времени (с)
    """
    # Число шагов моделирования
    n_steps = int(t_max / dt)

    # Инициализация массивов для хранения значений
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    time = np.linspace(0, t_max, n_steps)

    # Начальные условия
    x[0] = x0
    v[0] = v0

    # Массивы для хранения энергии
    kinetic_energy = np.zeros(n_steps)
    potential_energy = np.zeros(n_steps)
    total_energy = np.zeros(n_steps)

    # Метод Эйлера для численного решения уравнения
    for i in range(1, n_steps):
        # Вычисление ускорения
        a = -(k / m) * x[i - 1] - (c / m) * v[i - 1]

        # Обновление скорости и положения
        v[i] = v[i - 1] + a * dt
        x[i] = x[i - 1] + v[i - 1] * dt

        # Расчет энергий
        kinetic_energy[i] = 0.5 * m * v[i] ** 2
        potential_energy[i] = 0.5 * k * x[i] ** 2
        total_energy[i] = kinetic_energy[i] + potential_energy[i]

    # Построение графиков
    plt.figure(figsize=(12, 8))

    # Кинетическая энергия
    plt.subplot(3, 1, 1)
    plt.plot(time, kinetic_energy, label="Кинетическая энергия", color="blue")
    plt.xlabel("Время (с)")
    plt.ylabel("Энергия (Дж)")
    plt.title("Зависимость кинетической энергии от времени")
    plt.grid(True)
    plt.legend()

    # Потенциальная энергия
    plt.subplot(3, 1, 2)
    plt.plot(time, potential_energy, label="Потенциальная энергия", color="green")
    plt.xlabel("Время (с)")
    plt.ylabel("Энергия (Дж)")
    plt.title("Зависимость потенциальной энергии от времени")
    plt.grid(True)
    plt.legend()

    # Полная механическая энергия
    plt.subplot(3, 1, 3)
    plt.plot(time, total_energy, label="Полная механическая энергия", color="red")
    plt.xlabel("Время (с)")
    plt.ylabel("Энергия (Дж)")
    plt.title("Зависимость полной механической энергии от времени")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


# Ввод параметров с консоли с проверкой корректности
def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите число.")


# Получение параметров
m = get_positive_float_input("Введите массу груза (кг): ")
k = get_positive_float_input("Введите коэффициент жесткости пружины (Н/м): ")
c = get_positive_float_input("Введите коэффициент сопротивления среды: ")
x0 = get_positive_float_input("Введите начальное смещение (м): ")
v0 = get_positive_float_input("Введите начальную скорость (м/с): ")

# Запуск моделирования
simulate_spring_oscillations(m, k, c, x0, v0)
