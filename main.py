from turtle import Turtle, Screen
import random

# ---- CONFIG ----
COLORS = ["red", "blue", "green", "yellow", "black"]
LANES_Y = [-80, -40, 0, 40, 80]
FINISH_X = 200

# ---- SETUP ----
screen = Screen()
screen.setup(500, 300)
screen.title("Turtle Race")

# Ask the user for a valid bet color
def ask_for_bet():
    prompt = f"Pick a color from: {', '.join(COLORS)}"
    while True:
        ans = screen.textinput(title="Enter your bet", prompt=prompt)
        if ans is None:
            return None  # User pressed Cancel
        ans = ans.strip().lower()
        if ans in COLORS:
            return ans
        prompt = f"Invalid color!\nChoose from: {', '.join(COLORS)}"

user_bet = ask_for_bet()
race_is_on = bool(user_bet)

# Draw finish line
finish = Turtle(visible=False)
finish.penup(); finish.goto(FINISH_X, -140)
finish.setheading(90); finish.pendown()
finish.width(3); finish.color("gray"); finish.forward(280)

# Write color labels on the left side
label = Turtle(visible=False)
label.penup(); label.color("black")
for y, c in zip(LANES_Y, COLORS):
    label.goto(-230, y-10)
    label.write(c, font=("Arial", 10, "normal"))

# Create turtles
turtles = []
for i, c in enumerate(COLORS):
    t = Turtle(shape="turtle")
    t.penup(); t.speed("fastest")
    t.color(c)
    t.goto(x=-200, y=LANES_Y[i])
    turtles.append(t)

# Writer for displaying the result
writer = Turtle(visible=False)
writer.penup(); writer.goto(0, 0); writer.hideturtle()

# ---- RACE ----
while race_is_on:
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() > FINISH_X:
            race_is_on = False
            winner = t.pencolor()
            msg = f"THE WINNER IS {winner.upper()} TURTLE!\n"
            if user_bet and user_bet.lower() == winner.lower():
                msg += "\nCONGRATS, YOU WIN!"
            else:
                msg += "\nUNFORTUNATELY, YOU LOSE!"
            writer.write(msg, align="center", font=("Arial", 14, "bold"))
            break

screen.exitonclick()
