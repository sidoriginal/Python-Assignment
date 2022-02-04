from curses import COLOR_BLACK, COLOR_CYAN
from turtle import *
from _curses import COLOR_BLACK, COLOR_CYAN
speed(10)
color(COLOR_CYAN)
bgcolor(COLOR_BLACK)
b=200
while b>0:
    left(b)
    forward(b*3)
    b=b-1