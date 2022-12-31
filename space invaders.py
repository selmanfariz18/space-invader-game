import turtle,random,math,winsound

from player import Player
from enemy import Enemy
from bullet import Bullet
from score import Score

scr=turtle.Screen()
scr.setup(1000,600,0,0)
scr.bgcolor('black')
scr.title('Space invader')
scr.bgpic('dp.gif')

p=Player()
enemies=[]
for i in range(8):
    enemies.append(Enemy())
b=Bullet()
s=Score()

def collisionplay(a,b):
    distance=math.sqrt(abs(math.pow((a.xcor()-b.xcor()),2)+math.pow((a.ycor()-b.ycor()),2)))
    if distance<20:
        return True
    else:
        return False

def collision(a,b):
    distance=math.sqrt(abs(math.pow((a.xcor()-b.xcor()),2)+math.pow((a.ycor()-b.ycor()),2)))
    if distance<25:
        return True
    else:
        return False

def fireBullet():
    global selfstate
    if b.state=="Ready":
        b.state="Fire"
        winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
        x=p.xcor()
        y=p.ycor()+30
        b.goto(x,y)
        b.showturtle()

turtle.listen()
turtle.onkey(p.move_left,"Left")
turtle.onkey(p.move_right,"Right")
turtle.onkey(fireBullet,"space")


#main
while True:
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemy.speedamt
        enemy.setx(x)
        if enemy.xcor()>425:
            for j in enemies:
                y=j.ycor()
                y-=25
                j.sety(y)
            enemy.speedamt*=-1
        if enemy.xcor()<-425:
            for j in enemies:
                y=j.ycor()
                y-=20
                j.sety(y)
            enemy.speedamt*=-1
        #check collision
        if collisionplay(b,enemy):
            b.hideturtle()
            b.state='Ready'
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            b.setposition(0,-400)
            x=random.randint(-300,300)
            y=random.randint(180,280)
            enemy.setposition(x,y)
            #score
            s.Scorevalue+=10
            s.clear()
            s.write("score:{}".format(s.Scorevalue),align="left",font=("Arial",14,"bold"))
        #collide
        if collision(p,enemy):
            for e in enemies:
                e.hideturtle()
            p.hideturtle()
            s.pu()
            s.goto(0,0)
            s.pd()
            s.write("GAme Over!!",align='left',font=("Arial",14,"bold"))
            break
        if enemy.ycor()<=-200:
            winsound.PlaySound("gameover.wav",winsound.SND_ASYNC)
            for j in enemies:
                j.hideturtle()
            p.hideturtle()
            p.hideturtle()
            s.pu()
            s.goto(0,0)
            s.pd()
            s.write("GAme Over!!",align='left',font=("Arial",14,"bold"))
            break
    y=b.ycor()
    y+=b.speedamt
    b.sety(y)
    if b.ycor()>150:
        b.state="Ready"
    if b.ycor()>300:
        b.hideturtle()
        b.state="Ready"            

