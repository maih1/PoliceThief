import turtle as t
import time
from typing import Counter
import math

wn = t.Screen()
wn.title('Police and Thief ')
wn.addshape('t1.gif') 
wn.addshape('11.gif') 

def drawRectangle(x, y, width, hight, color):
    sq = t.Turtle()
    sq.penup()
    sq.goto(x, y)
    sq.color(color)
    sq.pendown()

    for i in range(4):
        if i%2 == 0:
            sq.forward(hight)
            sq.left(90)
        else:
            sq.forward(width)
            sq.left(90) 

    sq.hideturtle()

    return sq

def square(hor):
    t.forward(hor)
    t.left(90)
    t.forward(hor)
    t.left(90)

def write(i):
    
    style = ('Courier', 30, 'italic')
    t.write(i, font=style)

def rectangle(hor, col):
    t.pendown() #tạo con trỏ
    t.pensize(1)
    t.color(col)

    for counter in range(1,3):
        square(hor)
         
    t.penup()

def drawImg(x, y, a):
    myImage  = t.Turtle()
    myImage.speed(10) #so it will draw the image instantly
    myImage.shape(a) #give your object the image
    myImage.penup() #if you dont do this, it will draw a line
    myImage.goto(x, y) #give your image a location

    return myImage

def drawPolice(hor, count, i):
    rectangle(hor,'red')    
    write(i + 1)
    p=drawImg(count + 50, 250, '11.gif')

def drawThief(hor, count, i):
    rectangle(hor,'blue')
    write(i + 1)
    drawImg(count + 50, 250, 't1.gif')

def drawInput(array, hor):
    count = -350

    for i in range(0, len(array)):
        t.setx(count)
        count += 5
        if array[i] == 'P':
            drawPolice(hor, count, i)
            
        elif array[i] == 'T':
            drawThief(hor, count, i)

        count += hor  
        t.hideturtle() 

def move(offset_x, offset_y):

    canvas = t.getcanvas() # `turtle`, not `t`
    for element_id in canvas.find_all():
        canvas.move(element_id, offset_x, offset_y)


def drawPolice2(array):
    t.penup()
    count = 200
    t.setx(-300)
    _po = []
    _qu = []
    _wr = []

    for i in range(len(array)):
        t.sety(count)
        count -= 10
        rectangle(100,'red')    
        write(array[i] + 1)
        p = drawImg(-250, count + 50, '11.gif')
        count -= 100  
        
        _po.append(p)
    
    t.hideturtle()

    return _po
    
def drawThief2(array):
    t.penup()
    count = 200
    t.setx(-100)
    th = []

    for i in range(len(array)):
        t.sety(count)
        count -= 10
        rectangle(100,'blue')
        write(array[i] + 1)
        thi = drawImg(-50, count + 50 , 't1.gif')
        count -= 100 

        th.append(thi)

    t.hideturtle()

    return th

def drawRunRes(po, th, l , r):
    _po = po[r].position()
    _th = th[l].position()
    check = _th[0] - _po[0]
    po[r].speed(1)
    th[l].speed(1)
    po[r].forward(check)
    th[l].forward(20)

def drawRunGo(po, th, l, r):
    po[r].speed(1)
    th[l].speed(1)
    po[r].forward(100)
    th[l].forward(100)


def getPosition(array):
    pos = []
    for i in array:
        pos.append(i.position())
    return pos

def drawRunRes2(po, th, l , r, res, drawRes, count):
    _posRes = drawRes.position()
    _posTh = th[l].position()
    _check = int(abs(_posRes[1] - _posTh[1]))
    
    check = (_check // 20) - 2

    dk = drawAngle(po, th, l, r)
    _angle = angle(dk[0], dk[1])

    po[r].setheading(_angle)

    po[r].speed(1)
    th[l].speed(1)
    po[r].forward(math.hypot(dk[0], dk[1]))
    th[l].forward(20)
    
    po[r].speed(10)
    th[l].speed(10)
    i = 0
    while i < check:
        drawResult(res, po, r, drawRes, count)
        drawResult(res, th, l, drawRes, count)
        t.update()

        _posTh = th[l].position()
        if(_posTh[1] <= _posRes[1] - 10):
            i = check
        else:
            i += 1

    th[l].forward(count)

def drawRunGo2(po, th, l, r):
    dk = drawAngle(po, th, l, r)
    _angle = angle(dk[0], dk[1])
    po[r].setheading(_angle)
    po[r].speed(1)
    th[l].speed(1)
    po[r].forward(100)
    th[l].forward(100)

def drawResult(res, th, l, drawRes, count):
    _posRes = drawRes.position()
    _posTh = th[l].position()
    k = round(abs(_posRes[1] - _posTh[1]), 1)
    d = round(abs(_posRes[0] - _posTh[0]), 1)
    _angle = angle(d, k)
    goc = 90 - _angle
    th[l].setheading(360 - goc + 5 )
    th[l].speed(10)
    th[l].forward(20)
    th[l].setheading(0)

def drawNumRes(x, y, color, res):
    wr = t.Turtle()
    wr.hideturtle()
    wr.penup()
    wr.goto(x, y)
    wr.color(color)
    style = ('Courier', 30, 'italic')
    wr.write(res, font=style)

def drawAngle(po, th, l, r): 
    _po = po[r].position()
    _th = th[l].position()

    d = _th[1] - _po[1]
    k = _th[0] - _po[0]
    
    return d, k

def angle(d, k):
    _angle = math.degrees(math.atan(d/k))
    return int(_angle)

def rundraw(array):
    t.hideturtle()
    t.penup()
    t.speed('slow')

    t.goto(-350, 200)

    drawInput(array, 100)