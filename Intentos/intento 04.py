import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

def simulate_parabolic_motion(v0, theta, g):
    t_flight = 2 * v0 * np.sin(theta) / g
    t = np.linspace(0, t_flight, num=100)
    
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    
    return x, y

def simulate_button_click():
    v0 = float(velocity_entry.get())
    theta = np.deg2rad(float(angle_entry.get()))
    g = float(gravity_entry.get())

    fig, ax = plt.subplots()  # Crear una nueva figura con subtramas

    x_vals, y_vals = simulate_parabolic_motion(v0, theta, g)
    ax.plot(x_vals, y_vals, label=f'v0={v0}, theta={np.rad2deg(theta)}, g={g}')

    ax.set_xlabel('Distancia (m)')
    ax.set_ylabel('Altura (m)')
    ax.set_title('Simulador de Movimiento Parabólico')
    ax.grid(True)
    ax.legend()  # Mostrar leyendas para identificar cada trayectoria
    plt.show()

# Crear la ventana principal
window = tk.Tk()
window.title("Simulador de Movimiento Parabólico")

# Crear etiquetas y campos de entrada
velocity_label = tk.Label(window, text="Velocidad inicial (m/s):")
velocity_label.pack()
velocity_entry = tk.Entry(window)
velocity_entry.pack()

angle_label = tk.Label(window, text="Ángulo de lanzamiento (grados):")
angle_label.pack()
angle_entry = tk.Entry(window)
angle_entry.pack()

gravity_label = tk.Label(window, text="Aceleración debido a la gravedad (m/s^2):")
gravity_label.pack()
gravity_entry = tk.Entry(window)
gravity_entry.pack()

# Crear botón de simulación
simulate_button = tk.Button(window, text="Simular", command=simulate_button_click)
simulate_button.pack()

# Iniciar el bucle de eventos de la ventana
window.mainloop()
