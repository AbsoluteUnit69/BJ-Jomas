import pygame
import sys
import random

class KeyFunctions:
    @staticmethod
    def loadFile(filename):
        array_of_file_lines = []
        filename = str(filename)
        file = open(filename,"r")
        for line in file:
            x = line.replace("\n","")
            array_of_file_lines.append(x)
        return array_of_file_lines
    @staticmethod
    def writeText(surface,text,border = 0,max_size=72,text_colour = (0,0,0),type = "left"):#returns the lines, and the font / font size
        if max_size < 8:
            print("too small a font size ")
            return None
        size_array = [72,48,36,28,26,24,22,20,18,16,14,12,11,10,9,8]
        surface_width = int(surface.get_width() - border * 2)
        surface_height = int(surface.get_height()-border * 2)
        for size in range(len(size_array)):
            if max_size <size_array[size]:
                pass
            else:

                array_of_lines = []
                removed_stuff = []
                comicsans = pygame.font.SysFont("comicsansms", size_array[size])
                sentence = text
                height_of_line  = comicsans.size(sentence)[1]
                play = True
                loop = 0
                while play:
                    loop+=1
                    width = comicsans.size(sentence)[0]
                    if width>= surface_width:#if the entire sentence falls off of the surface
                        split_sentence = sentence.rsplit(' ', 1)
                        if len(split_sentence) == 1:#if the first word by itself doesnt fit on the screen, go to a smaller font
                            play = False
                        else:
                            removed_stuff.insert(0,split_sentence[1])
                            sentence = split_sentence[0]
                    else:
                        array_of_lines.append(sentence)
                        if len(removed_stuff) == 0:
                            play = False
                        else:
                            sentence = removed_stuff[0]
                            for i in range(1,len(removed_stuff)):
                                sentence = sentence + " " + str(removed_stuff[i])
                            removed_stuff = []
                height_needed = int(len(array_of_lines) * height_of_line)
                if height_needed < surface_height:
                    break
        
        for line_num in range(len(array_of_lines)):
            line_to_write = comicsans.render(array_of_lines[line_num],1,text_colour)
            if type == "centre":
                line_rect = line_to_write.get_rect(center = (int(surface_width/2 + border),int(height_of_line * line_num + border + height_of_line/2)))
                surface.blit(line_to_write,line_rect)
            else:
                surface.blit(line_to_write,(border,int(height_of_line * line_num + border)))

    @staticmethod
    def outputText(screen,image,text,name = "???",colour = (0,0,0)):#remove object and just give it the image and name
        HEIGHT = screen.get_height()
        WIDTH = screen.get_width()
        clock = pygame.time.Clock()
        FPS = 60

        top_start = int(HEIGHT/2 + HEIGHT/12)
        x = WIDTH
        y = (int(HEIGHT/8 * 3))
        l_border = (int(HEIGHT/24))
        s_border =  int(1/30 * y)
        z = int(x-int(2*l_border)-int(3*s_border))

        image_width = int(z/5)
        name_width = text_width = int(4*z/5)
        image_height = int(y-2*s_border)
        name_height = int(3*y/10)
        text_height = int(6*y/10)

        try:#if the user passed in a surface
            image = pygame.transform.scale(image,(image_width,image_height))
        except:#if the user passed in a directory
            image = pygame.transform.scale(pygame.image.load(image),(image_width,image_height))        

        background_surface = pygame.Surface((int(x-2*l_border),int(y))).convert_alpha()
        background_surface.fill((0,0,0))

        image_surface = pygame.Surface(((int(image_width),int(image_height)))).convert_alpha()
        image_surface.blit(image,(0,0))

        name_surface = pygame.Surface(((int(name_width),int(name_height)))).convert_alpha()
        name_surface.fill((180,180,180))
        KeyFunctions.writeText(name_surface,str(name),10)

        text_surface = pygame.Surface(((int(text_width),int(text_height)))).convert_alpha()
        text_surface.fill((200,200,200))
        line_completed = False
        line = text[0]
        letter = 0
        count = 0
        play = True
        while play:
            if count == 5 and not (line_completed):
                count = 0
                letter +=1
                if letter== len(text)-1:
                    line_completed = True
                line += text[letter]
                text_surface.fill((200,200,200))
                KeyFunctions.writeText(text_surface,line,10,36,colour)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if line_completed:
                        return
                    else:
                        line = text
                        text_surface.fill((200,200,200))
                        KeyFunctions.writeText(text_surface,line,10,36,colour)
                        line_completed = True
            screen.blit(background_surface,(l_border,top_start))
            screen.blit(image_surface,(int(l_border + s_border),int(top_start + s_border)))
            screen.blit(name_surface,(int(l_border + image_width +   2*s_border),int(top_start + s_border)))
            screen.blit(text_surface,(int(l_border + image_width +   2*s_border),int(top_start + 2 * s_border +name_height)))
            pygame.display.flip()
            clock.tick(FPS)
            count+=1
    @staticmethod
    def getRandomSelectionOf(array,number_of_selections):
        returned_array = []
        for i in range(0,number_of_selections):
            returned_array.append(array[random.randint(0,len(array)-1)])
        return returned_array