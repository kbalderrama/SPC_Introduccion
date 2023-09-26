import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
total_units = 256  # Cantidad total de unidades a producir
num_stations = 8   # Número de estaciones de trabajo
processing_times = [10, 15, 20, 15, 10, 15, 12, 18]  # Tiempos de procesamiento en cada estación
arrival_rate = 8# Tasa de llegada de unidades por hora

times_at_each_station = [[] for _ in range(num_stations)]
flag=False
# Simulación
def simulate_assembly_line(total_units, num_stations, mean_processing_times, arrival_rate):
    times_in_system = []
    global flag
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
            
            if flag==False:
                times_at_each_station[i].append(times_at_stations[i])
            
        exit_time = times_at_stations[-1]
        times_in_system.append(exit_time - arrival_time)
    flag=True
    return times_in_system

#simulación con 2000 repeticiones
avg_time_in_system = []
max_time_in_system = []
min_time_in_system = []
for _ in range(2000):
    simulation_results=simulate_assembly_line(total_units, num_stations, processing_times, arrival_rate)
    avg_time_in_system.append(np.mean(simulation_results))
    max_time_in_system.append(np.max(simulation_results)) 
    min_time_in_system.append(np.min(simulation_results))

promedio=np.mean(avg_time_in_system)
maximo=np.mean(max_time_in_system)
minimo=np.mean(min_time_in_system)

# Resultados
print(f"Tiempo promedio en el sistema: {promedio:.2f}")
print(f"Tiempo máximo en el sistema: {maximo:.2f}")
print(f"Tiempo mínimo en el sistema: {minimo:.2f}")

# Visualización de resultados
plt.hist(simulation_results, bins=20, edgecolor='blue')
plt.xlabel('Tiempo en el sistema')
plt.ylabel('Frecuencia')
plt.title('Distribución de Tiempos en el Sistema')
plt.show()

# Crear histogramas separados por estación de trabajo
plt.figure(figsize=(12, 8))
for i in range(num_stations):
    plt.subplot(2, 4, i + 1)  # 2 filas, 4 columnas
    plt.hist(times_at_each_station[i], bins=20, edgecolor='blue')
    plt.xlabel(f'Tiempo en Estación {i + 1}')
    plt.ylabel('Frecuencia')
    plt.title(f'Estación {i + 1}')
plt.tight_layout()
plt.show()



