import turtle 
def lastra():
    snow.right(45)
    f.write("right:" + str(45) + "\n")
    snow.forward(50)
    f.write("forward:" + str(50) + "\n")
    snow.forward(-50)
    f.write("forward:" + str(-50) + "\n")
    snow.right(-90)
    f.write("right:" + str(-90) + "\n")
    snow.forward(50)
    f.write("forward:" + str(50) + "\n")
    snow.forward(-50)
    f.write("forward:" + str(-50) + "\n")
    snow.right(45)
    f.write("right:" + str(45) + "\n")
def fiocco():
    for _ in range (8):
        snow.right(45)
        f.write("right:" + str(45) + "\n")
        snow.forward(150)
        f.write("forward:" + str(150) + "\n")
        snow.forward(-50)
        f.write("forward:" + str(-50) + "\n")
        lastra()
        snow.forward(-100)
        f.write("forward:" + str(-100) + "\n")


f = open("./codice.txt","w")
snow = turtle.Turtle()
sfondo = turtle.Screen()
snow.hideturtle()
sfondo.bgcolor("light blue") 
snow.color("white")
snow.speed(0)
fiocco()
sfondo.exitonclick()
f.close()