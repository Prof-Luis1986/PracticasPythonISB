import turtle
import time
import random

posponer = 0.1

Score = 0

# Configuración de la pantalla
WN = turtle.Screen()
WN.title("Juego de Snake")
WN.bgcolor("black")
WN.setup(width=600, height=600)
WN.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("#0A3E05")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Funciones
def arriba(): 
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo(): 
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def color_aleatorio():
    colores = ["red", "blue", "green", "yellow", "purple", "orange"]
    return random.choice(colores)

# Asignación de teclas
WN.listen()
WN.onkeypress(arriba, "Up")
WN.onkeypress(abajo, "Down")
WN.onkeypress(izquierda, "Left")
WN.onkeypress(derecha, "Right")

# Bucle principal del juego
try:
    while True:
        WN.update()

        # Verificar colisión con los bordes
        if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for segmento in segmentos:
                segmento.goto(1000, 1000)

            segmentos.clear()

            # Restablecer el puntaje y colores
            Score = 0
            cabeza.color("#0A3E05")
            comida.color("red")
            texto.clear()
            texto.write("Score: 0", align="center", font=("Courier", 24, "normal"))

        # Verificar colisión con la comida
        if cabeza.distance(comida) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            comida.goto(x, y)

            # Añadir un segmento
            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            nuevo_segmento.color(cabeza.color()[0])
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)

            # Incrementar el puntaje
            Score += 10
            texto.clear()
            texto.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal"))

            # Cambiar colores cada 100 puntos
            if Score % 100 == 0:
                nuevo_color = color_aleatorio()
                cabeza.color(nuevo_color)
                comida.color(nuevo_color)
                for segmento in segmentos:
                    segmento.color(nuevo_color)

        # Mover los segmentos finales primero en orden inverso
        totalSeg = len(segmentos)
        for index in range(totalSeg - 1, 0, -1):
            x = segmentos[index - 1].xcor()
            y = segmentos[index - 1].ycor()
            segmentos[index].goto(x, y)

        # Mover el segmento 0 a donde está la cabeza
        if totalSeg > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            segmentos[0].goto(x, y)

        mov()
        time.sleep(posponer)

except turtle.Terminator:
    print("El juego se ha cerrado inesperadamente.")

