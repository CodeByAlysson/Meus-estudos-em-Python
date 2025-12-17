#Vamos aprender a desenhar um círculo colorido usando a biblioteca turtle em Python.

import turtle as t
t.bgcolor("black")
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(360):
    t.pencolor(colors[i % len(colors)])
    t.circle(i, 60)
    t.left(25)
t.done()

# fim do código