# Welcome to my game
# Group 24 - Mengyi & Sauth
import tkinter as tk
import random
from tkinter.constants import ANCHOR, COMMAND, NW, SE, TRUE, W
from tkinter.font import BOLD 
import winsound

# ----------------------------------------------
# TKINTER GRAPHICS
# ----------------------------------------------
window = tk.Tk()
#Adjust size of the window
window.geometry("1200x650")
window.resizable(False,False)

#The title of the window
frame = tk.Frame()
window.title("Space Invader by (Sauth and MengYi)")
canvas = tk.Canvas(frame)

# BACKGROUND IN THE PROCESS=====================
bg = tk.PhotoImage(file="./img/start-game.png")
bg_game = tk.PhotoImage(file="./img/battle-game.png")
loading_background =  tk.PhotoImage(file="./img/loading_bg.png")
game_over =  tk.PhotoImage(file="./img/game-over.png")
game_win =  tk.PhotoImage(file="./img/win-game.png")
# # PLAYER IMAGE........................
player = tk.PhotoImage(file="./img/player.png")  #SIZE OF PLAYER (174x122)

# WINDOW SHOW WHEN PLAYER.................................
player_win = tk.PhotoImage(file="./img/win-game.png")
# PLAYER BULLET..........................
bullet_player = tk.PhotoImage(file="./img/bullet_player.png") #SIZE OF PLAYER BULLET ()
# PLAYER BULLET.......................
bullet_ennemy = tk.PhotoImage(file="./img/bullet_ennemy.png") #SIZE OF PLAYER BULLET (45x45)
bullet_main_ennemy = tk.PhotoImage(file="./img/bullet_main_enimy.png") #SIZE OF PLAYER BULLET (45x45)
# FIRE
fire_ennemy = tk.PhotoImage(file="./img/fire.png")
fire_player = tk.PhotoImage(file="./img/fire_player.png")
# ENNEMY IMAGES.....................
black_ennemy_image = tk.PhotoImage(file="./img/black-animy.png") #SIZE OF ENNEMY (95x95)
blue_ennemy_image = tk.PhotoImage(file="./img/blue-animy.png")
red_ennemy_image = tk.PhotoImage(file="./img/red-animy.png")
main_ennemy_image = tk.PhotoImage(file="./img/main-animy.png") #SIZE OF ENNEMY (330x330)

display_game = False
def display_start_game():
    global display_game
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)  
    if not display_game: 
        canvas.create_image(0,0,anchor=NW, image = bg,tags="start")
        canvas.create_rectangle(378,290,534,350,fill="red",outline="",tags="start")
        canvas.create_text(454,320,text="START",font=("Purisa", 30, BOLD), fill="white",tags=("startTheGame","start"))
        canvas.create_rectangle(660,290,816,350,fill="red",outline="",tags="start")
        canvas.create_text(744,320,text="EXIT",font=("Purisa", 30, BOLD), fill="white",tags=("exitTheGame","start"))
display_start_game()

def backGame(event):
    global display_game
    display_game = False
    display_start_game()

#EXIT THE WINDOW TO STOP THE PROGRAME-----------------------------
def close_the_window(event):
    window.destroy()
#START GAME============
def start_process(event):
    global display_game
    canvas.delete("start")
    display_game = True
    if display_game : 
        loading_the_process()

#LOADING TIME BEFORE ALLOW PLAYER TO PLAY GAME===============================
def loading_the_process():
    canvas.create_image(0,0,image= loading_background, anchor = NW)
    canvas.create_text(600,300,text="Loading...", font= ("Purisa", 40,BOLD), fill="red")
    durationOfLoading = random.randrange(500,2000)
    canvas.after(durationOfLoading,in_processing)


#GAME IN PROCESSING-------------------------------------------
def in_processing():
    global player_pos,player_socre,battle_image
    global_variable()
    battle_image = canvas.create_image(1200, 650, anchor=SE, image=bg_game)
    positionXOfPlayer = random.randrange(100,400)
    positionYOfPlayer = random.randrange(100,400)
    x = 86
    for i in range(5):
        life = canvas.create_rectangle(x,22,x+40,50,fill="red",outline="",tags="blood")
        x += 46
        listOfPlayerLives.append(life)
    player_socre = canvas.create_text(160,100,text="SCORE: 0",font=("Purisa", 16, BOLD), fill="white",tags=("startTheGame","start"))
    player_pos = canvas.create_image(positionXOfPlayer, positionYOfPlayer, image=player)  
    # CALL THE FUNCTION TO PROGRESS=========================================
    create_enemy()
    move_enemies()
    create_player_bullet()
    move_player_bullet()
    move_ennemy_bullet()

def global_variable():
    global listOfPlayerLives, minusPlayerLives, listOfEnemies,SCORE,listOfPlayerBullet,listOfEnnemyBullet,posOfEachEnnemy,newEnnemyStartX,newEnnemyStartY,playerStartX,playerStartY,BulletPlayerStartX,BulletPlayerStartY,positionXOfMainEnnemy,positionYOfMainEnnemy,stopTheGame,NUMBEROFALLENEMY
    # # VARIABLES
    # # ----------------------------------------------
    listOfPlayerLives = []
    minusPlayerLives = 0
    listOfEnemies = []
    SCORE = 0 
    listOfEnemies = []
    listOfPlayerBullet = []
    listOfEnnemyBullet = []
    listOfPlayerLives = []
    posOfEachEnnemy = []
    newEnnemyStartX = 1200
    newEnnemyStartY = 30
    playerStartX = 300
    playerStartY = 400
    BulletPlayerStartX = 380
    BulletPlayerStartY = 400
    positionXOfMainEnnemy = 1200
    positionYOfMainEnnemy = 650
    stopTheGame = True
    NUMBEROFALLENEMY = 100

# DISPLAY FEATURE WHEN PLAYER LOST THE GAME=================================================
def displayLost():
    winsound.PlaySound("sound/mixkit-player-losing-or-failing-2042.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(1200, 650, anchor=SE, image=game_over)
    canvas.create_text(110,70,text="BACK",font=("Purisa", 22, BOLD), fill="white",tags=("back","start"))
    canvas.create_text(600,480,text="SCORES: "+ str(SCORE),font=("Purisa", 50, BOLD), fill="white",tags=("start"))

# DISPLAY FEATURE WHEN PLAYER WIN THE GAME========================================
def displayWin():
    winsound.PlaySound("sound/mixkit-game-level-completed-2059.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(1200, 650, anchor=SE, image=game_win)
    canvas.create_text(110,70,text="BACK",font=("Purisa", 22, BOLD), fill="white",tags=("back","start"))
    canvas.create_text(600,480,text="SCORES: "+ str(SCORE),font=("Purisa", 50, BOLD), fill="white",tags=("start"))

# # ----------------------------------------------
# # CONSTANTS
# # ----------------------------------------------
MOVE_PLAYER_INCREMENT = 20
ENNEMY_IMAGES = [black_ennemy_image,blue_ennemy_image,red_ennemy_image]
SCORE = 0 
BULLET_SIZE = 59
ENNEMY_SIZE = 95
PLAYER_WIDTH = PLAYER_HEIGHT = 45
# # ----------------------------------------------

# # THE POSITION OF THE PLAYER================================================
def getPlayerPosition():
    return canvas.coords(player_pos)

# MOVE POSITION PLAYER BY USING KEY PRESS=====================================
def onWPressed(event):
    if display_game:
        goUp()
def onSPressed(event):
    if display_game:
        goDown()
def onAPressed(event):
    if display_game:
        goLeft()
def onDPressed(event):
    if display_game:
        goRight()

# MOVE POSITION BULLET BY USING KEY PRESS=====================================
#==============================================================================
def goUp():
    if getPlayerPosition()[1] > 50 :
        canvas.move(player_pos, 0, -MOVE_PLAYER_INCREMENT)
#MOVE PLAYER DOWN ======================================================
def goDown():
    if getPlayerPosition()[1] < 600:
        canvas.move(player_pos,0,MOVE_PLAYER_INCREMENT)
#MOVE PLAYER TO LEFT======================================================== 
def goLeft():
    if getPlayerPosition()[0] > 20:
        canvas.move(player_pos,-MOVE_PLAYER_INCREMENT,0)    
#MOVE PLAYER TO RIGHT======================================================
def goRight():
    if getPlayerPosition()[0] < 1000:
        canvas.move(player_pos,MOVE_PLAYER_INCREMENT,0)

# CREATE THE ENNEMIES AND THEIR BULLET TO DISPLAY ON SCREEN ===================
def create_enemy():
    global newEnnemyStartY,NUMBEROFALLENEMY
    if SCORE <= 50 :
        numberEnnemyOnce = random.randrange(5,10)
    elif SCORE > 50 :
        numberEnnemyOnce = random.randrange(10,20)
    if stopTheGame:
        if len(listOfEnemies) < numberEnnemyOnce and NUMBEROFALLENEMY > 0:
            newEnnemyStartY =random.randrange(20,500)
            ennemyImage = random.choice(ENNEMY_IMAGES)
            newEnemy = canvas.create_image(newEnnemyStartX,newEnnemyStartY,image=ennemyImage)
            listOfEnemies.append(newEnemy)
            bullet_of_ennemy = canvas.create_image(newEnnemyStartX, newEnnemyStartY, image=bullet_ennemy)
            listOfEnnemyBullet.append(bullet_of_ennemy)
            NUMBEROFALLENEMY -= 1
        newEnnemyStartY = 30
        if SCORE <= 50 :
            canvas.after(1000, create_enemy)
        elif SCORE > 50 :
            canvas.after(600, create_enemy)

# MOVE POSITION OF THE ENNEMIES TO ANYWHERE===========================
def move_enemies():
    ennemiesToBeDeleted = []
    if stopTheGame:
        for enemy in listOfEnemies:
            canvas.move(enemy, -10, 2)
            posOfEachEnnemy = canvas.coords(enemy)
            if posOfEachEnnemy[0] < 50 or posOfEachEnnemy[1] > 650:
                ennemiesToBeDeleted.append(enemy)
        for ennemy in ennemiesToBeDeleted:
            listOfEnemies.remove(ennemy)
            canvas.delete(ennemy)
        ennemyMeetPlayer(listOfEnemies)
        canvas.after(100,move_enemies)
    return ennemiesToBeDeleted

# CREATE THE BULLET OF THE PLAYER TO DISPLAY ON SCREEN ===================
def create_player_bullet():
    if stopTheGame:
        bullet_of_player = canvas.create_image(getPlayerPosition()[0] + 80, getPlayerPosition()[1], image=bullet_player)
        listOfPlayerBullet.append(bullet_of_player)
        canvas.after(500, create_player_bullet)

# MOVE BULLET OF ENNEMIES TO THE PLAYER   ==============================
def move_ennemy_bullet():
    bulletEnnemyToRemove = []
    if stopTheGame:
        for bullet_ennemy in listOfEnnemyBullet:
            canvas.move(bullet_ennemy, -30, 0)
            pos_bullet = canvas.coords(bullet_ennemy)
            if pos_bullet[0] < 100:
                bulletEnnemyToRemove.append(bullet_ennemy)
        for bullet_ennemy in bulletEnnemyToRemove:
            listOfEnnemyBullet.remove(bullet_ennemy)
            canvas.delete(bullet_ennemy)
        ennemyBulletMeetPlayer(listOfEnnemyBullet)
        canvas.after(100,move_ennemy_bullet)
        winsound.PlaySound("sound/shooting.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        

# MOVE BULLET OF PLAYER TO THE ENNEMIES ==============================
def move_player_bullet():
    bulletToRemove = []
    if stopTheGame:
        for bullet in listOfPlayerBullet:
            canvas.move(bullet, 20, 0)
            # winsound.PlaySound("sound/shoot.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            pos_bullet = canvas.coords(bullet)
            if pos_bullet[0] > 1100:
                bulletToRemove.append(bullet)
        for bullet in bulletToRemove:
            listOfPlayerBullet.remove(bullet)
            canvas.delete(bullet)
        bulletMeetEnnemy()
        # if SCORE > 2:
        #     bulletMeetMainEnnemy()
        canvas.after(100,move_player_bullet)

# DISPLAY FIRE WHEN BULLET OF PLAYER TOUCH ENNEMY ================================
def displayFire():
    positionOfEn = canvas.coords(enemy)
    winsound.PlaySound("sound/bomb.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(positionOfEn[0],positionOfEn[1],image=fire_ennemy,tags="deleteFire")
    canvas.after(300,disappearFire)

# DISPLAY FIRE WHEN PLAYER TOUCH ENNEMY ================================
def displayFirePlayer():
    winsound.PlaySound("sound/bomb.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(getPlayerPosition()[0]+80,getPlayerPosition()[1],image=fire_player,tags="deleteFire")
    canvas.after(300,disappearFire)
def disappearFire():
    canvas.delete("deleteFire")

# TO CHECK IF PLAYER BULLET MEET ENNEMY========================================
def playerBulletMeetEnnemy(listOfPlayerBullets, listOfEnemies):
    global enemy
    toBeDeleted = []
    for playerBullet in listOfPlayerBullets:
        positionOfBulletPlayer = canvas.coords(playerBullet)
        for enemy in listOfEnemies:
            positionOfEn = canvas.coords(enemy)
            if (positionOfBulletPlayer[1]+BULLET_SIZE >= positionOfEn[1]) and (positionOfBulletPlayer[1]+BULLET_SIZE <= positionOfEn[1]+ENNEMY_SIZE ) and (positionOfBulletPlayer[0]+BULLET_SIZE >= positionOfEn[0]) and (positionOfBulletPlayer[0]+BULLET_SIZE <= positionOfEn[0]+ENNEMY_SIZE):
                toBeDeleted.append(playerBullet)
                toBeDeleted.append(enemy)
                displayFire()
    return toBeDeleted

# TO CHECK IF ENNEMY BULLET MEET PLAYER========================================
def ennemyBulletMeetPlayer(listOfEnnemyBullet):
    toBeDeleted = []
    for ennemyBullet in listOfEnnemyBullet:
        positionOfBulletEnnemy = canvas.coords(ennemyBullet)
        if (getPlayerPosition()[1]+PLAYER_HEIGHT >=positionOfBulletEnnemy[1]) and (getPlayerPosition()[1]+PLAYER_HEIGHT <= positionOfBulletEnnemy[1]+85) and (getPlayerPosition()[0]+PLAYER_WIDTH >= positionOfBulletEnnemy[0]) and (getPlayerPosition()[0]+PLAYER_WIDTH <= positionOfBulletEnnemy[0]+85):
            toBeDeleted.append(ennemyBullet)
            bulletMeetPlayer()
            displayFirePlayer()
            deleteEnnemyBullet(ennemyBullet)
    return toBeDeleted

# CHECK WHEN THE PLAYER MEET WITH ENNEMY ==========================================
def ennemyMeetPlayer(listOfEnemies):
    global positionOfEnnemy
    toBeDeleted = []
    for ennemy in listOfEnemies:
        positionOfEnnemy = canvas.coords(ennemy)
        if (getPlayerPosition()[1]+PLAYER_HEIGHT >=positionOfEnnemy[1]) and (getPlayerPosition()[1]+PLAYER_HEIGHT <= positionOfEnnemy[1]+85) and (getPlayerPosition()[0]+PLAYER_WIDTH >= positionOfEnnemy[0]) and (getPlayerPosition()[0]+PLAYER_WIDTH <= positionOfEnnemy[0]+85):
            toBeDeleted.append(ennemy)
            displayFirePlayer()
            bulletMeetPlayer()
            deleteEnnemy(ennemy)
    return toBeDeleted

# DELETE ENNEMY FROM THE LIST OF THE ENNEMY ===================================
def bulletMeetEnnemy():
    meetEnemy = playerBulletMeetEnnemy(listOfPlayerBullet, listOfEnemies)
    if len(meetEnemy) > 0:
        listOfPlayerBullet.remove(meetEnemy[0])
        listOfEnemies.remove(meetEnemy[1])
        canvas.delete(meetEnemy[0])
        canvas.delete(meetEnemy[1])
        scoreIncrement()

# TO MINUS LIVE OF THE PLAYER WHENEVER TOUCHED ENNEMY OR BULLET OF THE ENNEMY====
def bulletMeetPlayer():
    global minusPlayerLives,stopTheGame
    minusPlayerLives += 1
    canvas.itemconfig(listOfPlayerLives[-minusPlayerLives], fill="")
    if minusPlayerLives == 5:
        stopTheGame = False
        canvas.after(1000,displayLost)

# TO DELETE=============================================
def deleteEnnemyBullet(ennemyBullet):
    listOfEnnemyBullet.remove(ennemyBullet)
    canvas.delete(ennemyBullet)
def deleteEnnemy(ennemy):
    listOfEnemies.remove(ennemy)
    canvas.delete(ennemy)
# .............................................

# INCREMENT SOCRE FOR PLAYER WHEN ITS BULLET TOUCH ENNEMY=========================
def scoreIncrement():
    global SCORE,stopTheGame,positionOfEnnemy
    SCORE += 1
    if SCORE <= 1: 
        title = "SCORE: "
    else:
        title = "SCORES: "
    canvas.itemconfig(player_socre,text= title + str(SCORE))
    if NUMBEROFALLENEMY == 0 and len(listOfEnemies)<1 or( SCORE > 90) :
        stopTheGame = False
        canvas.after(1000,displayWin)
# KEYS THAT PLAYER HAS TO PRESS TO PLAY THE GAME=================================
window.bind("<w>", onWPressed)
window.bind("<s>",onSPressed)
window.bind("<d>",onDPressed)
window.bind("<a>",onAPressed)
#LEFT CLICK TO START OR EXIT THE GAME==================================
canvas.tag_bind("startTheGame","<Button-1>",start_process)
canvas.tag_bind("exitTheGame","<Button-1>",close_the_window)
canvas.tag_bind("back","<Button-1>",backGame)
#DISPLAY WINDOW====================================================
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
