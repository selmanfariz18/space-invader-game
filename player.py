import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("player.gif")
        self.color('blue')
        self.speed(0)
        self.shape('player.gif')
        self.pu()
        self.goto(0,-250)

        self.playerspeed=40
    
    def move_left(self):
        q =self.xcor()
        q -= self.playerspeed
        if q < -450:
            q=-450
        self.setx(q)

    def move_right(self):
        q =self.xcor()
        q += self.playerspeed
        if q > 450:
            q=450
        self.setx(q)

    