millasPorHora = float(input("Por favor ingrese la cantidad de millas por hora, ingrese solo la cantidad numérica: "))
kilometrosPorHora = 1.61 * millasPorHora
metrosPorMinuto = (1609/60) * millasPorHora
print("La velocidad de", millasPorHora, "mi/h equivale a", kilometrosPorHora, "km/h y a", metrosPorMinuto, "m/min")