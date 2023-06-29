import matplotlib.pyplot as plt
import numpy as np

def simulate_parabolic_motion(v0, theta, g):
    t_flight = 2 * v0 * np.sin(theta) / g
    t = np.linspace(0, t_flight, num=100)
    
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    
    return x, y

# Parámetros iniciales
initial_velocity = 10.0  # Velocidad inicial (m/s)
launch_angle = np.pi / 4  # Ángulo de lanzamiento (en radianes)
gravity = 9.8  # Aceleración debido a la gravedad (m/s^2)

# Simulación del movimiento parabólico
x_vals, y_vals = simulate_parabolic_motion(initial_velocity, launch_angle, gravity)

# Gráfica de la trayectoria
plt.plot(x_vals, y_vals)
plt.xlabel('Distancia (m)')
plt.ylabel('Altura (m)')
plt.title('Simulador de Movimiento Parabólico')
plt.grid(True)
plt.show()
