import pygame

GAME_SCREEN_WIDTH  = 600
GAME_SCREEN_HEIGHT = 700

SQUARE_SIZE = 20

BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREY = (232, 232, 232)

class Renderer:
    surface = pygame.display.set_mode((GAME_SCREEN_WIDTH,  GAME_SCREEN_HEIGHT))
    
    def render_to_string(self, template):
        string_representation = ''
        
        for row in range(len(template)):
            for col in range(len(template[row])):
                string_representation += ('.' if template[row][col] == 0 else '*')
            string_representation += '\n'
            
        return string_representation
    
    def render(self, template, screen_x = 0, screen_y = 0):
        self.surface.fill(WHITE)
        
        for row in range(len(template)):
            for col in range(len(template[row])):
                x0 = screen_x + col * SQUARE_SIZE + 1
                y0 = screen_y + row * SQUARE_SIZE + 1
                if template[row] [col] == 1:
                    pygame.draw.rect(self.surface, BLUE, (x0, y0, SQUARE_SIZE - 2, SQUARE_SIZE - 2))
                else:
                    pygame.draw.rect(self.surface, GREY, (x0, y0, SQUARE_SIZE - 2, SQUARE_SIZE - 2))
        pygame.display.update()