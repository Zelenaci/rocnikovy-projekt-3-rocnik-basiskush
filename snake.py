# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:18:36 2018

@author: Ten Nejlepší
"""

import turtle
from random import randint



#screen 
SCREEN = turtle.Screen()
SCREEN.title("Basiskush´s green snake")
SCREEN_size= 500
SCREEN.setup(SCREEN_size, SCREEN_size)
SCREEN.bgcolor("black")

#náhodná pozice
def randompozice():                                                    
    return (randint(-SCREEN_size//2, SCREEN_size//2), randint(-SCREEN_size//2, SCREEN_size//2))

#dobrota 
food = turtle.Turtle()
food.up()
food.shape("circle")
food.color("orange")
food.ht()
food_coor = randompozice()

#had
snake = turtle.Turtle()
snake.up()
snake.shape("square")
snake.color("green")
snake.ht()
snake_coor = [(0, 0)]
stamps = []

#šipky 
def nahoru(): smer(0, 1)
def dolu(): smer(0, -1)
def pravo(): smer(1, 0)     #x,y 
def levo(): smer(-1, 0)

    


def displej():
    stopky = SCREEN.tracer()
    SCREEN.tracer(0)
    food.clearstamps(1)
    snake.clearstamps(len(snake_coor))
    food.goto(food_coor[0], food_coor[1])
    food.stamp()
    for x, y in snake_coor:
        snake.goto(x, y)
        snake.stamp()
    SCREEN.tracer(stopky)
    
    
stop = False
def pozice():
    global snake_coor, food_coor, stop
    avance()
    if okno_naraz():
        stop = True
    if jidlo_ham():
        append()
        food_coor = randompozice() 


def smycka():
    if stop:
        return
    pozice()
    displej()
    SCREEN.ontimer(smycka, 40)
    

def jidlo_ham():
    sx, sy = snake_coor[0]
    fx, fy = food_coor
    distance = ((sx-fx)**2 + (sy-fy)**2)**.5
    return distance<20


def okno_naraz():
    x, y = snake_coor[0]
    return not (-SCREEN_size//2-5<x<SCREEN_size//2+5) or not (-SCREEN_size//2-5<y<SCREEN_size//2+5) 


dir_x = 0
dir_y = 0
def avance():
    global snake_coor
    x, y = snake_coor[0]
    x += dir_x*25
    y += dir_y*25
    snake_coor.insert(0, (x, y))
    snake_coor.pop(-1)


def append():
    global snake_coor
    a = snake_coor[-1][:]
    snake_coor.append(a)


def smer(x, y):
    global dir_x, dir_y
    dir_y = y
    dir_x = x
    
    
#směr > šipka press
SCREEN.onkeypress(nahoru, "Up")     
SCREEN.onkeypress(dolu, "Down")
SCREEN.onkeypress(pravo, "Right")
SCREEN.onkeypress(levo, "Left")
SCREEN.listen()


smycka()
turtle.mainloop()



