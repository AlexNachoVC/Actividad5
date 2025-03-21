from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ!#$%&")*2 #Se cambian los elementos por letras y símbolos
state = {'mark': None, 'taps': 0}  # Agregar contador de taps
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    # Aumentar contador de taps
    state['taps'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    
    # Dibuja la imagen de fondo
    goto(0, 0)
    shape(car)
    stamp()

    # Dibuja las casillas ocultas
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # Dibuja el número en la casilla seleccionada y lo centra dentro de esta
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align = "center")

    # Mostrar número de taps (Dibujarlo después de las casillas para que quede al frente)
    up()
    goto(-190, 180)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 16, 'bold'))

    # Verificar si el juego ha terminado
    if all(not hidden for hidden in hide):
        goto(-50, 0)
        color('red')
        write('¡Ganaste!', font=('Arial', 30, 'bold'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
 
