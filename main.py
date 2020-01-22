import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue']:
    t.color(c)
    t.forward(75)
    t.left(90)

print ("hello world!")
for i in range (10): 
  t.forward(5)