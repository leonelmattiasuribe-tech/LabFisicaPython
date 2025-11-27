import numpy as np
import matplotlib.pyplot as plt

# 1. VALORES OBTENIDOS DE LA SEMANA 4 (MMC)
A = 0.0512    
sigma_A = 0.0105 
B = 0.9987    
sigma_B = 0.0050 


# Calcular la constante del resorte (k)
k = (4 * np.pi**2) / B
sigma_k = k * np.abs(sigma_B / B)

print("\n--- Tarea Persona 1: Constante del Resorte (k) ---")
print(f"k = {k:.4f} +- {sigma_k:.4f} [N/m o Unidades Relativas]")


# Calcular el periodo de oscilación T(9m)
X_pred = 9.0 
T2_pred = A + B * X_pred 
T_pred = np.sqrt(T2_pred)
sigma_T_pred = T_pred * np.abs(sigma_B / B)

print("\n--- Tarea Persona 2: Periodo de Oscilación T(9m) ---")
print(f"Periodo T(9m): {T_pred:.4f} +- {sigma_T_pred:.4f} [s]")


#  Graficar el movimiento oscilatorio para 9m
A_amp = 1.0 
T_sim = T_pred 
omega = (2 * np.pi) / T_sim
fase = 0.0 

t = np.linspace(0, 2 * T_sim, 500) 
x_t = A_amp * np.cos(omega * t + fase)

plt.figure(figsize=(10, 6))
plt.plot(t, x_t, 'g-')
plt.title(f'Simulación de Movimiento Armónico Simple (Masa 9m)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición $x(t)$ (m)')
plt.grid(True)
plt.savefig('simulacion_9m_final.png')

print("\n[FIN] Se ha generado la gráfica 'simulacion_9m_final.png'.")
