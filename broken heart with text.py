#left side of the heart



# Import turtle package
import turtle
  
# Creating a turtle object(pen)
pen = turtle.Turtle()
  
# Defining a method to draw curve
def curve():
    for i in range(200):
  
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)
  
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    pen.fillcolor('red')
  
    # Start filling the color
    pen.begin_fill()
  
    # Draw the left line
    pen.left(145)
    pen.forward(113)
  
    # Draw the left curve
    curve()
    pen.left(120)
    
    pen.goto(-35,100)
    
    pen.goto(0,0)
  
    # Ending the filling of the color
    pen.end_fill()

# Draw a heart
heart()
# To hide turtle8
pen.ht()




#right side of the heart




# Import turtle package
import turtle
  
# Creating a turtle object(pen)
pen = turtle.Turtle()
  
# Defining a method to draw curve
def curve():
    for i in range(200):
  
        # Defining step by step curve motion
        pen.left(1)
        pen.forward(1)
  
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    pen.fillcolor('red')
  
    # Start filling the color
    pen.begin_fill()
  
    # Draw the left line
    pen.left(35)
    pen.forward(113)
  
    # Draw the left curve
    curve()
    pen.left(120)
    
    pen.goto(-5,100)
    
    pen.goto(0,0)
  
    # Ending the filling of the color
    pen.end_fill()
  
# Draw a heart
heart()
# To hide turtle8
pen.ht()


#text 



def txt():
  
    # Move turtle to air
    pen.up()
  
    # Move turtle to a given position
    pen.setpos(-150,-80)
  
    # Move the turtle to the ground
    pen.down()
  
    # Set the text color to lightgreen
    pen.color('lightgreen')
  
    # Write the specified text in 
    # specified font style and size
    pen.write("I AM BROKEN", font=(
      "Verdana", 12, "bold"))
      
# Write text
txt()
# To hide turtle8
pen.ht()