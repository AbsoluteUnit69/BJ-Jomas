import pygame

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
        pos1 = None
        while run:

            self.screen_rect.fill((100, 100, 100))

            for b in self.blocks:
                b.display(self.screen_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos1 = pygame.mouse.get_pos()
                    pos1 = self.get_closest(pos1)
                if event.type == pygame.MOUSEBUTTONUP:
                    if width*height > 100:
                        self.blocks.append(Block((128, 0, 0), width, height, top_left))
                    pos1 = None

            pos2 = pygame.mouse.get_pos()
            pos2 = self.get_closest(pos2)

            if pos1 is not None:
                top_left = (min(pos1[0], pos2[0]), min(pos1[1], pos2[1]))
                bottom_left = (max(pos1[0], pos2[0]), max(pos1[1], pos2[1]))
                width = abs(top_left[0] - bottom_left[0])
                height = abs(top_left[1] - bottom_left[1])
                new_rect = pygame.Rect(top_left[0], top_left[1], width, height)
                pygame.draw.rect(self.screen_rect, (0, 100, 100), new_rect)

            for pos in self.line_pos_y:
                pygame.draw.line(self.screen_rect, (0, 0, 0), pos, (pos[0], 540))
            
            for pos in self.line_pos_x:
                pygame.draw.line(self.screen_rect, (0, 0, 0), pos, (960, pos[1]))

            self.screen.update()

m = Map_maker()