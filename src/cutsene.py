import pygame
import random
from pathlib import Path
from spritesheet import*


class CutScene:
    def __init__(self):
        self.minister = pygame.image.load("../res/tory.png").convert_alpha()
        self.phone = pygame.image.load("../res/phone.png").convert_alpha()
        self.rece = pygame.image.load("../res/rec.png").convert_alpha()
        self.mou = pygame.image.load("../res/m.png").convert_alpha()

        self.left_click = SpriteSheet(self.mou, 3, 300, 300, 400, 400, 2)
        self.right_click = SpriteSheet(self.mou, 3, 300, 300, 400, 400, 1)
        self.sheet_phone = SpriteSheet(self.phone, 1, 200, 200, 100, 100)
        self.sheet_recev = SpriteSheet(self.rece, 1, 200, 200,93, 33)
        self.angle = 0

        self.target_angle = -90
        self.target_angle2 = 0

        self.recev_start = [500, 312]
        self.recev_target = [550, 150]
        self.recev_loc = [500, 312]

        ##states call, end and info
        self.state = "call"
        self.size = 30
        
        ###conditionals for the sounds
        self.sound_1 = False
        self.sound_2 = False

        self.font = pygame.font.Font(Path(r'../res/LondonTube-MABx.ttf'), self.size)    
        self.text_target = 30
        self.rect_target = 20

        self.end_target = 50

    def play(self, screen, setting, button_list, text_list, block_list, speed_buttons, func_buts, sound_list):
        screen.blit(self.minister, (0, 0))
        
        
        #screen.blit(self.rece, (200, 300))
        screen.blit(self.sheet_phone.animation_list[self.sheet_phone.ind], (500, 300))
        
        
        if self.state == "call":
            rotated_image = pygame.transform.rotate(self.sheet_recev.animation_list[self.sheet_recev.ind], self.angle)
            screen.blit(rotated_image, self.recev_loc)
            if self.recev_loc[1] > self.recev_target[1]:
                self.recev_loc[1] -= 2

            if self.recev_loc[0] < self.recev_target[0]:
                self.recev_loc[0] += 1
            
            if self.angle > self.target_angle:
                self.angle-=1

            button_list[0].draw(screen, "SKIP", setting)
            button_list[1].draw(screen, "NEXT", setting)

            
            block_list[0].draw(screen)
          
            if block_list[0].x_pos > self.rect_target:
                block_list[0].x_pos -= 10

            if setting.txt_state == 1:
                if text_list[0].x_pos > self.text_target:
                    text_list[0].x_pos -= 10
                    text_list[1].x_pos -= 10
                    text_list[2].x_pos -= 10
            
            text_list[0].draw(screen, "Hello Mr Transport Minister. With 7 months until the")
            text_list[1].draw(screen, "election. We've decided to enact heavy tax cuts. To")
            text_list[2].draw(screen, "fund this we've decided to cut waste... ")
            
            
            #text_target
            #text_list[0].x_pos += 10

            if setting.txt_state == 2:
                button_list[1].refresh()
                if text_list[4].x_pos > self.text_target:
                    text_list[0].x_pos -= 10
                    text_list[1].x_pos -= 10
                    text_list[2].x_pos -= 10
                    text_list[4].x_pos -= 10
                    text_list[5].x_pos -= 10
                    text_list[6].x_pos -= 10

            text_list[4].draw(screen, "by firing everyone who works on the underground. ")
            text_list[5].draw(screen, "Now thats your job. Congratulations, make sure no")
            text_list[6].draw(screen, "one dies! That would look bad.")

            if setting.txt_state >= 3:
                button_list[1].refresh()
                self.state = "end"
                
            #                           "BLIMEY!"
        if self.state == "end":
            rotated_image = pygame.transform.rotate(self.sheet_recev.animation_list[self.sheet_recev.ind], self.angle)
            screen.blit(rotated_image, self.recev_loc)
            if self.sound_1 == False:
                sound_list[0].play()
                self.sound_1 = True
            block_list[1].draw(screen)
            block_list[0].draw(screen)
            block_list[0].x_pos -= 10
            text_list[4].x_pos -= 10
            text_list[5].x_pos -= 10
            text_list[6].x_pos -= 10
            text_list[4].draw(screen, "by firing everyone who works on the underground. ")
            text_list[5].draw(screen, "Now thats your job. Congratulations, make sure no")
            text_list[6].draw(screen, "one dies! That would look bad.")
            button_list[0].draw(screen, "SKIP", setting)
            button_list[1].draw(screen, "NEXT", setting)
            

            if self.angle < self.target_angle2:
                self.angle+=1

            if self.recev_loc[1] < self.recev_start[1]:
                self.recev_loc[1] += 2

            if self.recev_loc[0] > self.recev_start[0]:
                self.recev_loc[0] -= 1

            text_list[3].draw(screen, "BLIMEY!")

            if setting.txt_state == 4:
                button_list[1].refresh()
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((0,0), (2000, 2000)))
                button_list[0].draw(screen, "SKIP", setting)
                button_list[1].draw(screen, "NEXT", setting)
                screen.blit(self.left_click.animation_list[self.left_click.ind], (30, 230))
                screen.blit(self.right_click.animation_list[self.right_click.ind], (450, 230))
                text_list[8].draw(screen, "LEFT CLICK ON TRAINS                   RIGHT CLICK ON TRAINS")
                text_list[7].draw(screen, "     TO STOP THEM                                TO SPEED THEM UP")

            if setting.txt_state == 5:
                button_list[1].refresh()
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((0,0), (2000, 2000)))
                text_list[8].draw(screen, "Press A to slow down time\nPress D to speed up time\nPress Space to pause ")
                func_buts(setting, speed_buttons)
                speed_buttons[0].draw(screen, "II", setting)
                speed_buttons[1].draw(screen, ">", setting)
                speed_buttons[2].draw(screen, ">>", setting)
                button_list[0].draw(screen, "SKIP", setting)
                button_list[1].draw(screen, "NEXT", setting)
                text_list[9].draw(screen, "Left click on crossings to\ntrun them a train \ncan go through \nany crossing facing \nthe same direction\nOtherwise the train \ncrashes!")
                
                
            if setting.txt_state == 6:
                button_list[1].refresh()
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((0,0), (2000, 2000)))
                
                text_list[9].draw(screen, "DROP OFF 30,000 PASSENGERS OR MORE, \nAND DON'T CRASH MORE THAN 6 TRAINS\nto win the election coming up in May!")
                button_list[0].draw(screen, "SKIP", setting)
                button_list[1].draw(screen, "NEXT", setting)

            if setting.txt_state == 7:
                setting.state = "game"

    def end_scene(self, setting, screen, txt_list, button_list, sound_list):
        screen.blit(self.minister, (200, 0))

        if self.sound_2 == False:
            sound_list[1].play()
            self.sound_2 = True

        button_list[0].draw(screen, "REPLAY", setting)
        button_list[1].draw(screen, "EXIT", setting)

        button_list[0].refresh()

        if txt_list[0].y_pos > self.end_target:
            for t in txt_list:
                t.y_pos -= 10
        if setting.passengers >= 30000 and setting.crashes <= 6:
            setting.elections_won = 1
            txt_list[0].draw(screen, f"Congratulations Mr Minister:")
        else:
            txt_list[0].draw(screen, f"Sad times Mr Minister:")

        
        txt_list[1].draw(screen, f"   Passengers transported: {setting.passengers}")
        txt_list[2].draw(screen, f"   Trains crashed: {setting.crashes}")
        txt_list[3].draw(screen, f"   Stops used: {setting.freezes}")
        txt_list[4].draw(screen, f"   Speed boosts used: {setting.speedys}")

        

        txt_list[5].draw(screen, f"   Elections won: {setting.elections_won}")
        txt_list[6].draw(screen, f"{setting.end_txts[setting.elections_won]}")
        

class Particles:
    def __init__(self, pos):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.origin_x = pos[0]
        self.origin_y = pos[1]
        self.size = 20


        self.directions = []
        
        #self.directions = [[0,2],[2, 2], [-2, 2], [-2, 0], [2, 0], [0, -2], [2, -2], [-2, -2]]
        self.rect_pos = []
        self.rect_sizes = []
        self.rects = []
        #for i in range(len(self.rects)):
            #self.directions.append([random.randint(-2, 2), random.randint(-2, 2)])
        self.created = False


    def explosion(self, screen, pos):
        if self.created == False:
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.origin_x = pos[0]
            self.origin_y = pos[1]

            self.rect_pos = [(self.x_pos, self.y_pos)]*16
            self.rect_sizes = [(self.size, self.size)]*16
            self.rects = [pygame.Rect(posi, size) for posi, size in zip(self.rect_pos, self.rect_sizes)]
            for i in range(len(self.rects)):
                self.directions.append([random.randint(-2, 2), random.randint(-2, 2)])

            self.created = True
            
        if self.size > 0:
            #
            #ffc071	(255,192,113)
            #ffa255	
            #ff5b14	(255,91,20)
            #ff2323	(255,35,35)
            for rect in self.rects:
                if self.size >= 20:
                    pygame.draw.rect(screen, (254,255,181), rect)

                if self.size >=14 and self.size < 20:
                    pygame.draw.rect(screen, (255,162,85), rect)
                
                if self.size >= 5 and self.size < 14:
                    pygame.draw.rect(screen, (255,35,35), rect)

                if self.size <= 4:
                    pygame.draw.rect(screen, (0, 0, 0), rect)
                
                self.size -= 0.03
                rect[2] = self.size
                rect[3] = self.size

            for r in range(len(self.rects)):
                self.rects[r][0] += self.directions[r][0]
                self.rects[r][1] += self.directions[r][1]
        

        

    
    def refresh(self):
        self.created = False
        self.size = 26






            
