from PIL import Image, ImageDraw
import math
import random

N = 200
HEIGHT = 3104 #<---------Image height in pixels
WIDTH = 4672  #<---------Image width in pixels
GOLDEN_RULE = 0.5*(1 + 5**0.5)
DISTANCE = 80
THETA_ODD = 0#math.pi/16 #<---------Inclination angle of the line segments
THETA_EVEN = -GOLDEN_RULE*THETA_ODD
LINE_WIDTH = 10

notOne = True
x_previous = WIDTH/2
y_previous = HEIGHT/2
x_next = 0
y_next = 0

def generateRandomRGBA():
    r = round(random.random() * 255)
    g = round(random.random() * 255)
    b = round(random.random() * 255)
    return (r, g, b, 255)

img = Image.new(mode="RGB", size=(WIDTH, HEIGHT), color=generateRandomRGBA())
draw = ImageDraw.Draw(img)
colour_even = generateRandomRGBA()
colour_odd = generateRandomRGBA()

for i in range(N):
    #print(i)
    next = i + 1
    
    x_previous = 0
    y_previous = i*HEIGHT/N
    x_next = 0
    y_next = 0
    notOne = True
    
    while notOne:
        if next % 2 != 0:
            next = 3 * next + 1
            x_next = x_previous + DISTANCE*math.cos(THETA_ODD)*random.random()
            y_next = y_previous + DISTANCE*math.sin(THETA_ODD)*random.random()
            draw.line((x_previous, y_previous, x_next, y_next), fill=colour_even, width = LINE_WIDTH)
        else:
            next = next / 2
            x_next = x_previous + DISTANCE*math.cos(THETA_EVEN)*random.random()
            y_next = y_previous + DISTANCE*math.sin(THETA_EVEN)*random.random()
            draw.line((x_previous, y_previous, x_next, y_next), fill=colour_odd, width = LINE_WIDTH)

        
        x_previous = x_next
        y_previous = y_next
        if next == 1:
            notOne = False
            #draw.ellipse([x_next, y_next,x_next+30, y_next+30], fill=(0, 255, 0, 255), width = 10)
    #print(i)

img.save("wallpapers/drawing_"+str(N)+"v_"+str(random.random())+".png")
