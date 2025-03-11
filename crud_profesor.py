#Hecho por: Pedro Hernández Figueroa 22270495

import mysql.connector

def conectar():
    return mysql.connector.connect(
            host='localhost',
            user='root',
            password='19270904',
            database='practica05'
    )

def crear_profesor(nombre_profesor):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO profesor (nombre_profesor) VALUES (%s)", (nombre_profesor,))
        conexion.commit()
        print(" Profesor agregado correctamente.")
    except mysql.connector.Error as e:
        print(" Error al insertar datos:", e)
    finally:
        cursor.close()
        conexion.close()

def mostrar_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM profesor")
        profesores = cursor.fetchall()
        print("\n Lista de Profesores:")
        for prof in profesores:
            print(f"ID: {prof[0]}, Nombre: {prof[1]}")
    except mysql.connector.Error as e:
        print(" Error al recuperar datos:", e)
    finally:
        cursor.close()
        conexion.close()

def actualizar_profesor(id_profesor, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("UPDATE profesor SET nombre_profesor=%s WHERE clave_profesor=%s",
                       (nuevo_nombre, id_profesor))
        conexion.commit()
        if cursor.rowcount > 0:
            print(" Profesor actualizado correctamente.")
        else:
            print(" No se encontró el profesor.")
    except mysql.connector.Error as e:
        print(" Error al actualizar datos:", e)
    finally:
        cursor.close()
        conexion.close()

def eliminar_profesor(id_profesor):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM profesor WHERE clave_profesor=%s", (id_profesor,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(" Profesor eliminado correctamente.")
        else:
            print(" No se encontró el profesor.")
    except mysql.connector.Error as e:
        print(" Error al eliminar datos:", e)
    finally:
        cursor.close()
        conexion.close()

def menu():
    while True:
        print("\n CRUD de Profesores")
        print("1. Agregar Profesor")
        print("2. Mostrar Profesores")
        print("3. Actualizar Profesor")
        print("4. Eliminar Profesor")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_profesor = input("Ingrese nombre del profesor: ")
            crear_profesor(nombre_profesor)
        elif opcion == "2":
            mostrar_profesores()
        elif opcion == "3":
            id_profesor = input("Ingrese ID del profesor a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            actualizar_profesor(id_profesor, nuevo_nombre)
        elif opcion == "4":
            id_profesor = input("Ingrese ID del profesor a eliminar: ")
            eliminar_profesor(id_profesor)
        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
