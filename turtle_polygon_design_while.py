# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Turtle Graphics — Polygon Design (WHILE Loop)
# DATE WRITTEN: 9/30/2020
# UPDATED:      2026 — fixed typos "PURPPOSE" → "PURPOSE" and "END PROGRSM"
#                      → "END PROGRAM", renamed howMany → how_many, added
#                      turtle.done() to keep window open, renamed from
#                      "Square" to "Polygon" (shape only closes at 8 sides
#                      since each turn is fixed at 45°)
#
# PURPOSE: Use Python's turtle graphics module to draw a customizable yellow
#          filled polygon on a light gray canvas using a WHILE loop.
#          The user enters the number of sides at runtime.
#
# NOTE ON SHAPE: The turtle turns 45° per side. The shape fully closes
#          only when 8 sides are entered (8 × 45° = 360°). Entering fewer
#          sides produces an open/partial shape.
#
# KEY CONCEPT — WHILE LOOP:
#   The loop control variable (count) starts at 1 and increments each
#   iteration until it exceeds how_many. Each iteration draws one side.
#
# Compare to:
#   turtle-stop-sign-while-loop (adds STOP text and pole)
#   A4-FOR-Loop-Design (same shape concept using FOR loop)

import turtle  # Import the turtle graphics module

# ============================================================
# Configure the drawing canvas and turtle settings

turtle.bgcolor("light gray")    # Set background color of the canvas
turtle.shape("square")          # Set turtle cursor shape
turtle.pensize(3)               # Set pen width in pixels
turtle.pencolor("red")          # Set outline/pen color

# ============================================================
# Input Operation — ask user how many sides the shape should have

how_many = int(input("Enter the number of sides for the design (enter 8 for a closed octagon):\n"))

# ============================================================
# Begin filling the shape with yellow color

turtle.fillcolor("yellow")  # Define color to fill the shape
turtle.begin_fill()         # Begin filling the shape

# ============================================================
# WHILE LOOP — draw the shape one side at a time

count = 1                       # Initialize the loop control variable

while count <= how_many:        # Continue looping while count has not exceeded how_many
    turtle.forward(100)         # Draw one side of the shape (100 pixels)
    turtle.left(45)             # Turn left 45 degrees to draw the next side
    count = count + 1           # Update the loop control variable (increment by 1)
    # END WHILE LOOP

turtle.end_fill()               # End filling the shape once all sides are drawn
turtle.hideturtle()             # Hide the turtle cursor when drawing is complete
turtle.done()                   # Keep the window open until the user closes it

# END PROGRAM
