import pygame

pygame.font.init()

class Button:
    def __init__(self, x, y, width, height, colour, border_colour, surface, option):
        self.surface = surface
        
        self.colour = colour
        self.border_colour = border_colour
        
        self.rect = pygame.Rect((x + 5, y + 5), (width - 10, height - 10))
        self.border_rect = pygame.Rect((x, y), (width, height))
        
        self.center = self.rect.center
        
        self.option = option
        
        temp_option = str(self.option).replace("_", " ")

        self.font = pygame.font.SysFont('Arial', 25)
        
        self.text = self.font.render(temp_option, True, (0,0,0))

        self.text_rect = self.text.get_rect(center = self.center)
        
    def draw(self, edge_roundness = 10, with_text = True):
        pygame.draw.rect(self.surface, self.border_colour, self.border_rect, 0, edge_roundness, edge_roundness, edge_roundness, edge_roundness)
        pygame.draw.rect(self.surface, self.colour, self.rect, 0, edge_roundness, edge_roundness, edge_roundness, edge_roundness)
        if with_text:
            self.surface.blit(self.text, self.text_rect)
        
    def get_topleft(self):
        return self.rect.topleft
    
    def get_center(self):
        return list(self.rect.center)

    def set_colour(self, colour, border_colour):
        self.colour = colour
        self.border_colour = border_colour        

    def is_button_pressed(self, pos_of_surface = (0, 0)):
        action = False
        
        pos = [0, 0]
        
        pos[0] += pygame.mouse.get_pos()[0] - pos_of_surface[0]
        pos[1] += pygame.mouse.get_pos()[1] - pos_of_surface[1]

        
        if self.border_rect.collidepoint(pos):                  
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
                
        return action
    
    def get_option(self):
        return self.option