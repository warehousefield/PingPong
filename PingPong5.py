
import turtle

window = turtle.Screen()
window.title("VICTOR")
window.setup(width=0.8, height=0.8)
# размер экрана в % от 100
window.bgcolor("white")
# цвет экрана (белый)
window.tracer(2)
# Скорость анимации. Что бы не дергалось изображение и не тормозили мячики

border = turtle.Turtle()
# граница стола
border.speed(0)
# изменение скорости отрисовки на более высокую
border.color("green")
# цвет стола
border.begin_fill()
# заполнение стола зеленым цветом от начала движения
border.goto(-500, 300)
# движение от центра (координаты 0,0) в лев верх угол х=-500,у=300
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()
# заполнение стола зеленым цветом до конца движения

border.goto(0, 300)
border.color("white")
border.goto(0, -300)
border.hideturtle()

# перемещаем рокетку влево по оси х, а команда пенап стирает след от перемещения


rocket_a = turtle.Turtle()
# создание рокетки
rocket_a.color("white")
# рокетка белого цвета
rocket_a.shape("square")
# придание рокетке формы квадрата
rocket_a.shapesize(stretch_wid=5, stretch_len=1)
# рокетка приняла нужную нам форму 5ед от центра по вертикали =50 пикселей и 1 ед от центра толщины=10 пикс
rocket_a.penup()
rocket_a.goto(-450, 0)
# перемещаем рокетку влево по оси х, а команда пенап стирает след от перемещения в виде линии

import keyword


def move_up():
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250
    rocket_a.sety(y + 8)


def move_down():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y - 8)
# движение вправо

# задаем движение рокетки по оси У при нажатии клавиш. У+5 и У-5 это скорость движения рокетки
# if это ограничение при которых рокетка не выходит за пределы поля
window.listen()
# команда окну для реагирования на события которые мы зададим ниже
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

# задание кнопок управления рокеткой W вверх с вниз.

# 1 мячик
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 1

# 2 мячик
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("white")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = 4
ball2.dy = 2

# 3 мячик
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("circle")
ball3.color("white")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = 4
ball3.dy = 1


while True:
    window.update()
    #      Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)

    ball3.setx(ball3.xcor() + ball3.dx)
    ball3.sety(ball3.ycor() + ball3.dy)

    # border checking(устанавливаем потолок для мячика)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # (устанавливаем пол для мячика)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    # (устанавливаем правую стенку для мячика)
    if ball.xcor() > 490 :
        ball.setx(490)
        ball.dx *= -1


    # (делаем левую границу для ведения счета)
    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1

    # Rocket and ball collision
    if ball.xcor() < -440 and (ball.ycor() > -450) and (
            ball.ycor() < rocket_a.ycor() + 50 and ball.ycor() > rocket_a.ycor() - 50):
        ball.setx(-440)
        ball.dx *= -1

# border checking(устанавливаем потолок для мячика)2

    if ball2.ycor() > 290:
        ball2.sety(290)
        ball2.dy *= -1
    # (устанавливаем пол для мячика)
    if ball2.ycor() < -290:
        ball2.sety(-290)
        ball2.dy *= -1
        # устанавливаем выступ

    # (устанавливаем правую стенку для мячика)
    if ball2.xcor() > 490 :
        ball2.setx(490)
        ball2.dx *= -1


    # (делаем левую границу для ведения счета)
    if ball2.xcor() < -490:
        ball2.goto(0, 0)
        ball2.dx *= -1

    # Rocket and ball collision
    if ball2.xcor() < -440 and (ball2.ycor() > -450) and (
            ball2.ycor() < rocket_a.ycor() + 50 and ball2.ycor() > rocket_a.ycor() - 50):
        ball2.setx(-440)
        ball2.dx *= -1

# border checking(устанавливаем потолок для мячика)3
    if ball3.ycor() > 290:
        ball3.sety(290)
        ball3.dy *= -1
    # (устанавливаем пол для мячика)
    if ball3.ycor() < -290:
        ball3.sety(-290)
        ball3.dy *= -1
        # устанавливаем выступ

    # (устанавливаем правую стенку для мячика)
    if ball3.xcor() > 490 :
        ball3.setx(490)
        ball3.dx *= -1


    # (делаем левую границу для ведения счета)
    if ball3.xcor() < -490:
        ball3.goto(0, 0)
        ball3.dx *= -1

    # Rocket and ball collision
    if ball3.xcor() < -440 and (ball2.ycor() > -450) and (
            ball3.ycor() < rocket_a.ycor() + 50 and ball2.ycor() > rocket_a.ycor() - 50):
        ball3.setx(-440)
        ball3.dx *= -1
