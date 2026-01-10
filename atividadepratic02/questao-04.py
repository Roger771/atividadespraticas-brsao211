distancia_percorrida = float(input("Digite a distânci percorrida em km: "))
combustivel_gasto = float(input("Digite o combustivel gasto em litros: "))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"consumo médio: {consumo_medio:.2f} km/l")
print(f"Distância: {distancia_percorrida}")
print(f"Combustivel gasto: {combustivel_gasto} L")