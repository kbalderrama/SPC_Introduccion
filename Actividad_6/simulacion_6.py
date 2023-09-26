import numpy as np
import matplotlib.pyplot as plt

from simulation import simulate_assembly_line

# Parámetros del modelo
total_units = 256
num_stations = 8

# Variación de la tasa de llegada y los tiempos de procesamiento
arrival_rates = [4, 8, 12, 16, 20]  # Diferentes tasas de llegada
processing_time_variations = [
    [10, 15, 20, 15, 10, 15, 12, 18],  # Valores originales
    [15, 20, 25, 20, 15, 20, 18, 25],  # Aumento de los tiempos de procesamiento
    [5, 10, 15, 10, 5, 10, 8, 12],    # Reducción de los tiempos de procesamiento
]

# Almacenar resultados para cada combinación de tasas de llegada y tiempos de procesamiento
avg_times_in_system_matrix = np.zeros((len(arrival_rates), len(processing_time_variations)))

for i, arrival_rate in enumerate(arrival_rates):
    for j, processing_times_variation in enumerate(processing_time_variations):
        # Ejecución de la simulación para cada combinación
        simulation_results = simulate_assembly_line(total_units, num_stations, processing_times_variation, arrival_rate)
        
        # Cálculo del tiempo promedio en el sistema
        avg_time_in_system = np.mean(simulation_results)
        avg_times_in_system_matrix[i, j] = avg_time_in_system

# Visualización de resultados en un mapa de calor
plt.figure(figsize=(10, 6))
plt.imshow(avg_times_in_system_matrix, cmap='viridis', origin='lower')
plt.colorbar(label='Tiempo Promedio en el Sistema')
plt.xticks(np.arange(len(processing_time_variations)), ['Original', 'Aumento', 'Reducción'])
plt.yticks(np.arange(len(arrival_rates)), arrival_rates)
plt.xlabel('Variación de Tiempos de Procesamiento')
plt.ylabel('Tasa de Llegada (unidades por hora)')
plt.title('Impacto de la Tasa de Llegada y Variación de Tiempos de Procesamiento en el Tiempo Promedio en el Sistema')
plt.show()
