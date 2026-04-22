#Crear imagen con PIL
from PIL import Image
#Crear una imagen en blanco de 200x200 píxeles
imagen_blanca = Image.new('RGB', (200, 200), color='white')
#Guardar la imagen
imagen_blanca.save('IMG\\imagen_blanca.png')
#Crear una imagen con un fondo rojo
imagen_roja = Image.new('RGB', (200, 200), color='red')
#Guardar la imagen roja
imagen_roja.save('IMG\\imagen_roja.png')
#Crear una imagen con un fondo azul
imagen_azul = Image.new('RGB', (200, 200), color='blue')
#Guardar la imagen azul
imagen_azul.save('IMG\\imagen_azul.png')
#Crear una imagen con un fondo verde
imagen_verde = Image.new('RGB', (200, 200), color='green')
#Guardar la imagen verde
imagen_verde.save('IMG\\imagen_verde.png')
