import turtle
import time
import snake as s
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = s.Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        # print("nom")

    # detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
        print("Game Over")

    # # detect collision with tail-Method 1
    # for segment in snake.segments:
    #     if snake.head == segment:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_on = False
    #         score.game_over()
    #         print(snake.head.distance(segment))
    #         print("Game Over")

    # detect collision with tail-Method 2
    new_segments=snake.segments[1:]
    for segment in new_segments:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
            print(snake.head.distance(segment))
            print("Game Over")

screen.exitonclick()
