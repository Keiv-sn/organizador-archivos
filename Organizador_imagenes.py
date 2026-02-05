
from shutil import move
from pathlib import Path
from datetime import datetime


# Define la carpeta de origen donde están los archivos (Screenshots del usuario)
carpeta_origen = Path.home() / "Pictures" / "Screenshots"

# Define la carpeta base de destino donde se crearán subcarpetas por fecha
carpeta_destino = Path.home() / "Pictures" / "Carpeta Fecha"

# Define la ruta del archivo de log donde se registrarán los movimientos
archivo_log = Path.home() / "Pictures" / "registro_movimientos.txt"

# Abre el archivo de log en modo "append" (agregar al final) usando codificación UTF-8
with open(archivo_log, "a", encoding="utf-8") as registro:

    # Recorre todos los elementos dentro de la carpeta de origen
    for archivo in carpeta_origen.iterdir():

        # Verifica que el elemento sea un archivo y no una carpeta
        if archivo.is_file():
            try:
                # Obtiene la fecha de última modificación del archivo en formato timestamp
                archivo_fecha = archivo.stat().st_mtime

                # Muestra en consola la fecha de modificación y el nombre del archivo
                print(f"Fecha de modificación: {archivo_fecha} - Archivo: {archivo.name}")

                # Convierte el timestamp a un objeto datetime
                fecha = datetime.fromtimestamp(archivo_fecha)

                # Formatea la fecha en formato "YYYY-MM" (ejemplo: 2025-01)
                carpeta = fecha.strftime("%Y-%m")

                # Construye la ruta completa de la carpeta destino según el mes
                destino = carpeta_destino / carpeta

                # Muestra en consola la carpeta que se va a crear (si no existe)
                print(f"Creando carpeta: {destino}")

                # Crea la carpeta destino, incluyendo carpetas padre si no existen
                # exist_ok=True evita errores si la carpeta ya existe
                destino.mkdir(parents=True, exist_ok=True)

                # Define la ruta final del archivo dentro de la carpeta destino
                destino_archivo = destino / archivo.name

                # Muestra en consola el movimiento del archivo
                print(f"Mover archivo {archivo} a {destino_archivo}")

                # Mueve el archivo desde la carpeta origen a la carpeta destino
                move(str(archivo), str(destino_archivo))

                # Obtiene la fecha y hora actual para el registro del log
                hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M")

                # Escribe en el archivo de log el movimiento realizado
                registro.write(f"[{hora_actual}] movido {archivo.name} a {destino.name}/\n")

            # Captura cualquier error que ocurra durante el proceso
            except Exception as e:

                # Obtiene la fecha y hora actual cuando ocurre el error
                hora_error = datetime.now().strftime("%Y-%m-%d %H:%M")

                # Registra en el log que ocurrió un error al mover el archivo
                registro.write(f"[{hora_error}] ERROR al mover {archivo.name} al destino {destino.name}/\n")
                

