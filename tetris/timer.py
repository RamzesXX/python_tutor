import pygame

NUMBER_SIZE = 20
LINE_THICKNESS = 2
LINE_SPACE = 1
LINE_LENGHT = NUMBER_SIZE - 2 * (LINE_THICKNESS + LINE_SPACE)
TIMER_TOP = 999

BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LED_COLOR = RED
BACKGROUND_COLOR = BLACK


NUMBERS_LED_SEGMENTS =[
        [0, 1, 2, 4, 5, 6],
        [2, 5],
        [0, 2, 3, 4, 6],
        [0, 2, 3, 5, 6],
        [1, 3, 2, 5],
        [0, 1, 3, 5, 6],
        [0, 1, 3, 4, 5, 6],
        [0, 2, 5],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 5, 6]       
        
]
LED_SEGMENT_X = [
    [LINE_THICKNESS + LINE_SPACE - 1, LINE_LENGHT],
    [0, LINE_THICKNESS],
    [NUMBER_SIZE - LINE_THICKNESS - 1, LINE_THICKNESS],
    [LINE_THICKNESS + LINE_SPACE - 1, LINE_LENGHT],
    [0, LINE_THICKNESS],
    [NUMBER_SIZE - LINE_THICKNESS - 1, LINE_THICKNESS],
    [LINE_THICKNESS + LINE_SPACE - 1, LINE_LENGHT]
]
LED_SEGMENT_Y = [
    [0, LINE_THICKNESS],
    [LINE_THICKNESS + LINE_SPACE - 1, LINE_LENGHT],
    [LINE_THICKNESS + LINE_SPACE - 1, LINE_LENGHT],
    [2 * LINE_SPACE + LINE_LENGHT + LINE_THICKNESS - 1, LINE_THICKNESS],
    [3 * LINE_SPACE + LINE_LENGHT + 2 * LINE_THICKNESS - 1, LINE_LENGHT],
    [3 * LINE_SPACE + LINE_LENGHT + 2 * LINE_THICKNESS - 1, LINE_LENGHT],
    [4 * LINE_SPACE + 2 * LINE_LENGHT + 2 * LINE_THICKNESS - 1, LINE_THICKNESS]
]

def number_digts(number):
    n = len(str(number))
    return n

class Digit:
   
    def __init__(self, surface):
        self.surface = surface
    
    def draw(self, digit, x, y):
        
        for segment in NUMBERS_LED_SEGMENTS[digit]:
            pygame.draw.rect(self.surface, LED_COLOR, (x + LED_SEGMENT_X[segment][0], y + LED_SEGMENT_Y[segment][0], \
                                                   LED_SEGMENT_X[segment][1], LED_SEGMENT_Y[segment][1]))


class Timer:

    def __init__(self, timer_goal, surface):
        self.surface = surface
        self.timer_goal = TIMER_TOP if timer_goal > TIMER_TOP else timer_goal
        self.digits = [Digit(surface) for r in range(len(str(self.timer_goal)))]
        self.reset()       

    def reset(self):
        self.counter = 0
        self.is_running = False   
    
    def tick(self):
        if self.is_running:
            self.counter += 1
            if self.counter >= self.timer_goal:
                self.stop()
        self.draw()
                         
    def start(self):
        self.is_running = True
        
    def stop(self):
        self.is_running = False   

    def draw(self):
        self.surface.fill(BACKGROUND_COLOR)
        tmp_counter = self.counter
        for i in range (len(self.digits)):
            self.digits[i].draw(tmp_counter % 10, (len(self.digits)- i - 1) * NUMBER_SIZE, 0)
            tmp_counter //= 10
        pygame.display.update()

        
        
        
#        self.tick_counter += 1
#        
#        if self.tick_counter % self.speed == 0:
#            count += 1
#            self.draw_digit(count)
#        pygame.display.update()

count = 0
pygame.init()
surface = pygame.display.set_mode((100,  100))
t = Timer(234876, surface)
clock1 = pygame.time.Clock()
t.start()
while True:
    clock1.tick(100)
    t.tick()
    
