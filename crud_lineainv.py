#Hecho por: Pedro Hernández Figueroa 22270495

import mysql.connector

try:
    conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='19270904',
            database='practica05'
    )
    cursor = conexion.cursor()
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
    exit()

def crear_linea():
    nombre = input("Ingrese el nombre de la línea de investigación: ")
    try:
        sql = "INSERT INTO lineainv (nombre_linea) VALUES (%s)"
        cursor.execute(sql, (nombre,))
        conexion.commit()
        print("Línea de investigación creada con éxito.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")

def mostrar_lineas():
    try:
        cursor.execute("SELECT * FROM lineainv")
        lineas = cursor.fetchall()
        if not lineas:
            print("No hay líneas de investigación registradas.")
        else:
            for linea in lineas:
                print(f"ID: {linea[0]}, Nombre: {linea[1]}")
    except mysql.connector.Error as err:
        print(f"Error al recuperar datos: {err}")

def actualizar_linea():
    mostrar_lineas()
    id_linea = input("Ingrese el ID de la línea a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    try:
        sql = "UPDATE lineainv SET nombre_linea = %s WHERE clave_linea = %s"
        cursor.execute(sql, (nuevo_nombre, id_linea))
        conexion.commit()
        if cursor.rowcount > 0:
            print("Línea de investigación actualizada correctamente.")
        else:
            print("No se encontró la línea de investigación.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar datos: {err}")

def eliminar_linea():
    mostrar_lineas()
    id_linea = input("Ingrese el ID de la línea a eliminar: ")
    try:
        sql = "DELETE FROM lineainv WHERE clave_linea = %s"
        cursor.execute(sql, (id_linea,))
        conexion.commit()
        if cursor.rowcount > 0:
            print("Línea de investigación eliminada correctamente.")
        else:
            print("No se encontró la línea de investigación.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar datos: {err}")

while True:
    print("\n1. Crear línea de investigación")
    print("2. Mostrar líneas de investigación")
    print("3. Actualizar línea")
    print("4. Eliminar línea")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_linea()
    elif opcion == "2":
        mostrar_lineas()
    elif opcion == "3":
        actualizar_linea()
    elif opcion == "4":
        eliminar_linea()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")

cursor.close()
conexion.close()
