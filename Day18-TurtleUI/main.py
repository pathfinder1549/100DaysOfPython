import colorgram
import turtle as t
import random as r


# extract colors
#colors = colorgram.extract('image.jpg', 6)
#colors_rbg = []
#for color_iter in colors:
#    #colors_rbg.append(color_iter.rgb)
#    r = color_iter.rgb.r
#    g = color_iter.rgb.g
#    b = color_iter.rgb.b
#    colors_rbg.append((r, g, b))
#
#print(colors_rbg)

color_list = [(31, 103, 156), (150, 23, 55), (220, 232, 237), (224, 159, 51)]

turt = t.Turtle()
scrn = t.Screen()
scrn.colormode(255)
turt.hideturtle()
turt.width(20)
turt.speed(0)
turt.penup()
origin_x = -225
origin_y = -225

for j in range(10):
    # y axis
    turt.sety(j*50 + origin_y)
    for i in range(10):
        # x axis        
        turt.setx(i*50 + origin_x)
        turt.dot(20,r.choice(color_list))

scrn.exitonclick()
