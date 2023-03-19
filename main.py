import turtle

def draw_petal(t, r, angle):
    for i in range(2):
        t.circle(r, angle)
        t.left(180-angle)

def draw_flower(t, n, r, angle):
    for i in range(n):
        draw_petal(t, r, angle)
        t.left(360/n)

def draw_stem(t, length):
    t.right(90)
    t.forward(length)

def draw_flower_with_stem():
    t = turtle.Turtle()
    t.speed(0)
    draw_flower(t, 7, 100, 60)
    draw_stem(t, 200)
    turtle.done()

draw_flower_with_stem()
