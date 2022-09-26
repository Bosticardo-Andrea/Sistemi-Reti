import turtle 
snow = turtle.Turtle()
sfondo = turtle.Screen()
snow.hideturtle()
sfondo.bgcolor("light blue") 
snow.color("white")
snow.speed(0)

f = open("./codice.txt","r")
righe = f.readlines()
for riga in righe:
    s = riga.split(":") 
    if(s[0] == "forward"):
        snow.forward(float(s[-1]))
    elif(s[0] == "right"):
        snow.right(float(s[-1])) 
    #print(s[-1])
    #print(s[0])
sfondo.exitonclick()
f.close()