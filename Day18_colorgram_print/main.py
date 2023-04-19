###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random

screen = t.Screen()
timmy_the_turtle = t.Turtle()
# Extract 30 colors from an image.
colors = colorgram.extract('image.jpg', 30)
# print(type(colors))
first_color = []
rgb_colors = []
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
#
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# print(rgb)
for print_color in colors:
    # first_color.append(print_color.rgb)
    # #rgb = first_color.rgb # e.g. (255, 151, 210)
    # print(first_color)
    r = print_color.rgb.r
    g = print_color.rgb.g
    b = print_color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
    #print(type(new_color)) -> Tuple
print(rgb_colors)  # -> List




direction = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")
t.colormode(255)
x = -270
y = -180

def random_color():
    random_color = random.choice(rgb_colors)
    return random_color


def draw(times):
    for count in range(times):
        global x, y
        # x = random.randint(0,270)
        # y = random.randint(0,270)
        # direction_a = random.choice(direction)
        # timmy_the_turtle.forward(100)
        #timmy_the_turtle.penup()
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.dot(25)
        timmy_the_turtle.forward(30)
        x, y = timmy_the_turtle.pos()
        print(x, y)
        if x == 270 and y != 180:
            y += 30
            x = -270
            timmy_the_turtle.setpos(x, y)
        #elif x == 270 and y <= 180:

        # position = timmy_the_turtle.pos(-270, -180)
        # if position.y == (-270, 180)

        # current_heading = timmy_the_turtle.heading()
        # timmy_the_turtle.setheading(current_heading + 10)


# start drawing #######################################################
timmy_the_turtle.penup()
timmy_the_turtle.setpos(-270, -180) # x == -270, west; y == -180, south
for count in range(200):
    # line_colour = random.choice(colour)
    # timmy_the_turtle.color(line_colour)
    # timmy_the_turtle.color(random_color())
    # timmy_the_turtle.circle(50,50, 50)
    # timmy_the_turtle.dot()
    draw(count)
    if x < 270 and y == 180:
        break


screen.exitonclick()
