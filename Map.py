import pygame
import copy
from Button import Button
'''
Conrtols:
r for rectangle mode:
    mouse button down for position 1
    mouse button up for position 2
    rectangle will be drawn between the two
l for lever mode:
    no grid snapping first mouse button up will place the lever where the mouse is

control z will undo the last block placed in the mode you are in

'''
class Map(pygame.sprite.Sprite):
    def __init__(self, timed_platforms, levers):
        pygame.sprite.Sprite.__init__(self)
        self.timed_platforms = timed_platforms
        self.levers = levers
        self.active_time = 0
        self.activated_levers = []

    def getMapState(self):
        return self.active_time

    def display(self, screen_rect):
        for block in maps[index].timed_platforms[selected_time]:
            block.display(screen_rect)
        for lever in maps[index].levers:
            lever.display(screen_rect)

    def getTimedPlatforms(self):
        return self.timed_platforms

    def getLevers(self):
        return self.levers
    
    def checkCollisions(self, rect):
        colliding = False
        for platform in self.timed_platforms[self.active_time]:
            colliding = platform.checkCollide(rect)
            if colliding == True:
                return True

    def checkInteractions(self, rect):
        colliding = False
        for lever in self.levers:
            colliding = lever.checkCollide(rect)
            if colliding == True:
                if lever.flick():
                    self.activated_levers.append(lever.getTime())
                    self.active_time = lever.getTime()
                else:
                    self.activated_levers.remove(lever.getTime())
                    self.active_time = self.activated_levers[-1]
                return True

class Block(pygame.sprite.Sprite):
    def __init__(self, image_code, width, height, position, time):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([width, height])
       self.image.fill(image_code)
       self.image_code = image_code
       self.rect = self.image.get_rect()
       self.rect.topleft = position
       self.time = time
    
    def display(self, screen):
        screen.blit(self.image, (self.rect.topleft))

    def getText(self):
        text = str(self.image_code) + "." + str(self.rect.width) + "." + str(self.rect.height) + "." + str(self.rect.topleft[0]) + "." + str(self.rect.topleft[1]) + "." + str(self.time)
        return text

    def checkCollide(self, rect):
        return self.rect.colliderect(rect)

    def getTime(self):
        return self.time

    def display_grey(self, screen):
        pygame.draw.rect(screen, (120, 120, 120, 50), self.rect) # remove after map created

class Lever(Block):
    def __init__(self, image_code, width, height, position, time):
        Block.__init__(self, image_code, width, height, position, time)
        self.activated = False

    def flick(self):
        self.activated = not(self.activated)
        return self.activated

class Platform(Block):
    def __init__(self, image_code, width, height, position, time,  co_friction = 1):
        Block.__init__(self, image_code, width, height, position, time)
        self.co_friction = co_friction

    def getCoFriction(self):
        return self.co_friction

    def getText(self):
        text = str(self.image_code) + "." + str(self.rect.width) + "." + str(self.rect.height) + "." + str(self.rect.topleft[0]) + "." + str(self.rect.topleft[1]) + "." + str(self.time) + "." + str(self.co_friction)
        return text

class Map_maker():
    def __init__(self):
        self.screen = pygame.display
        self.screen_rect = self.screen.set_mode((960, 540))
        self.time_blocks = {}
        self.points = []
        for row in range(0, 960, 12):
            for column in range(0, 540, 12):
                self.points.append((row, column))
        self.line_pos_y = []
        for i in range(0, 960, 12):
            self.line_pos_y.append((i, 0))
        self.line_pos_x = []
        for i in range(0, 540, 12):
            self.line_pos_x.append((0, i))
        self.mode = "rect"
        self.interactables = []
        self.time_buttons = [Button(0, 0, 32, 32,(50, 100, 120), (50, 50, 50), self.screen_rect, 0)]
        self.start_loop()

    def get_closest(self, pos):
        x_twelves = pos[0]//12
        if (pos[0]%12) >= 6:
            x_twelves += 1
        y_twelves = pos[1]//12
        if (pos[1]%12) >= 6:
            y_twelves += 1
        return ((x_twelves*12),(y_twelves*12))

    def start_loop(self):
        run = True
        self.pos1 = None
        undo = False
        selected_time = 0
        co_friction = 1
        while run:

            self.screen_rect.fill((100, 100, 100))
            for time in self.time_blocks:
                if time == selected_time:
                    for block in self.time_blocks[time]:
                        block.display(self.screen_rect)
                elif time == (selected_time - 1):
                    for block in self.time_blocks[time]:
                        block.display_grey(self.screen_rect)

            for i in self.interactables:
                i.display(self.screen_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos1 = pygame.mouse.get_pos()
                    self.pos1 = self.get_closest(self.pos1)
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.mode == "rect":
                        if width*height > 100:
                            if selected_time in self.time_blocks.keys():
                                self.time_blocks[selected_time].append(Platform((128, 0, 0), width, height, top_left, selected_time, co_friction))
                            else:
                                self.time_blocks[selected_time] = [(Platform((128, 0, 0), width, height, top_left, selected_time, co_friction))]
                        self.pos1 = None
                    if self.mode == "lever":
                        temp = Lever((0, 50, 110), 24, 24, self.pos1, len(self.time_buttons))
                        font = pygame.font.SysFont(None, 24)
                        img = font.render(str(len(self.interactables) + 1), True, (0, 0, 0))
                        temp.image.blit(img, (7, 5))
                        self.interactables.append(temp)

                        self.time_buttons.append(Button(self.time_buttons[-1].rect.topleft[0] + 32, 0, 32, 32,(50, 100, 120), (50, 50, 50), self.screen_rect, self.time_buttons[-1].option + 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        undo = True
                        save = True
                    if event.key == pygame.K_z and undo:
                        if self.mode == "rect":
                            try:
                                self.time_blocks[selected_time].pop()
                            except:
                                pass
                        elif self.mode == "lever":
                            if len(self.interactables) > 0:
                                self.interactables.pop()
                                self.time_buttons.pop()
                        undo = False
                        save = False
                    if event.key == pygame.K_s and save == True:
                        save = False
                        undo = False
                        self.saveMap()
                    if event.key == pygame.K_l:
                        self.mode = "lever"
                    if event.key == pygame.K_r:
                        self.mode = "rect"
                        self.pos1 = None
                    if event.key == pygame.K_c:
                        try:
                            for block in self.time_blocks[selected_time - 1]:
                                try:
                                    temp = copy.copy(block)
                                    temp.time += 1
                                    self.time_blocks[selected_time].append(temp)
                                except:
                                    self.time_blocks[selected_time] = [temp]
                        except:
                            pass
                        
                if event.type == pygame.KEYUP:
                    if event == pygame.K_LCTRL:
                        undo = False

            pos2 = pygame.mouse.get_pos()
            pos2 = self.get_closest(pos2)

            if self.pos1 is not None and self.mode == "rect":
                top_left = (min(self.pos1[0], pos2[0]), min(self.pos1[1], pos2[1]))
                bottom_left = (max(self.pos1[0], pos2[0]), max(self.pos1[1], pos2[1]))
                width = abs(top_left[0] - bottom_left[0])
                height = abs(top_left[1] - bottom_left[1])
                new_rect = pygame.Rect(top_left[0], top_left[1], width, height)
                pygame.draw.rect(self.screen_rect, (0, 100, 100), new_rect)

            if self.mode == "lever":
                self.pos1 = pygame.mouse.get_pos()
                new_rect = pygame.Rect(self.pos1[0], self.pos1[1], 24, 24)
                pygame.draw.rect(self.screen_rect, (0, 50, 110), new_rect)

            for pos in self.line_pos_y:
                pygame.draw.line(self.screen_rect, (0, 0, 0), pos, (pos[0], 540))
            
            for pos in self.line_pos_x:
                pygame.draw.line(self.screen_rect, (0, 0, 0), pos, (960, pos[1]))

            for button in self.time_buttons:
                button.draw()
                if button.is_button_pressed():
                    selected_time = button.get_option()

            self.screen.update()

    def saveMap(self):
        lines = []
        for time in self.time_blocks:
            line = []
            for platform in self.time_blocks[time]:
                text = platform.getText()
                line.append(text)
            lines.append(line)
        lines2 = []
        for lever in self.interactables:
            text = lever.getText()
            lines2.append(text)
        with open("maps.txt", "a") as f:
            for line in lines:
                for sub_line in line:
                    f.write(sub_line)
                    f.write("&")
            f.write("\n")
            for line in lines2:
                f.write(line)
                f.write("&")
            f.write("\n")
        f.close
    
def loadMaps():
    maps = []
    with open("maps.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            levers = []
            platforms = {}
            lines[i] = lines[i].strip("\n")
            platform_info = lines[i].split("&")
            platform_info.pop()
            for platform in platform_info:
                platform = platform.split(".")
                temp = ((platform[0].strip("(")).strip(")")).split(",")
                for j in range(0, len(temp)):
                    temp[j] = temp[j].strip(" ")
                code = (int(temp[0]), int(temp[1]), int(temp[2]))
                if not int(platform[5]) in platforms:
                    platforms[int(platform[5])] = [Platform(code, int(platform[1]), int(platform[2]), (int(platform[3]), int(platform[4])), int(platform[5]), int(platform[6]))]
                else:
                    platforms[int(platform[5])].append(Platform(code, int(platform[1]), int(platform[2]), (int(platform[3]), int(platform[4])), int(platform[5]), int(platform[6])))

            lines[i+1] = lines[i+1].strip("\n")
            lever_info = lines[i+1].split("&")
            lever_info.pop()
            for lever in lever_info:
                lever = lever.split(".")
                temp = ((lever[0].strip("(")).strip(")")).split(",")
                for j in range(0, len(temp)):
                    temp[j] = temp[j].strip(" ")
                code = (int(temp[0]), int(temp[1]), int(temp[2]))
                levers.append(Lever(code, int(lever[1]), int(lever[2]), (int(lever[3]), int(lever[4])), int(lever[5])))

            maps.append(Map(platforms, levers))
        return maps
m = Map_maker()



maps = loadMaps()

screen = pygame.display
screen_rect = screen.set_mode((960, 540))

index = 0
run = True
selected_time = 0
while run:
    screen_rect.fill((100, 100, 100))
    for block in maps[index].timed_platforms[selected_time]:
        block.display(screen_rect)
    for lever in maps[index].levers:
        lever.display(screen_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                index += 1
                selected_time = 0
                if index == len(maps):
                    index = 0
            if event.key == pygame.K_m:
                selected_time += 1
                if selected_time == len(maps[index].timed_platforms.keys()):
                    selected_time = 0
    screen.update()