import os

# Carpeta donde están los archivos
carpeta = ".\imagenes" 

# Verifica si la carpeta existe
if not os.path.exists(carpeta):
    print(f" La carpeta '{carpeta}' no existe. Verificá la ruta.")
    exit()

# Listar archivos de la carpeta
archivos = os.listdir(carpeta)

# Filtrar solo los archivos que terminan en .jpg ignorando mayúsculas
archivos_jpg = [f for f in archivos if f.lower().endswith(".jpg")]

# Verifica si la carpeta está vacía o no hay .jpg
if not archivos_jpg:
    print(f" La carpeta '{carpeta}' no contiene archivos .jpg para renombrar.")
    exit()

# Ordenar alfabéticamente
archivos_jpg.sort()

# Renombrar con contador
for i, archivo in enumerate(archivos_jpg, start=1):
    nuevo_nombre = f"foto_{i}.jpg"
    ruta_vieja = os.path.join(carpeta, archivo)
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)

    os.rename(ruta_vieja, ruta_nueva)
    print(f"Renombrado: {archivo} -> {nuevo_nombre}")

print("\n Archivos renombrados correctamente.")