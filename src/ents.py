import pygame
import random
from spritesheet import*

class Train:
    def __init__(self, image, route, start = 0, ghost = False):
        self.x_pos = route.points[start][0]
        self.y_pos = route.points[start][1]
        self.start_x_pos = self.x_pos
        self.start_y_pos = self.y_pos
        self.route = route
        self.loop = route.loop
        self.ghost = ghost

        ###to tell the train if its going
        self.going = True
        self.timer = 0
        self.prev_dest = 0
        self.dest = 1 # self = self, dest = destination
        self.forward = True

        ###this handels the timer for the freezing of the trains after being clicked on
        self.frozen = False
        self.f_tick_timer = pygame.time.get_ticks()

        ###thisll handle the speedy shit
        self.speedy = False
        self.s_tick_timer = pygame.time.get_ticks()

        ###help control speed
        ###this is added to the end of the movement
        ### *0 to stop a train, *2 to double speed
        ###the *2 speed doesnt work, as they keep going forever at some point
        self.multi = 1

        #for scaling 
        self.size = 24
        self.size_half = self.size/2
        #i added this width var, to work properly we need to rotate the train as well
        #self.size_width = self.size*3
        self.size_width = self.size

        ###this is to work out if the train has crashed or not
        self.alive = True
        self.fired = False
        #for the collisions
        self.col_rect = pygame.Rect(self.x_pos, self.y_pos, 10, 10)

        ###to test train rect
        self.RECT_COLOUR = (30, 30, 150)
        self.NORMAL_COLOUR = (30, 30, 150)
        self.FROZE_COLOUR = (0, 213, 250)
        self.SPEEDY_COLOUR = (255, 210, 0)

        if self.ghost:
            gray = (150, 150, 150)
            self.RECT_COLOUR = gray
            self.NORMAL_COLOUR = gray
            self.FROZE_COLOUR = gray
            self.SPEEDY_COLOUR = gray
        
        self.sprite = SpriteSheet(0, 0, 0, 0, 0, 0)
    
    def move(self, setting, screen, particles = None):
        ###thisll work if the train hasnt crashed
        if self.alive == True and self.ghost == False:

            ###this code handels freezing the train
            if self.frozen == True:
                if setting.game_speed > 0:
                    froze_ticks = (pygame.time.get_ticks() - self.f_tick_timer) // (1000/setting.game_speed)
                    self.multi = 0
                    self.RECT_COLOUR = self.FROZE_COLOUR
                    if froze_ticks > 2:
                        self.multi = 1
                        self.frozen = False
                        setting.freezes += 1
                        self.RECT_COLOUR = self.NORMAL_COLOUR
                
                    
            if self.frozen == False:
                self.f_tick_timer = pygame.time.get_ticks()

            ###this is for speeding
            if self.speedy == True:
                if setting.game_speed > 0:
                    froze_ticks = (pygame.time.get_ticks() - self.s_tick_timer) // (1000/setting.game_speed)
                    self.multi = 2
                    self.RECT_COLOUR = self.SPEEDY_COLOUR
                    if froze_ticks > 2:
                        self.multi = 1
                        self.speedy = False
                        setting.speedys += 1
                        self.RECT_COLOUR = self.NORMAL_COLOUR
                    
                    
            if self.speedy == False:
                self.s_tick_timer = pygame.time.get_ticks()


            can_pause = True
            """if self.going == False:
                print(f"Timer: {self.timer}, time: {pygame.time.get_ticks()}\n")
                if self.timer <= pygame.time.get_ticks():
                    self. going == True
                    can_pause = False     """
            if self.going == True:        
                if self.route.points[self.dest][0] > self.route.points[self.prev_dest][0]:
                    self.x_pos += setting.SPEED* self.multi
                elif self.route.points[self.dest][0]< self.route.points[self.prev_dest][0]:
                    self.x_pos -= setting.SPEED* self.multi

                if self.route.points[self.dest][1] > self.route.points[self.prev_dest][1]:
                    self.y_pos += setting.SPEED* self.multi
                elif self.route.points[self.dest][1] < self.route.points[self.prev_dest][1]:
                    self.y_pos -= setting.SPEED* self.multi

            """for s in self.route.stations:
                if self.x_pos == s.x_pos and self.y_pos == s.y_pos:
                    if self.going and can_pause:
                        self.timer = pygame.time.get_ticks() + 2000
                        self.going = False"""


            if self.loop == False:
                #if self.x_pos == self.route.points[self.dest][0] and self.y_pos == self.route.points[self.dest][1]:
                if self.route.points[self.dest][0] - setting.SPEED*self.multi < self.x_pos < self.route.points[self.dest][0] + setting.SPEED*self.multi:
                    if self.route.points[self.dest][1] - setting.SPEED*self.multi < self.y_pos < self.route.points[self.dest][1] + setting.SPEED*self.multi:

                        self.x_pos = self.route.points[self.dest][0]
                        self.y_pos = self.route.points[self.dest][1]

                        if self.forward == True:
                            if self.dest < len(self.route.points)-1:
                                self.prev_dest = self.dest
                                self.dest += 1
                                setting.passengers += random.randint(10, 150)
                            else:
                                setting.passengers += random.randint(10, 150)
                                
                                self.forward = False
                                self.prev_dest = self.dest
                                
                                self.dest -= 1
                                

                        elif self.forward == False:
                            if self.dest > 0:
                                self.prev_dest = self.dest
                                self.dest -= 1
                                setting.passengers += random.randint(10, 150)
                            else:
                                setting.passengers += random.randint(10, 150)

                                self.forward = True
                                self.prev_dest = self.dest
                                
                                self.dest += 1
                                
                        #print(f"x: {self.x_pos}, y: {self.y_pos}\n dest: {self.dest}") 

            if self.loop == True:
                if self.route.points[self.dest][0] - setting.SPEED*self.multi < self.x_pos < self.route.points[self.dest][0] + setting.SPEED*self.multi:
                    if self.route.points[self.dest][1] - setting.SPEED*self.multi < self.y_pos < self.route.points[self.dest][1] + setting.SPEED*self.multi:

                        self.x_pos = self.route.points[self.dest][0]
                        self.y_pos = self.route.points[self.dest][1]

                        if self.dest < len(self.route.points)-1:
                                self.prev_dest = self.dest
                                self.dest += 1
                                setting.passengers += random.randint(10, 150)
                        else:
                            setting.passengers += random.randint(10, 150)
                            self.prev_dest = self.dest
                            self.dest = 0
            

            

            pygame.draw.rect(screen, self.RECT_COLOUR, pygame.Rect(self.x_pos - self.size_half, self.y_pos - self.size_half, self.size, self.size_width))
            ##sets the collision rect to the current location of the drawn rect
            self.col_rect = pygame.Rect(self.x_pos - self.size_half, self.y_pos - self.size_half, self.size, self.size_width)

        elif self.alive == False:

            particles.explosion(screen, [self.x_pos, self.y_pos])

        elif self.ghost == True:
            pygame.draw.rect(screen, self.RECT_COLOUR, pygame.Rect(self.x_pos - self.size_half, self.y_pos - self.size_half, self.size, self.size_width))


    
    def refresh(self):
        self.alive = True
        self.x_pos = self.start_x_pos
        self.y_pos = self.start_y_pos
        self.going = True
        self.timer = 0
        self.prev_dest = 0
        self.dest = 1 # self = self, dest = destination
        self.forward = True
        
        
class crossing:
    def __init__(self, x_pos, y_pos, vertical: bool = False) -> None:
        self.sz = 24
        self.ln_sz = 6
        self.colour = (0, 10, 60)
        self.x_pos = x_pos - self.sz/2
        self.y_pos = y_pos - self.sz/2
        self.vertical = vertical #allows vertical. If false, only allows horizontal
        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.sz, self.sz)

    def draw(self, surface):
        if self.vertical:
            pygame.draw.rect(surface, self.colour, (self.x_pos + 1, self.y_pos, (self.sz - self.ln_sz)/2, self.sz))
            pygame.draw.rect(surface, self.colour, (self.x_pos + 1 + (self.sz - self.ln_sz)/2 + self.ln_sz , self.y_pos, (self.sz - self.ln_sz)/2, self.sz))
        else:
            pygame.draw.rect(surface, self.colour, (self.x_pos, self.y_pos + 1, self.sz, (self.sz - self.ln_sz)/2))
            pygame.draw.rect(surface, self.colour, (self.x_pos, self.y_pos + 1 + (self.sz - self.ln_sz)/2 + self.ln_sz , self.sz, (self.sz - self.ln_sz)/2))

    def update_col(self, train_list, screen):
        for t in train_list:
            if pygame.Rect.colliderect(self.hitbox, t.col_rect):
                if t.route.points[t.prev_dest][0] == t.route.points[t.dest][0] and self.vertical == False:
                    t.alive = False
                    #todo add explosion
                elif t.route.points[t.prev_dest][1] == t.route.points[t.dest][1] and self.vertical == True:
                    t.alive = False
        

class Stations:
    def __init__(self, image, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

def get_lines(station1: Stations, station2: Stations) -> tuple: 

    #returns [l1_start(x, y), l2_start, l3_start, l3_end] if not same x or y

    if station1.x_pos == station2.x_pos and station1.y_pos == station2.y_pos: #returns no line if stations on same position
        return None 
    
    elif station1.x_pos == station2.x_pos or station1.y_pos == station2.y_pos: #returns single line if on same x or y
        return [(station1.x_pos, station1.y_pos), (station2.x_pos, station2.y_pos)]
    
    else:
        x_dist = abs(station2.x_pos - station1.x_pos)
        y_dist = abs(station2.y_pos - station1.y_pos)

        if x_dist > y_dist:
            x_angle_len = y_dist
            y_angle_len = y_dist
            straight_len = int((x_dist - y_dist)/2)
            
            if station2.x_pos < station1.x_pos:
                straight_len = -straight_len
                x_angle_len = -x_angle_len

            if station2.y_pos < station1.y_pos:
                y_angle_len = -y_angle_len

            return [
                (station1.x_pos, station1.y_pos), 
                (station1.x_pos + straight_len, station1.y_pos),
                (station1.x_pos + straight_len + x_angle_len, station1.y_pos + y_angle_len),
                (station1.x_pos + straight_len*2 + x_angle_len, station1.y_pos + y_angle_len)
            ]
        
        if y_dist > x_dist:
            x_angle_len = x_dist
            y_angle_len = x_dist
            straight_len = int((y_dist - x_dist)/2)
            
            if station2.y_pos < station1.y_pos:
                straight_len = -straight_len
                y_angle_len = -y_angle_len

            if station2.x_pos < station1.x_pos:
                x_angle_len = -x_angle_len

            return [
                (station1.x_pos, station1.y_pos),
                (station1.x_pos, station1.y_pos + straight_len),
                (station1.x_pos + x_angle_len, station1.y_pos + straight_len + y_angle_len),
                (station1.x_pos + x_angle_len, station1.y_pos + straight_len*2 + y_angle_len)
            ]

        

class Route:
    def __init__(self, stations: list, colour: tuple = (255, 0, 0), loop: bool = False, ghost = False) -> None:
        self.stations = stations
        self.colour = colour
        self.ghost = ghost
        self.gray = (190, 190, 190)
        self.loop = loop
        self.points = []

    
        for s in range(len(stations)):
            if s+1 < len(stations):
                self.points += get_lines(self.stations[s], self.stations[s+1])
                
    def draw(self, screen):
        for l in range(len(self.points)):
            ###the circles give rounded edges to the corners and edges of the lines
            

            if l+1 < len(self.points):
                if self.points[l][0] == self.points[l+1][0] or self.points[l][1] == self.points[l+1][1]:
                    w = 10 #straight width
                    #pygame.draw.circle(screen, self.colour, (self.points[l]), 5)
                else:
                    w = 14 #width on angle
                    #pygame.draw.circle(screen, self.colour, (self.points[l]), 6)
                if self.ghost:
                    pygame.draw.line(screen, self.gray, self.points[l], self.points[l+1], w)
                else:
                    pygame.draw.line(screen, self.colour, self.points[l], self.points[l+1], w)
                   
            if self.loop == True:
                if self.ghost:   
                    pygame.draw.line(screen, self.gray, self.points[len(self.points)-1], self.points[0], 11)
                    pygame.draw.circle(screen, self.gray, (self.points[len(self.points) - 1]), 15)
                    pygame.draw.circle(screen, (255, 255, 255), (self.points[len(self.points) - 1]), 10)
                else:
                    pygame.draw.line(screen, self.colour, self.points[len(self.points)-1], self.points[0], 11)
                    pygame.draw.circle(screen, self.colour, (self.points[len(self.points) - 1]), 15)
                    pygame.draw.circle(screen, (255, 255, 255), (self.points[len(self.points) - 1]), 10)

            if self.ghost:
                pygame.draw.circle(screen, self.gray, (self.points[l]), 15)
                pygame.draw.circle(screen, (255, 255, 255), (self.points[l]), 10)
            else:
                pygame.draw.circle(screen, self.colour, (self.points[l]), 15)
                pygame.draw.circle(screen, (255, 255, 255), (self.points[l]), 10)

    

    def check_overlap(self, route_2) -> list:

        cross_list = []

        for s in range(0, len(self.stations), 2):
            x1 = self.stations[s].x_pos
            y1 = self.stations[s].y_pos
            x1_d = 0
            y1_d = 0

            if s+1 >= len(self.stations):
                continue

            if self.stations[s].x_pos != self.stations[s+1].x_pos and self.stations[s].y_pos != self.stations[s+1].y_pos: #check if straight x
                continue

            if self.stations[s].y_pos < self.stations[s+1].y_pos:
                y1_d = 1
                x1_d = 0   
            elif self.stations[s].y_pos > self.stations[s+1].y_pos:
                y1_d = -1
                x1_d = 0

            if self.stations[s].x_pos < self.stations[s+1].x_pos:
                y1_d = 0
                x1_d = 1   
            elif self.stations[s].x_pos > self.stations[s+1].x_pos:
                y1_d = 0
                x1_d = -1

            for s2 in range(0, len(route_2.stations), 2):
                x2 = route_2.stations[s2].x_pos
                y2 = route_2.stations[s2].y_pos
                x2_d = 0
                y2_d = 0
                 
                if s2+1 >= len(route_2.stations):
                    continue
                 
                if route_2.stations[s2].y_pos != route_2.stations[s2+1].y_pos and route_2.stations[s2].x_pos != route_2.stations[s2+1].x_pos:
                    continue
                
               # print(f"x:{route_2.stations[s2].x_pos}, y: {route_2.stations[s2].y_pos}")
              #  print(f"x2:{route_2.stations[s2+1].x_pos}, y2: {route_2.stations[s2+1].y_pos}")
                if route_2.stations[s2].y_pos < route_2.stations[s2+1].y_pos:
                    y2_d = 1
                    x2_d = 0   
                elif route_2.stations[s2].y_pos > route_2.stations[s2+1].y_pos:
                    y2_d = -1
                    x2_d = 0

                if route_2.stations[s2].x_pos < route_2.stations[s2+1].x_pos:
                    y2_d = 0
                    x2_d = 1   
                elif route_2.stations[s2].x_pos > route_2.stations[s2+1].x_pos:
                    y2_d = 0
                    x2_d = -1

                


                c1 = 0
                while x1 != self.stations[s+1].x_pos or y1 != self.stations[s+1].y_pos:
                    x2 = route_2.stations[s2].x_pos
                    y2 = route_2.stations[s2].y_pos
                    if c1 > 300:
                        break
                    c1 += 1
                    
                    c2 = 0
                    print(f"d x: {x1}, y: {y1}\n")
                    while x2 != route_2.stations[s2+1].x_pos or y2 != route_2.stations[s2+1].y_pos:
                        if c2 > 300:
                            break
                        c2 += 1
                        if x1 == x2 and y1 == y2:
                            cross = (x1, y1)
                            cross_list.append(cross)
                            return cross_list

                        x2 += x2_d
                        y2 += y2_d

                    x1 += x1_d
                    y1 += y1_d

    
        return cross_list


                        




        