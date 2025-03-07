import mysql.connector

def conectar():
    return mysql.connector.connect(
            host='localhost',
            user='root',
            password='19270904',
            database='practica05'
    )

def crear_tipo_proyecto():
    conexion = conectar()
    cursor = conexion.cursor()
    nombre_tipo = input("Ingrese el nombre del tipo de proyecto: ")
    sql = "INSERT INTO tipoproyec (nombre_tipo) VALUES (%s)"
    try:
        cursor.execute(sql, (nombre_tipo,))
        conexion.commit()
        print("Tipo de proyecto agregado correctamente.")
    except mysql.connector.Error as err:
        print("Error al insertar:", err)
    finally:
        cursor.close()
        conexion.close()

def mostrar_tipos_proyecto():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM tipoproyec"
    try:
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}")
    except mysql.connector.Error as err:
        print("Error al recuperar datos:", err)
    finally:
        cursor.close()
        conexion.close()

def actualizar_tipo_proyecto():
    conexion = conectar()
    cursor = conexion.cursor()
    clave_tipo = input("Ingrese el ID del tipo de proyecto a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    sql = "UPDATE tipoproyec SET nombre_tipo = %s WHERE clave_tipo = %s"
    try:
        cursor.execute(sql, (nuevo_nombre, clave_tipo))
        conexion.commit()
        print("Tipo de proyecto actualizado correctamente.")
    except mysql.connector.Error as err:
        print("Error al actualizar:", err)
    finally:
        cursor.close()
        conexion.close()

def eliminar_tipo_proyecto():
    conexion = conectar()
    cursor = conexion.cursor()
    clave_tipo = input("Ingrese el ID del tipo de proyecto a eliminar: ")
    sql = "DELETE FROM tipoproyec WHERE clave_tipo = %s"
    try:
        cursor.execute(sql, (clave_tipo,))
        conexion.commit()
        print("Tipo de proyecto eliminado correctamente.")
    except mysql.connector.Error as err:
        print("Error al eliminar:", err)
    finally:
        cursor.close()
        conexion.close()

def menu():
    while True:
        print("\nGestión de Tipos de Proyecto")
        print("1. Crear Tipo de Proyecto")
        print("2. Mostrar Tipos de Proyecto")
        print("3. Actualizar Tipo de Proyecto")
        print("4. Eliminar Tipo de Proyecto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_tipo_proyecto()
        elif opcion == "2":
            mostrar_tipos_proyecto()
        elif opcion == "3":
            actualizar_tipo_proyecto()
        elif opcion == "4":
            eliminar_tipo_proyecto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
