import turtle

# Configuración de la ventana y el lápiz
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
window.bgcolor("light blue")

# Dibujar el sol
pen.penup()
pen.goto(-200, 200)
pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Dibujar las montañas
pen.penup()
pen.goto(-400, -100)
pen.pendown()
pen.color("gray")
pen.begin_fill()
pen.goto(-200, 100)
pen.goto(0, -50)
pen.goto(200, 50)
pen.goto(400, -100)
pen.goto(-400, -100)
pen.end_fill()

# Dibujar las nubes
pen.penup()
pen.goto(-200, 100)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(40)
pen.end_fill()
pen.penup()
pen.goto(-150, 150)
pen.pendown()
pen.begin_fill()
pen.circle(40)
pen.end_fill()
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# Dibujar el agua
pen.penup()
pen.goto(-400, -100)
pen.pendown()
pen.color("blue")
pen.begin_fill()
pen.goto(-200, -200)
pen.goto(0, -150)
pen.goto(200, -200)
pen.goto(400, -100)
pen.goto(-400, -100)
pen.end_fill()

# Mostrar el dibujo
turtle.done()
