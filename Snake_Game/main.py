def want_to_continue():
    from turtle import Turtle, Screen
    import time
    import random

    my_screen = Screen()
    my_screen.bgcolor("black")
    my_screen.setup(height=600, width=600)
    my_screen.title("Saanp wali Game🐍 ")
    my_screen.tracer(0)


    def north():
        if segments[0].heading() != 270:
            segments[0].setheading(90)
        
    def turn_right():
        if segments[0].heading() != 180:
            segments[0].setheading(0)

    def turn_left():
        if segments[0].heading() != 0:
            segments[0].setheading(180)

    def down():
        if segments[0].heading() != 90:
            segments[0].setheading(270)

    def game_over():
        gameover.hideturtle()
        gameover.color("white")
        gameover.penup() 
        gameover.write("GAME OVER", align="Center", font=("Courier", 24, "normal"))

    def add_segment(position):
        new_segment = Turtle()
        new_segment.color("springgreen")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)

    def extend():
        add_segment(segments[-1].position())

    def retry():
        play_again = want_to_retry.textinput(prompt="YES / NO?", title="play again?")
        if play_again == "yes":
            my_screen.clear()
            want_to_continue()
        else:
            game_over()
            my_screen.exitonclick()






    my_screen = Screen()
    my_screen.listen()
    my_screen.onkey(fun=north, key="Up")
    my_screen.onkey(fun=turn_right, key="Right")
    my_screen.onkey(fun=turn_left, key="Left")
    my_screen.onkey(fun=down, key="Down")




    new_position = ((0,0), (-20,0), (-40,0))
    segments = []

    for position in new_position:
        add_segment(position)
        
    food = Turtle()
    scoreboard = Turtle()
    gameover = Turtle()
    want_to_retry = Screen()
    food.shape("circle")
    food.penup()
    food.shapesize(stretch_len=0.5, stretch_wid=0.5)
    food.color("blue")
    food.speed("fastest")
    random_x = random.randint(-290, 290)
    random_y = random.randint(-290, 290)
    food.goto(x=random_x, y=random_y)

    score = 0


    game_is_on = True

    while game_is_on:
        food_x = random.randint(-280, 280)
        food_y = random.randint(-280, 260)
        if segments[0].distance(food) < 15:
            food.goto(x=food_x, y=food_y)
            score += 1
            extend()
            scoreboard.write(f"Score is:{score} ", align="center", font=("Courier", 24, "normal"))
        if segments[0].xcor() > 280 or segments[0].xcor() < -280 or segments[0].ycor() > 280 or segments[0].ycor() < -280:
            retry()
            scoreboard.clear()
            game_over()
            game_is_on = False
            
            
        

        for segment in segments[1:]:
            if segments[0].distance(segment) < 8:
                scoreboard.clear()
                game_over()
                game_is_on = False
                retry()
                
        


    
        my_screen.update()
        time.sleep(0.05)

        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.color("white")
        scoreboard.goto(x=0,y=260)
        scoreboard.clear()
        scoreboard.write(f"Score is:{score} ", align="center", font=("Courier", 24, "normal"))
            
        for seg in range(len(segments)-1, 0 , -1):
            new_x = segments[seg - 1].xcor()
            new_y = segments[seg - 1].ycor()
            segments[seg].goto(new_x,new_y)
        segments[0].forward(10)




    my_screen = Screen()
    my_screen.exitonclick()

want_to_continue()