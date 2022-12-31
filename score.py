import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.speed(0)
        self.Scorevalue=0
        self.pu()
        self.setposition(-350,250)
        self.write("Score:{}",format(self.Scorevalue),align='left',font=('Arial',14,'bold'))
        self.hideturtle()