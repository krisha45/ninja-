#Jeremiah De Los Santos, Eddie Ruiz, Alex Puello, Krisha Patel
#Collect as many diamonds as you can while you fight off a fire breathing dragon
#Ninja Quest


from gamelib import *

game = Game(800,600,"Ninja Quest")

bk  = Image("battle.jpg",game)
bk.resizeTo(800,600)
ninja = Image("ninja.jpg",game,use_alpha=False)
diamonds = Image("diamond.jpg",game,use_alpha=False)
boost = Image("download.jpg",game,use_alpha=False) 
ninja.resizeBy(-50)
dragon = Image("dragon 2.png",game,use_alpha=False)
ninja.moveTo(100,350)
diamonds.moveTo(500,500)
dragon.moveTo(500,250)
boost.moveTo(400,200) 
diamonds.resizeBy(-90)
boost.resizeBy(-80)
ninja.setSpeed(6,60)
dragon.setSpeed(4,100)
health = 100
score = 0


while not game.over:
    game.processInput() 
    bk.draw()
    ninja.draw()
    boost.draw() 
   

    diamonds.draw()
    dragon.move(True)

    if keys.Pressed[K_UP]:
        ninja.y-=5

    if keys.Pressed[K_DOWN]:
        ninja.y+=5

    if keys.Pressed[K_LEFT]:
        ninja.x-=5
        
    if keys.Pressed[K_RIGHT]:
        ninja.x+=5
    if ninja.collidedWith(diamonds):
        
        diamonds.moveTo(randint(200,600),randint(1,600))
        dragon.moveTo(randint(100,700),randint(100,500)) 
        dragon.speed+=1 
        game.score+=10
        
    if ninja.collidedWith(dragon):
        health-=10
        ninja.moveTo(ninja.x-100,ninja.y)
    
       
    if game.score>=100:
        game.drawText("You Win!!",100,5)
        game.over=True


    if ninja.collidedWith(boost):
        health+=5
        boost.moveTo(randint(300,500),randint(5,400))


    
    if ninja.health <-10:
        game.over = True
    
    
       
   
    game.drawText("Health = " + str(health),650,10)
    
    game.displayScore()#display score


    game.update(60)  

game.quit() 


