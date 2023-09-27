import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
total_units = 256  # Cantidad total de unidades a producir
num_stations = 10 # Número de estaciones de trabajo
processing_times = [8, 12, 10, 12, 8, 10, 9, 13, 8, 10 ]    # Tiempos de procesamiento en cada estación
arrival_rate = 8# Tasa de llegada de unidades por hora


# Resto del código (simulación y análisis de resultados):

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

# Resto del código (análisis de resultados y visualización)...
# ...
# Análisis de resultados
avg_time_in_system = np.mean(simulation_results)
max_time_in_system = np.max(simulation_results)
min_time_in_system = np.min(simulation_results)

# Visualización de resultados
plt.hist(simulation_results, bins=20, edgecolor='black')
plt.xlabel('Tiempo en el sistema')
plt.ylabel('Frecuencia')
plt.title('Distribución de Tiempos en el Sistema')
plt.show()


# Imprimir resultados
print("Resultados de la simulación con la nueva tasa de llegada:")
print(f"Tiempo promedio en el sistema: {np.mean(simulation_results):.2f}")
print(f"Tiempo máximo en el sistema: {np.max(simulation_results):.2f}")
print(f"Tiempo mínimo en el sistema: {np.min(simulation_results):.2f}")
