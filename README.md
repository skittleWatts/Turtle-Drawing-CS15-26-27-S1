# Activity 2: Trying out Turtle

In this activity, we will explore our first built-in library: Turtle! Turtle allows you to create a visual output for your program.

When you have completed the tutorial portion, be sure to also complete the [Extension Activity](#extension-activity-turtle-drawing)!


## 1. Create a Root Folder

Whenever you are creating a new Python project, it is best to stay organized by placing all the files related to the project in the same folder. Create a folder named `root`.

Inside the folder, create a new `main.py` file.

## 2. A Brief Overview of Turtle and Importing the Library

Turtle is a library that allows you to draw using a turtle! It isn't a literal turtle, but it is a shape on the screen that can draw.

Turtle works by giving the program instructions in a sequence. You can program the turtle to move forwards or backwards, or rotate left or right. You can also program the turtle to start or stop drawing.

Below is a brief outline of some common Turtle commands. If you want to extend your understanding of the Turtle library, the full documentation can be found here: [Turtle Documentation](https://docs.python.org/3/library/turtle.html)

|    Command     | Shorthand | Effect                                                                             |
|:--------------:|:---------:|------------------------------------------------------------------------------------|
| `forward(50)`  | `fd(50)`  | Move the turtle forward by 50 pixels.                                              |
| `backward(50)` | `bk(50)`  | Move the turtle backwards by 50 pixels.                                            |
|   `left(90)`   | `lt(90)`  | Rotate the turtle left (counter-clockwise) 90 degrees.                             |
|  `right(90)`   | `rt(90)`  | Rotate the turtle right (clockwise) 90 degrees.                                    |
|   `penup()`    |  `up()`   | Lift the "pen" and stop drawing.                                                   |
|  `pendown()`   | `down()`  | Lower the pen and start drawing.                                                   |
|   `reset()`    |    n/a    | Clear the screen, reset all values, return the turtle to the center of the screen. |
|   `clear()`    |    n/a    | Delete the drawing, but leave everything else as is.                               |
|    `done()`    |    n/a    | Keeps the window open at the end of the program.                                   |

To get started with turtle, we need to import the turtle library into our program:

```python
import turtle
```

When importing a module, we need to access its namespace.

| Namespace                                                                                                                                               |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| *A namespace is a collection of names and their associated values that helps Python determine which variable, function, or object is being referenced.* |

This would mean that for every single command, we would need to write `turtle` in front of it like this:

```python
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
```

As you can see, that would become very tedious. To simplify our namespace, we have two main options:

### Option 1: Import the Entire Namespace

This option is helpful if you are only working with a single library and plan on using it a lot. If you import the entire namespace, you don't need to write anything in front of the functions from that library. However, there is a risk of accidentally overwriting the libraries functions and objects, so this method should be used with caution!

```python
from turtle import *
```

To access turtle now our code would look like this:

```python
forward(50)
left(90)
forward(50)
right(90)
forward(50)
```

### Option 2: Importing Using an Alias

It's best practice when working with multiple libraries to import them with a namespace still, as it makes it clearer what code is coming from what library. It also prevents you from accidentally overwriting any functions or objects that library uses. This shorter namespace is called an alias.

| Alias                                                                                                 |
|:------------------------------------------------------------------------------------------------------|
| *An alias is an alternative name used to refer to an existing variable, function, object, or module.* |

We can give turtle an alias of `t` like this:

```python
import turtle as t
```

Our code is still shorter, but we don't run the risk of overlapping with other namespaces:

```python
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
```

---

For this activity, we are only using the turtle library, so we will import everything:

```python
from turtle import *
```

## 3. Creating a Line

With turtle imported, we can start by drawing a line!

```python
forward(100)
```

Run the code and see what happens!

You might notice that the window closed rather abruptly. To prevent this, we will add `done()` to the end of our program, which tells Python to leave the window open until we are finished.

```python
done()
```

You'll notice that the turtle starts in the center of the screen, then walks forward drawing a line for 100 pixels!

You might not like the color that the line is, so change it to your favourite color (mine is orange) with this code:

```python
color("orange")
```

Run the project again and see what happens.

If nothing changed, think about where you changed the color in the sequence. 

Was your sequence like this?

| Step | Instruction           |
|:----:|-----------------------|
|  1   | Import turtle.        |
|  2   | Draw the line.        |
|  3   | Change the color.     |
|  4   | Keep the window open. |

Or was this your sequence?

| Step | Instruction           |
|:----:|-----------------------|
|  1   | Import turtle.        |
|  2   | Change the color.     |
|  3   | Draw the line.        |
|  4   | Keep the window open. |

If you draw the line before you change the color, will the color of the line be the new color?

Either way, ensure your sequence works before moving on to the next step. Your line should be the color you want!

## 4. Creating a Square

Now that we have a line, let's make it a square. For each line of the square, make it a different color so that all 4 sides are different colors.

You'll also need to turn the turtle with either left or right before moving it on each line.

```python
color("red")
left(90)
forward(100)
```

Add the rest of the code you need to draw a square!

## 5. Writing "Hello"

With a multicolor square under your belt, it's time for something a little more challenging, we're going to write a word with the turtle. 

First of all, we need to rest after the square that we have:

```python
reset()
```

This will clear the screen and put our turtle back to where it started.

For writing the word "Hello", one thing that might be useful is planning out some variables so we can adjust how big everything is. We can store the size of our letters as variables, as well as the size of the gap between letters.

The letter size will be the height and width of a lowercase letter, so an uppercase letter will just be twice that size.

```python
letter_size = 30
gap = 10
```

Next we want to move the turtle left a ways without drawing so that we are starting further left on the screen. We can lift the pen up, and move the turtle back. 

```python
penup()

# Account for 'H' and 'e' and the gaps between them
backward_length = (letter_size * 2) + (gap * 2)

backward(backward_length)
```

Now we are ready to start writing!

```python

# H
pendown()
left(90)
forward(letter_size * 2)
backward(letter_size)
right(90)
forward(letter_size)
left(90)
forward(letter_size)
backward(letter_size * 2)
right(90)
penup()
forward(gap)

# e
pendown()
left(90)
forward(letter_size)
right(90)
forward(letter_size)
right(90)
forward(letter_size / 2)
right(90)
forward(letter_size)
left(90)
forward(letter_size / 2)
left(90)
forward(letter_size)
penup()
forward(gap)

# l
pendown()
left(90)
forward(letter_size * 2)
right(90)
penup()
forward(gap)

# l 
pendown()
right(90)
forward(letter_size * 2)
left(90)
penup()
forward(gap)

# o
pendown()
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)
```

Now, you could just copy and paste that code. And maybe you did! But that's okay, because it's going to be a jumping off point for your next challenge!

# Extension Activity: Turtle Drawing

Create a new file named `turtle_drawing.py` inside of your root folder.

Create your own original drawing from scratch using Python's Turtle library.

If you need ideas for your drawing, you could:

* Write your own name or the name of your school
* Draw a self-portrait
* Draw a house
* Draw a car
* Draw your favorite animal

## Requirements

* Draw at least **15 visible lines** using Turtle movement commands.
* Use at least **3 different colors** in the finished drawing.
* Use `penup()` and `pendown()` to create at least **2 separate sections** of the drawing that are not connected by lines.
* Use both `left()` and `right()` to change the turtle's direction.
* Create and use at least **one variable** to control a measurement in your drawing, such as the length of a line or the distance between parts.
