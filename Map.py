import pygame
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
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, position):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.rect = self.image.get_rect()
       self.rect.topleft = position
    
    def display(self, screen):
        screen.blit(self.image, (self.rect.topleft))

class Map_maker():
    def __init__(self):
        self.screen = pygame.display
        self.screen_rect = self.screen.set_mode((960, 540))
        self.blocks = []
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
        while run:

            self.screen_rect.fill((100, 100, 100))

            for b in self.blocks:
                b.display(self.screen_rect)

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
                            self.blocks.append(Block((128, 0, 0), width, height, top_left))
                        self.pos1 = None
                    if self.mode == "lever":
                        self.interactables.append(Block((0, 50, 110), 24, 24, self.pos1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        undo = True
                    if event.key == pygame.K_z and undo:
                        if self.mode == "rect":
                            if len(self.blocks) > 0:
                                self.blocks.pop()
                        elif self.mode == "lever":
                            if len(self.interactables) > 0:
                                self.interactables.pop()
                    if event.key == pygame.K_l:
                        self.mode = "lever"
                    if event.key == pygame.K_r:
                        self.mode = "rect"
                        self.pos1 = None
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

            self.screen.update()

m = Map_maker()