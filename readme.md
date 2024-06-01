# Turtle Graphics Color Extraction

This project uses the `turtle` graphics module in Python to draw circles with colors extracted from an image using the `colorgram` library. The turtle draws circles in a grid pattern, changing colors based on the extracted colors from the provided image (`goku.jpg`).

## Features

- Extracts the top 10 colors from an image.
- Draws circles on the screen using the extracted colors.
- Displays a grid of colored circles using the Turtle graphics module.

## Prerequisites

- Python 3.x
- `turtle` module (comes with the standard Python library)
- `colorgram.py` library

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Install the `colorgram.py` library using pip:

    ```sh
    pip install colorgram.py
    ```

3. Clone this repository or download the code files.

4. Place your image (`goku.jpg`) in the same directory as your Python script.

## Usage

1. Run the Python script to start the Turtle graphics drawing:

    ```sh
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the name of your Python file.

2. The Turtle graphics window will open and start drawing circles in a grid pattern using the colors extracted from the `goku.jpg` image.

## Code Explanation

Here is a brief explanation of the original code:

```python
from turtle import Turtle, Screen
import colorgram
import time

# Set up the screen
screen = Screen()
screen.colormode(255)

# Create the turtle
t = Turtle()
t.pu()
goto_x = -400
goto_y = -400
t.goto(goto_x, goto_y)
t.pd()

# Extract colors from the image
colors = colorgram.extract("goku.jpg", 10)

# Draw circles with the extracted colors
while goto_y < 0:
    for q in colors:
        current_color = q.rgb
        t.color(current_color.r, current_color.g, current_color.b)
        t.fillcolor(current_color.r, current_color.g, current_color.b)

        t.begin_fill()
        t.circle(20)
        t.end_fill()
        time.sleep(1)  # Pause for 1 second between circles

        if goto_x < 0:
            goto_x += 50
        else:
            goto_y += 50
            goto_x = -400
        t.pu()
        t.goto(goto_x, goto_y)
        t.pd()

screen.exitonclick()
