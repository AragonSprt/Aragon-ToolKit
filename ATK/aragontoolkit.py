import os
import pyqrcode
import shutil
import turtle
import time
import random


# Application setup
os.system("cls")


# Bools
run = True
menu = True


# Variables
def clear():
    os.system("cls")


# Main program
while run:
    while menu:
        clear()
        print("                                         _______          _ _  ___ _    __     ")
        print("     /\                                 |__   __|        | | |/ (_) |   \ \    ")
        print("    /  \   _ __ __ _  __ _  ___  _ __      | | ___   ___ | | ' / _| |_   \ \   ")
        print("   / /\ \ | '__/ _` |/ _` |/ _ \| '_ \     | |/ _ \ / _ \| |  < | | __|   \ \  ")
        print("  / ____ \| | | (_| | (_| | (_) | | | |    | | (_) | (_) | | . \| | |_     \ \ ")
        print(" /_/    \_\_|  \__,_|\__, |\___/|_| |_|    |_|\___/ \___/|_|_|\_\_|\__|     \_\ ")
        print("                      __/ |                                                    ")
        print("                     |___/                                                     ")
        print("")
        print("")
        print("")
        print("1 | Play Snake game.")
        print("2 | Create a QR code.")
        print("3 | Return a link to TrilomiaV2.")
        print("4 | Return a link to my youtube channel.")
        print("5 | Return the links to my Discord servers.")
        print("6 | Invite links for my bots.")
        print("7 | Quit the tool.")
        print("")

        choice = input("↳ ")

        if choice == "bagel??":
            input("IS THIS A BAGEL ???")
        elif choice == "1":
            play = True

            delay = 0.1

            # Score
            score = 0
            high_score = 0

            # Set up the screen
            wn = turtle.Screen()
            wn.title("Snake Game | By Aragon")
            wn.bgcolor("blue")
            wn.setup(width=600, height=600)
            wn.tracer(0)  # Turns off the screen updates

            # Snake head
            head = turtle.Turtle()
            head.speed(0)
            head.shape("square")
            head.color("black")
            head.penup()
            head.goto(0, 0)
            head.direction = "stop"

            # Snake food
            food = turtle.Turtle()
            food.speed(0)
            food.shape("square")
            food.color("red")
            food.penup()
            food.goto(0, 100)

            segments = []

            # Pen
            pen = turtle.Turtle()
            pen.speed(0)
            pen.shape("square")
            pen.color("white")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 260)
            pen.write("Score: 0  High Score: 0", align="center", font=("Archivo", 24, "normal"))

            # Functions
            def go_up():
                if head.direction != "down":
                    head.direction = "up"


            def go_down():
                if head.direction != "up":
                    head.direction = "down"


            def go_left():
                if head.direction != "right":
                    head.direction = "left"


            def go_right():
                if head.direction != "left":
                    head.direction = "right"


            def move():
                if head.direction == "up":
                    y = head.ycor()
                    head.sety(y + 20)

                if head.direction == "down":
                    y = head.ycor()
                    head.sety(y - 20)

                if head.direction == "left":
                    x = head.xcor()
                    head.setx(x - 20)

                if head.direction == "right":
                    x = head.xcor()
                    head.setx(x + 20)


            def leave():
                play = False
                turtle.bye()

                os.system("aragontoolkit.py")


            # Keyboard bindings
            wn.listen()
            wn.onkeypress(go_up, "z")
            wn.onkeypress(go_down, "s")
            wn.onkeypress(go_left, "q")
            wn.onkeypress(go_right, "d")
            wn.onkeypress(leave, "x")
            # Main game loop
            while play:
                wn.update()

                # Check for a collision with the border
                if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"

                    # Hide the segments
                    for segment in segments:
                        segment.goto(1000, 1000)

                    # Clear the segments list
                    segments.clear()

                    # Reset the score
                    score = 0

                    # Reset the delay
                    delay = 0.1

                    pen.clear()
                    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                              font=("Archivo", 24, "normal"))

                    # Check for a collision with the food
                if head.distance(food) < 20:
                    # Move the food to a random spot
                    x = random.randint(-290, 290)
                    y = random.randint(-290, 290)
                    food.goto(x, y)

                    # Add a segment
                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color("grey")
                    new_segment.penup()
                    segments.append(new_segment)

                    # Shorten the delay
                    delay -= 0.001

                    # Increase the score
                    score += 10

                    if score > high_score:
                        high_score = score

                    pen.clear()
                    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                              font=("Archivo", 24, "normal"))

                    # Move the end segments first in reverse order
                for index in range(len(segments) - 1, 0, -1):
                    x = segments[index - 1].xcor()
                    y = segments[index - 1].ycor()
                    segments[index].goto(x, y)

                # Move segment 0 to where the head is
                if len(segments) > 0:
                    x = head.xcor()
                    y = head.ycor()
                    segments[0].goto(x, y)

                move()

                # Check for head collision with the body segments
                for segment in segments:
                    if segment.distance(head) < 20:
                        time.sleep(1)
                        head.goto(0, 0)
                        head.direction = "stop"

                        # Hide the segments
                        for segment in segments:
                            segment.goto(1000, 1000)

                        # Clear the segments list
                        segments.clear()

                        # Reset the score
                        score = 0

                        # Reset the delay
                        delay = 0.1

                        # Update the score display
                        pen.clear()
                        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                                  font=("Archivo", 24, "normal"))

                time.sleep(delay)

            wn.mainloop()
        elif choice == "2":
            title = input("Give your QR code a title > ")
            text = input("What would you like the QR code to say > ")

            file_name_svg = title + ".svg"

            url = pyqrcode.create(text)

            url.svg(file_name_svg, scale=8)

            os.mkdir(fr"c:\Users\Cyril_\Desktop\{title}")

            shutil.move(file_name_svg, fr"c:\Users\Cyril_\Desktop\{title}")
            input("Your QR code has been created.")
        elif choice == "3":
            input("Here is the link -> https://mega.nz/folder/jZYWQaJA#EgRXuV7QkJ-ohXmmt7eGyA")
        elif choice == "4":
            input("Here is the link -> https://youtube.com/@aragonspirit")
        elif choice == "5":
            print("Here are the links:")
            print("")
            print("Aragon & Etoile de lune Community YT -> https://discord.gg/Ep2HfkdCB52")
            print("")
            print("Insight | Official -> https://discord.gg/rJZuCtgweb")
            print("")
            print("Airport People -> https://discord.gg/MPaQARNas3")
            input("")
        elif choice == "6":
            input("There is the link -> https://docs.google.com/document/d/1_ccn94VXMvPfhrJP-j5KhJdeptKiSbFgymGAb7wum1k/edit?usp=sharing")
        elif choice == "7":
            clear()
            print("  ____               _ ")
            print(" |  _ \             | |")
            print(" | |_) |_   _  ___  | |")
            print(" |  _ <| | | |/ _ \ | |")
            print(" | |_) | |_| |  __/ |_|")
            print(" |____/ \__, |\___| (_)")
            print("         __/ |         ")
            print("        |___/          ")
            print("")
            print(" -> You successfully left the tool.")
            quit()
        else:
            input("Please choose a number between the ones ahead!")
