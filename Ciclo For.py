# Crear el diccionario
vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino": "MDE",
    "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
}

# Imprimir los valores del diccionario
for key, value in vuelo.items():
    print(f"{key}: {value}")

# Imprimir los valores de tipo de maleta
print("Tipos de Maleta:")
for tipo in vuelo["Tipo_Maleta"]:
    print(tipo)
