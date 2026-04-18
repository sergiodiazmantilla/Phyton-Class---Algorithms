# CRUD de registro de usuarios con almacenamiento en una base de datos SQLite
import sqlite3

def crear_base_datos():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def registrar_usuario(id, nombre, correo, contraseña):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO usuarios (id, nombre, correo, contraseña)
            VALUES (?, ?, ?, ?)
        ''', (id, nombre, correo, contraseña))
        conn.commit()
        return f"Usuario '{nombre}' registrado con éxito."
    except sqlite3.IntegrityError:
        return "Error: El correo electrónico ya está registrado."
    finally:
        conn.close()
# Ejemplo de uso para registrar un usuario
if __name__ == "__main__":
    crear_base_datos()

    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Eliminar usuario")
        print("4. Actualizar contraseña")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            # ID AUTOMÁTICO, no se solicita al usuario
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute('SELECT MAX(id) FROM usuarios')
            max_id = cursor.fetchone()[0]
            id_usuario = max_id + 1 if max_id is not None else 1
            cursor.close()
            conn.close()
            nombre_usuario = input("Ingrese su nombre: ")
            correo_usuario = input("Ingrese su correo electrónico: ")
            contraseña_usuario = input("Ingrese su contraseña: ")
            resultado_registro = registrar_usuario(id_usuario, nombre_usuario, correo_usuario, contraseña_usuario)
            print(resultado_registro)
        elif opcion == "2":
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute('SELECT id, nombre, correo FROM usuarios')
            usuarios = cursor.fetchall()
            print("\nUsuarios registrados:")
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}")
            cursor.close()
            conn.close()
        elif opcion == "3":
            id_usuario = input("Ingrese el ID del usuario a eliminar: ")
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Usuario eliminado con éxito.")
            else:
                print("Error: Usuario no encontrado.")
            cursor.close()
            conn.close()
        elif opcion == "4":
            id_usuario = input("Ingrese el ID del usuario para actualizar la contraseña: ")
            nueva_contraseña = input("Ingrese la nueva contraseña: ")
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE usuarios SET contraseña = ? WHERE id = ?', (nueva_contraseña, id_usuario))
            conn.commit()
            if cursor.rowcount > 0:
                print("Contraseña actualizada con éxito.")
            else:
                print("Error: Usuario no encontrado.")
            cursor.close()
            conn.close()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    crear_base_datos()
