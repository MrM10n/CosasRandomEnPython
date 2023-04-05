import random

nombres_masculinos = ["Juan", "Pedro", "Pablo", "Luis", "Diego", "Andrés", "Santiago", "Mateo", "Carlos", "Javier", "Hugo", "Leonardo", "Gabriel", "Felipe", "Rafael", "Bruno", "Jorge", "David", "Mario", "Manuel", "Alex", "Samuel", "Chris", "Jamie"]
nombres_femeninos = ["Ana", "María", "Luisa", "Laura", "Paula", "Sara", "Juliana", "Isabella", "Camila", "Carolina", "Mariana", "Valentina", "Antonia", "Lucía", "Gabriela", "Daniela", "Florencia", "Elena", "Clara", "Catalina", "Jordan", "Taylor", "Avery", "Casey"]
nombres_neutros = ["Alexis", "Charlie", "Robin", "Reese", "Jamie", "Avery", "Jordan", "Taylor", "Morgan", "Hayden", "Cameron", "Casey", "Riley", "Quinn", "Parker", "Harper"]
apellidos = ["González", "Rodríguez", "Gómez", "Fernández", "Pérez", "López", "García", "Martínez", "Sánchez", "Díaz", "Álvarez", "Romero", "Torres", "Ruiz", "Gutiérrez", "Ramírez", "Sosa", "Vega", "Flores", "González"]

def generar_nombre(genero):
    if genero == "masculino":
        nombre1 = random.choice(nombres_masculinos)
    elif genero == "femenino":
        nombre1 = random.choice(nombres_femeninos)
    else:
        nombre1 = random.choice(nombres_neutros)
    nombre2 = random.choice(nombres_neutros)
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)
    nombre_completo = nombre1 + " " + nombre2 + " " + apellido1 + " " + apellido2
    return nombre_completo

genero_elegido = input("¿Qué género quieres que tenga el nombre? (masculino, femenino o neutro): ")
nombre_generado = generar_nombre(genero_elegido)
print("El nombre generado es:", nombre_generado)