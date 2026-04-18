# CRUD (Simulacion en terminal) de registro de usuarios
def registrar_usuario(nombre, correo, contraseña):
    # Aquí podrías agregar lógica para validar los datos, como verificar el formato del correo
    # o la fortaleza de la contraseña. Por simplicidad, solo se muestra un mensaje de éxito.
    return f"Usuario '{nombre}' registrado con éxito."
# Ejemplo de uso
if __name__ == "__main__":
    nombre_usuario = input("Ingrese su nombre: ")
    correo_usuario = input("Ingrese su correo electrónico: ")
    contraseña_usuario = input("Ingrese su contraseña: ")
    resultado_registro = registrar_usuario(nombre_usuario, correo_usuario, contraseña_usuario)
    print(resultado_registro)
