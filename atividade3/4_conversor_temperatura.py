print("=== Conversor de Temperatura ===")
print("Unidades disponíveis:")
print("1 - Celsius (C)")
print("2 - Fahrenheit (F)")
print("3 - Kelvin (K)")

temperatura = float(input("Digite a temperatura: "))
origem = int(input("Digite a unidade de origem (1-3): "))
destino = int(input("Digite a unidade de destino (1-3): "))

if origem == 1:
    celsius = temperatura
elif origem == 2:
    celsius = (temperatura - 32) * 5/9
elif origem == 3:
    celsius = temperatura - 273.15

if destino == 1:
    resultado = celsius
    unidade = "°C"
elif destino == 2:
    resultado = (celsius * 9/5) + 32
    unidade = "°F"
elif destino == 3:
    resultado = celsius + 273.15
    unidade = "K"

unidades = {1: "°C", 2: "°F", 3: "K"}
print(f"{temperatura}{unidades[origem]} = {resultado:.2f}{unidade}")
