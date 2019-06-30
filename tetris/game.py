import pygame, sys
from pygame.locals import *
from renderer import *
from board import *

TICK_TIMER_EVENT_ID = USEREVENT+1
TIMER_INTERVAL_MS = 10




#  Space  - fall
#  1..6   - change shape
#  Enter  - restart
#  Up     - rotate
#  Left, Right, Down - move shape
#  Esc    - exit
class Game:
    game_over = True
    is_falling = False
    board = None
    renderer = None
    tick_counter = 0
    speed = 80
    
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.renderer = Renderer()
        pygame.time.set_timer(TICK_TIMER_EVENT_ID, TIMER_INTERVAL_MS)
        self.renderer.render(self.board.game_board)
        
    def new_game(self):
         self.board.new_game()
         self.game_over = False
         self.is_falling = False
                     
    def terminate(self):
        pygame.time.set_timer(TICK_TIMER_EVENT_ID, 0)#to end the program
        pygame.quit()
        sys.exit()
        
        
    def run(self):
        self.new_game()
        while True:
            for event in pygame.event.get():
                self.event_handler(event)
                    
        
    def event_handler(self, event):
        if event.type == QUIT:
            self.terminate()

        if event.type == pygame.KEYDOWN:
            self.process_key_event(event)
            
        if event.type == TICK_TIMER_EVENT_ID:
            self.process_timer_event(event)
        
        
    def process_key_event(self, event):
        if event.key == pygame.K_ESCAPE:
            self.terminate()
                
        if event.key == K_UP:
            if self.board.rotate_shape_clockwise():
                self.renderer.render(self.board.game_board)

        elif event.key == K_DOWN:
            if self.board.move_shape_down():
                self.renderer.render(self.board.game_board)
            
        elif event.key == K_RIGHT:
            if self.board.move_shape_right():
                self.renderer.render(self.board.game_board)

        elif event.key == K_LEFT:
            if self.board.move_shape_left():
                self.renderer.render(self.board.game_board)
                
        elif event.key == K_SPACE:
            self.is_falling = True

        elif event.key == K_RETURN:
            self.new_game()
                
        elif event.key >= 49 and event.key <= 57:
            shape_index = event.key - 49
            if self.board.change_shape(shape_index):
                self.renderer.render(self.board.game_board)



    def process_timer_event(self, event):
        if self.game_over:
            return
        self.tick_counter += 1
        if self.tick_counter >= self.speed or self.is_falling:
            self.tick_counter = 0
            if not self.board.move_shape_down():
                self.is_falling = False
                if not self.board.next_shape():
                    self.game_over = True
            self.renderer.render(self.board.game_board)