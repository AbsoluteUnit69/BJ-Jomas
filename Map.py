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
        self.screen_rect = self.screen.set_mode((700, 500))
        self.blocks = []
        positions = [[(0, 480), 700, 20], [(200, 250), 150, 20]]
        for pos in positions:
            self.blocks.append(Block((128, 0, 0), pos[1], pos[2], (pos[0])))
        self.start_loop()

    def start_loop(self):
        run = True
        pos1 = None
        while run:

            self.screen_rect.fill((100, 100, 100))

            pos2 = pygame.mouse.get_pos()

            for b in self.blocks:
                b.display(self.screen_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos1 = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    if width*height > 100:
                        self.blocks.append(Block((128, 0, 0), width, height, top_left))
                    pos1 = None

            pos2 = pygame.mouse.get_pos()

            if pos1 is not None:
                top_left = (min(pos1[0], pos2[0]), min(pos1[1], pos2[1]))
                bottom_left = (max(pos1[0], pos2[0]), max(pos1[1], pos2[1]))
                width = abs(top_left[0] - bottom_left[0])
                height = abs(top_left[1] - bottom_left[1])
                new_rect = pygame.Rect(top_left[0], top_left[1], width, height)
                pygame.draw.rect(self.screen_rect, (0, 100, 100), new_rect)

            self.screen.update()

m = Map_maker()