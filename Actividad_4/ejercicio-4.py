import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  # Importa la función de densidad de probabilidad de la distribución normal

# Parámetros del modelo
total_units = 256  # Cantidad total de unidades a producir
num_stations = 10   # Número de estaciones de trabajo
processing_times = [10, 15, 20, 15, 10, 15, 12, 18,2,38]  # Tiempos de procesamiento en cada estación
arrival_rate = 4  # Tasa de llegada de unidades por hora

# Simulación
def simulate_assembly_line(total_units, num_stations, mean_processing_times, arrival_rate):
    times_in_system = []
    for _ in range(total_units):
        arrival_time = np.random.exponential(scale=1 / arrival_rate)
        times_at_stations = [0] * num_stations
        for i in range(num_stations):
            # Generate random processing time for each station
            processing_time = np.random.exponential(scale=mean_processing_times[i])
            if i > 0:
                times_at_stations[i] = max(times_at_stations[i - 1] + processing_time, arrival_time)
            else:
                times_at_stations[i] = arrival_time + processing_time
        exit_time = times_at_stations[-1]
        times_in_system.append(exit_time - arrival_time)
    return times_in_system

# Ejecución de la simulación
simulation_results = simulate_assembly_line(total_units, num_stations, processing_times, arrival_rate)

# Análisis de resultados
avg_time_in_system = np.mean(simulation_results)
max_time_in_system = np.max(simulation_results)
min_time_in_system = np.min(simulation_results)
std_deviation_time_in_system = np.std(simulation_results)
percentile_95_time_in_system = np.percentile(simulation_results, 95)

# Resultados
print(f"Tiempo promedio en el sistema: {avg_time_in_system:.2f}")
print(f"Tiempo máximo en el sistema: {max_time_in_system:.2f}")
print(f"Tiempo mínimo en el sistema: {min_time_in_system:.2f}")
print(f"Desviación estándar de los tiempos en el sistema: {std_deviation_time_in_system:.2f}")
print(f"Percentil 95 de los tiempos en el sistema: {percentile_95_time_in_system:.2f}")

# Visualización de resultados
plt.hist(simulation_results, bins=20, edgecolor='blue')
plt.xlabel('Tiempo en el sistema')
plt.ylabel('Frecuencia')
plt.title('Distribución de Tiempos en el Sistema')
plt.axvline(x=avg_time_in_system + std_deviation_time_in_system, color='red', linestyle='--', label='Desviación Estándar')
plt.axvline(x=avg_time_in_system - std_deviation_time_in_system, color='red', linestyle='--')
plt.axvline(x=percentile_95_time_in_system, color='green', linestyle='--', label='Percentil 95')
plt.show()
