import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 500

satellite_num = 8
satellites = []
lines = []
next_satellite = 0
start_time = 0
end_time = 0
total_time = 0

def make_satellites():
    global start_time
    for item in range(satellite_num):
        satellite = Actor("satellite")
        satellite.pos = (random.randint(40,WIDTH-40), random.randint(40,HEIGHT-40))
        satellites.append(satellite)
    start_time = time.time()

def draw():
    global total_time 
    screen.blit("galaxybg", (0,0))
    number = 1
    for item in satellites:
        screen.draw.text(str(number), (item.pos[0], item.pos[1]+20))
        item.draw()
        number += 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_satellite < satellite_num:
        total_time = time.time()-start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30, color=(255,255,255))
    else:
        screen,draw.text(str(round(total_time,1)), (10,10), fontsize=30, color=(255,255,255))

def update():
    pass

def on_mouse_down(pos):
    global next_satellite
    global lines
    global satellite_num
    global satellites

    if next_satellite < satellite_num:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
                next_satellite += 1
                print(lines)
            else:
                lines = []
                next_satellite = 0

make_satellites()
pgzrun.go()