from turtle import Turtle, Screen
import random

# List of colors for the turtles
colors = ["red", "green", "purple", "cyan", "coral", "blue"]

# List of y positions for the turtles
y_position = [-150, -90, -30, 30, 90, 150]

# Create the turtle graphics window
screen = Screen()

# Set the size of the window
screen.setup(width=600, height=600)

# Ask the user to make a bet on which color will win the race
user_bet = screen.textinput("Make your bet", "Which color will win the race? Choose a color: ")

# Create a list to store all the turtles
all_turtles = []

# Generate a random forward step for each turtle
forward_step = random.randint(0, 5)

# Flag to track whether the race has started or not
is_race_start = False

# If the user made a bet, start the race
if user_bet:
    is_race_start = True

# Create the turtles and add them to the list
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-270, y=y_position[i])
    new_turtle.forward(forward_step)
    all_turtles.append(new_turtle)

# Keep moving the turtles until one of them crosses the finish line
while is_race_start:
    for turtle in all_turtles:
        # If a turtle crosses the finish line, end the race
        if turtle.xcor() > 280:
            clr = turtle.pencolor()
            # Check if the user won or lost the bet
            if clr == user_bet:
                print(f"You won the bet! The {clr} turtle wins the race.")
            else:
                print(f"You lost the bet! The {clr} turtle wins the race.")
            is_race_start = False

        # Generate a random forward step for the turtle
        forward_step = random.randint(0, 10)
        turtle.forward(forward_step)

# Close the turtle graphics window
screen.bye()
