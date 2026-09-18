yo = {
    "nombre": "hernan",
    "edad": 18,
    "es_estudiante": True
}

yo_lista = ["nombre", 18, True]
print(yo_lista[0])
print(yo["nombre"])

#modificar un elemento
yo_lista[0] = "Hernan Tamara"
print(yo_lista)
yo["nombre"] = "Arath Estrada"
print(yo)

yo_lista.append("calle 27 #12-34")
yo_lista.append(3175341899)
yo["Telefono"] = 3175341899
yo["Dirrecion"] = "Calle 27 # 12-34"
print(yo)

#Update
yo_2 = {"rh": "O+", "Profesion": "Cientifico de datos"}
yo.update(yo_2)
print(yo)

eliminado = yo.popitem()
eliminado_2 = yo.pop("rh")
print(eliminado)
print(yo)