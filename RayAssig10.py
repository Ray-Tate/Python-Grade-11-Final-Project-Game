#Name: Ray Tate Assignment 10.
#Input: Poll for mouse movement.
#Processing: Calculate the position of shapes, the score, button registration, and music timing.
#Output: Display calculated shapes and play sound effects.

import pygame, math, sys, random, time

def runMenu(surface,FPS,fpsClock):
    pygame.display.set_caption("Line Walker")
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    yellow = (255,215,0)
    red = (255,0,0)
    while True:
        surface.fill(orange)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break

        button = pygame.Rect(100, 100, 200, 200)
        pygame.draw.rect(surface, green, button)

        button2 = pygame.Rect(500, 100, 200, 200)
        pygame.draw.rect(surface, yellow, button2)

        button3 = pygame.Rect(900, 100, 200, 200)
        pygame.draw.rect(surface, red, button3)

        button4 = pygame.Rect(345, 800, 510, 50)
        pygame.draw.rect(surface, white, button4)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos

            if button.collidepoint(mousePos):
                surface.fill(white)
                return "Game"
            if button2.collidepoint(mousePos):
                surface.fill(white)
                return "Rules"
            if button3.collidepoint(mousePos):
                surface.fill(white)
                return "Quit"
            if button4.collidepoint(mousePos):
                surface.fill(white)
                return "Scores"

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("START", True, black )
        textRect = text.get_rect()
        textRect.center = (200,200)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("RULES", True, black )
        textRect = text.get_rect()
        textRect.center = (600,200)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("EXIT", True, black )
        textRect = text.get_rect()
        textRect.center = (1000,200)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 120)
        text = font.render("Line Walker", True, black )
        textRect = text.get_rect()
        textRect.center = (600,500)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Score History", True, black )
        textRect = text.get_rect()
        textRect.center = (600,825)
        surface.blit(text, textRect)

        pygame.display.update()
        fpsClock.tick(FPS)

def runRules(surface,FPS,fpsClock):
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break
        surface.fill(orange)
        button = pygame.Rect(0, 0, 130, 70)
        pygame.draw.rect(surface, red, button)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos

            if button.collidepoint(mousePos):
                start = "Game"
                surface.fill(white)
                return start

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Control the dot my moving the mouse.", True, black )
        textRect = text.get_rect()
        textRect.center = (600,200)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Move the dot from start to end, keeping it within the lines.", True, black )
        textRect = text.get_rect()
        textRect.center = (600,300)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Gain points by completing levels quickly.", True, black )
        textRect = text.get_rect()
        textRect.center = (600,400)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Use \"ESC\" at any time to exit.", True, black )
        textRect = text.get_rect()
        textRect.center = (600,500)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Back", True, black )
        textRect = text.get_rect()
        textRect.center = (65,35)
        surface.blit(text, textRect)

        pygame.display.update()
        fpsClock.tick(FPS)

def runScoreHistory(surface,FPS,fpsClock,oldScores):
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break
        surface.fill(orange)
        button = pygame.Rect(0, 0, 130, 70)
        pygame.draw.rect(surface, red, button)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos

            if button.collidepoint(mousePos):
                start = "Game"
                surface.fill(white)
                return start

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Back", True, black )
        textRect = text.get_rect()
        textRect.center = (65,35)
        surface.blit(text, textRect)

        if oldScores == []:
            oldScores = "None"
        font = pygame.font.SysFont("ComicSans", 70)
        text = font.render(str(oldScores), True, black )
        textRect = text.get_rect()
        textRect.center = (600,450)
        surface.blit(text, textRect)

        pygame.display.update()
        fpsClock.tick(FPS)

def runDeathScreen(surface,FPS,fpsClock,score):
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    red = (160,0,0)
    pygame.mouse.set_visible(True)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break

        Skull = pygame.image.load("Skull_and_Crossbones.png")
        surface.fill(red)
        surface.blit(Skull, (345,410))
        button = pygame.Rect(345, 350, 510, 50)
        pygame.draw.rect(surface, orange, button)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Score: "+str(score), True, black )
        textRect = text.get_rect()
        textRect.center = (600,275)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Main Menu", True, black )
        textRect = text.get_rect()
        textRect.center = (600,375)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 120)
        text = font.render("You Suck", True, black )
        textRect = text.get_rect()
        textRect.center = (600,120)
        surface.blit(text, textRect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos

            if button.collidepoint(mousePos):
                return

        pygame.display.update()
        fpsClock.tick(FPS)

def runWinScreen(surface,FPS,fpsClock,score):
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    pygame.mouse.set_visible(True)
    ScoreOut = open("Old Score.txt", "a")
    ScoreOut.write ("\n"+str(score))
    ScoreOut.close()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break
        surface.fill(orange)
        pygame.mixer.music.stop()
        button = pygame.Rect(345, 350, 510, 50)
        pygame.draw.rect(surface, green, button)

        font = pygame.font.SysFont("ComicSans", 120)
        text = font.render("You Win", True, black )
        textRect = text.get_rect()
        textRect.center = (600,120)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Score: "+str(score), True, black )
        textRect = text.get_rect()
        textRect.center = (600,275)
        surface.blit(text, textRect)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Main Menu", True, black )
        textRect = text.get_rect()
        textRect.center = (600,375)
        surface.blit(text, textRect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos

            if button.collidepoint(mousePos):
                return

        pygame.display.update()
        fpsClock.tick(FPS)

def runLevel1(surface,FPS,fpsClock):
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    detectWhite = (255,255,255,255)
    detectGreen = (0,255,0,255)
    timeStart = time.time()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break
        surface.fill(orange)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Level 1", True, black )
        textRect = text.get_rect()
        textRect.center = (90,42)
        surface.blit(text, textRect)

        pygame.mouse.set_visible(False)
        rectangle = pygame.Rect(85, 85, 230, 230)
        rectangle2 = pygame.Rect(900, 600, 200, 200)
        rectangle3 = pygame.Rect(155,315,90,430)
        rectangle4 = pygame.Rect(155,665,745,90)
        pygame.draw.rect(surface,white,rectangle,0)
        pygame.draw.rect(surface,green,rectangle2,0)
        pygame.draw.rect(surface,white,rectangle3,0)
        pygame.draw.rect(surface,white,rectangle4,0)
        mousePos = pygame.mouse.get_pos()

        dot1 = [mousePos[0]+16,mousePos[1]]
        dot2 = [mousePos[0],mousePos[1]+16]
        dot3 = [mousePos[0]-16,mousePos[1]]
        dot4 = [mousePos[0],mousePos[1]-16]
        dot5 = [mousePos[0]+11,mousePos[1]+11]
        dot6 = [mousePos[0]-11,mousePos[1]-11]
        dot7 = [mousePos[0]+11,mousePos[1]-11]
        dot8 = [mousePos[0]-11,mousePos[1]+11]

        dot1Colour = surface.get_at(dot1)
        dot2Colour = surface.get_at(dot2)
        dot3Colour = surface.get_at(dot3)
        dot4Colour = surface.get_at(dot4)
        dot5Colour = surface.get_at(dot5)
        dot6Colour = surface.get_at(dot6)
        dot7Colour = surface.get_at(dot7)
        dot8Colour = surface.get_at(dot8)

        pygame.draw.circle(surface,black,mousePos,15,0)

        timeNow = time.time()

        timer = int(timeNow - timeStart)
        score = 1000
        score = score - timer*50

        if score < 0:
            score = 0

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render(str(score), True, black )
        textRect = text.get_rect()
        textRect.center = (1110,42)
        surface.blit(text, textRect)

        pygame.display.update()
        fpsClock.tick(FPS)

        if dot1Colour == detectGreen and dot2Colour == detectGreen and dot3Colour == detectGreen and dot4Colour == detectGreen and dot5Colour == detectGreen and dot6Colour == detectGreen and dot7Colour == detectGreen and dot8Colour == detectGreen:
            return "Win", score
        elif (dot1Colour == detectWhite or dot1Colour == detectGreen)  and (dot2Colour == detectWhite or dot2Colour == detectGreen) and (dot3Colour == detectWhite or dot3Colour == detectGreen) and (dot4Colour == detectWhite or dot4Colour == detectGreen) and (dot5Colour == detectWhite or dot5Colour == detectGreen) and (dot6Colour == detectWhite or dot6Colour == detectGreen) and (dot7Colour == detectWhite or dot7Colour == detectGreen) and (dot8Colour == detectWhite or dot8Colour == detectGreen):
            ok = 0
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Splat Sound Effect.mp3")
            pygame.mixer.music.play(0)
            pygame.mixer.music.set_volume(0.5)
            score = 0
            return "Dead", score

def runLevel2(surface,FPS,fpsClock,score1):
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    detectWhite = (255,255,255,255)
    detectGreen = (0,255,0,255)
    timeStart = time.time()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break
        surface.fill(orange)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Level 2", True, black )
        textRect = text.get_rect()
        textRect.center = (90,42)
        surface.blit(text, textRect)

        timeNow = time.time()

        timer = int(timeNow - timeStart)
        score = 1500 + score1
        score = score - timer*50
        if score < score1:
            score = score1

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render(str(score), True, black )
        textRect = text.get_rect()
        textRect.center = (1110,42)
        surface.blit(text, textRect)

        rectangle = pygame.Rect(900, 600, 200, 200)
        rectangle2 = pygame.Rect(100, 600, 200, 200)
        rectangle3 = pygame.Rect(966, 85, 68, 515)
        rectangle4 = pygame.Rect(784,85,182,68)
        rectangle5 = pygame.Rect(716,85,68,515)
        rectangle6 = pygame.Rect(166, 85, 68, 515)
        rectangle7 = pygame.Rect(234,85,182,68)
        rectangle8 = pygame.Rect(416, 85, 68, 583)
        rectangle9 = pygame.Rect(484,600,300,68)
        rectangle10 = pygame.Rect(300,800,765,-37)
        pygame.draw.rect(surface,white,rectangle,0)
        pygame.draw.rect(surface,green,rectangle2,0)
        pygame.draw.rect(surface,white,rectangle3,0)
        pygame.draw.rect(surface,white,rectangle4,0)
        pygame.draw.rect(surface,white,rectangle5,0)
        pygame.draw.rect(surface,white,rectangle6,0)
        pygame.draw.rect(surface,white,rectangle7,0)
        pygame.draw.rect(surface,white,rectangle8,0)
        pygame.draw.rect(surface,white,rectangle9,0)
        pygame.draw.rect(surface,white,rectangle10,0)

        mousePos = pygame.mouse.get_pos()

        dot1 = [mousePos[0]+16,mousePos[1]]
        dot2 = [mousePos[0],mousePos[1]+16]
        dot3 = [mousePos[0]-16,mousePos[1]]
        dot4 = [mousePos[0],mousePos[1]-16]
        dot5 = [mousePos[0]+11,mousePos[1]+11]
        dot6 = [mousePos[0]-11,mousePos[1]-11]
        dot7 = [mousePos[0]+11,mousePos[1]-11]
        dot8 = [mousePos[0]-11,mousePos[1]+11]

        dot1Colour = surface.get_at(dot1)
        dot2Colour = surface.get_at(dot2)
        dot3Colour = surface.get_at(dot3)
        dot4Colour = surface.get_at(dot4)
        dot5Colour = surface.get_at(dot5)
        dot6Colour = surface.get_at(dot6)
        dot7Colour = surface.get_at(dot7)
        dot8Colour = surface.get_at(dot8)

        pygame.draw.circle(surface,black,mousePos,15,0)

        if dot1Colour == detectGreen and dot2Colour == detectGreen and dot3Colour == detectGreen and dot4Colour == detectGreen and dot5Colour == detectGreen and dot6Colour == detectGreen and dot7Colour == detectGreen and dot8Colour == detectGreen:
            return "Win", score
        elif (dot1Colour == detectWhite or dot1Colour == detectGreen)  and (dot2Colour == detectWhite or dot2Colour == detectGreen) and (dot3Colour == detectWhite or dot3Colour == detectGreen) and (dot4Colour == detectWhite or dot4Colour == detectGreen) and (dot5Colour == detectWhite or dot5Colour == detectGreen) and (dot6Colour == detectWhite or dot6Colour == detectGreen) and (dot7Colour == detectWhite or dot7Colour == detectGreen) and (dot8Colour == detectWhite or dot8Colour == detectGreen):
            ok = 0
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Splat Sound Effect.mp3")
            pygame.mixer.music.play(0)
            pygame.mixer.music.set_volume(0.25)
            return "Dead", score1

        pygame.display.update()
        fpsClock.tick(FPS)

def runLevel3(surface,FPS,fpsClock,score1):
    orange = (255,165,0)
    green = (0,255,0)
    black = (0,0,0)
    white = (255,255,255)
    detectWhite = (255,255,255,255)
    detectGreen = (0,255,0,255)
    timeStart = time.time()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return "Quit"
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                return "Quit"
                break
        surface.fill(orange)

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render("Level 3", True, black )
        textRect = text.get_rect()
        textRect.center = (90,42)
        surface.blit(text, textRect)

        timeNow = time.time()

        timer = int(timeNow - timeStart)
        score = 2000 + score1
        score = score - timer*50
        if score < score1:
            score = score1

        font = pygame.font.SysFont("ComicSans", 50)
        text = font.render(str(score), True, black )
        textRect = text.get_rect()
        textRect.center = (1110,42)
        surface.blit(text, textRect)

        rectangle = pygame.Rect(100, 600, 200, 200)
        rectangle2 = pygame.Rect(500, 350, 200, 200)
        rectangle3 = pygame.Rect(166, 85, 68, 515)
        rectangle4 = pygame.Rect(234, 85, 732, 68)
        rectangle5 = pygame.Rect(966, 85, 68, 649)
        rectangle6 = pygame.Rect(566, 666, 400, 68)
        rectangle7 = pygame.Rect(566, 666, 68, -116)
        pygame.draw.rect(surface,white,rectangle,0)
        pygame.draw.rect(surface,green,rectangle2,0)
        pygame.draw.rect(surface,white,rectangle3,0)
        pygame.draw.rect(surface,white,rectangle4,0)
        pygame.draw.rect(surface,white,rectangle5,0)
        pygame.draw.rect(surface,white,rectangle6,0)
        pygame.draw.rect(surface,white,rectangle7,0)

        mousePos = pygame.mouse.get_pos()

        dot1 = [mousePos[0]+16,mousePos[1]]
        dot2 = [mousePos[0],mousePos[1]+16]
        dot3 = [mousePos[0]-16,mousePos[1]]
        dot4 = [mousePos[0],mousePos[1]-16]
        dot5 = [mousePos[0]+11,mousePos[1]+11]
        dot6 = [mousePos[0]-11,mousePos[1]-11]
        dot7 = [mousePos[0]+11,mousePos[1]-11]
        dot8 = [mousePos[0]-11,mousePos[1]+11]

        dot1Colour = surface.get_at(dot1)
        dot2Colour = surface.get_at(dot2)
        dot3Colour = surface.get_at(dot3)
        dot4Colour = surface.get_at(dot4)
        dot5Colour = surface.get_at(dot5)
        dot6Colour = surface.get_at(dot6)
        dot7Colour = surface.get_at(dot7)
        dot8Colour = surface.get_at(dot8)

        pygame.draw.circle(surface,black,mousePos,15,0)

        if dot1Colour == detectGreen and dot2Colour == detectGreen and dot3Colour == detectGreen and dot4Colour == detectGreen and dot5Colour == detectGreen and dot6Colour == detectGreen and dot7Colour == detectGreen and dot8Colour == detectGreen:
            return "Win", score
        elif (dot1Colour == detectWhite or dot1Colour == detectGreen)  and (dot2Colour == detectWhite or dot2Colour == detectGreen) and (dot3Colour == detectWhite or dot3Colour == detectGreen) and (dot4Colour == detectWhite or dot4Colour == detectGreen) and (dot5Colour == detectWhite or dot5Colour == detectGreen) and (dot6Colour == detectWhite or dot6Colour == detectGreen) and (dot7Colour == detectWhite or dot7Colour == detectGreen) and (dot8Colour == detectWhite or dot8Colour == detectGreen):
            ok = 0
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Splat Sound Effect.mp3")
            pygame.mixer.music.play(0)
            pygame.mixer.music.set_volume(0.25)
            return "Dead", score1

        pygame.display.update()
        fpsClock.tick(FPS)

def main():
    pygame.init()

    surface = pygame.display.set_mode([1200, 900])
    pygame.display.set_caption("Line Walker")
    FPS = 60
    fpsClock = pygame.time.Clock()
    oldScores = []

    while True:
        pygame.mixer.music.load("Athletic Theme - Super Mario World.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.25)
        menu = runMenu(surface,FPS,fpsClock)
        if menu == "Quit":
            pygame.quit()
            break
        if menu == "Game":
            play = runLevel1(surface,FPS,fpsClock)
            if play[0] == "Win":
                play = runLevel2(surface,FPS,fpsClock,play[1])
                if play[0] == "Win":
                    play = runLevel3(surface,FPS,fpsClock,play[1])
                    if play[0] == "Win":
                        oldScores.append(str(play[1]))
                        play = runWinScreen(surface,FPS,fpsClock,play[1])
                        if play != "Quit":
                            play = (0,0)
        if menu == "Scores":
            play = runScoreHistory(surface,FPS,fpsClock,oldScores)
        if menu == "Rules":
            play = runRules(surface,FPS,fpsClock)
        if play[0] == "Dead":
            oldScores.append(str(play[1]))
            play = runDeathScreen(surface,FPS,fpsClock,play[1])
        if play == "Quit":
            pygame.quit()
            break

if __name__ == '__main__':
    main()
