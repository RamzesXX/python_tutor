from shape import *

BOARD_SIZE_X = 12
BOARD_SIZE_Y = 22

class Board:
    shape = Shape()
    shape_x = int(BOARD_SIZE_X / 2) -2
    shape_y = 0
    shape_index = 0
    
    game_board = []
    board_size_x = BOARD_SIZE_X
    board_size_y = BOARD_SIZE_Y
    
    is_shape_on_board = False
                   
    def __init__(self, init_shape = 0, board_size_x = BOARD_SIZE_X, board_size_y = BOARD_SIZE_Y):
        self.board_size_x = board_size_x
        self.new_game()
        
    def new_game(self):
        self.shape_x = int(BOARD_SIZE_X / 2) -2
        self.shape_y = 0
        self.game_board = [ [0 for c in range(self.board_size_x)] for r in range(self.board_size_y) ]
        self.next_shape()
        
        
    # add the shape to the board      
    def put_shape(self):
        if self.is_shape_on_board:
            return
        
        rotated_blueprint = self.shape.get_rotated_blueprint()
        for row in range(len(rotated_blueprint)):
            for col in range(len(rotated_blueprint[row])):
                if rotated_blueprint[row][col] != 0:
                    self.game_board[self.shape_y + row][self.shape_x + col] = self.shape.color
                    
        self.is_shape_on_board = True
    
    
    # take the shape off the board        
    def take_shape(self):
        if not self.is_shape_on_board:
            return
        
        rotated_blueprint = self.shape.get_rotated_blueprint()
        for row in range(len(rotated_blueprint)):
            for col in range(len(rotated_blueprint[row])):
                if rotated_blueprint[row][col] != 0:
                    self.game_board[self.shape_y + row][self.shape_x + col] = 0
                    
        self.is_shape_on_board = False     
    
    
    # check if it is allowed to put shape at the coordinates    
    def can_put_at(self, x, y, shape):
        if x < 0 or y < 0:
            return False

        rotated_blueprint = shape.get_rotated_blueprint()
        for row in range(len(rotated_blueprint)):
            for col in range(len(rotated_blueprint[row])):
                if rotated_blueprint[row][col] != 0:
                    if (y + row > self.board_size_y - 1) or \
                       (x + col > self.board_size_x - 1) or \
                       (self.game_board[y + row][x + col] != 0):
                        return False
        return True
    
        
    def rotate_shape_clockwise(self):
        is_board_updated = True
        self.take_shape()
        self.shape.rotate_clockwise()
        if not self.can_put_at(self.shape_x, self.shape_y, self.shape):
            self.shape.rotate_counterclockwise()
            is_board_updated = False
        self.put_shape()
        
        return is_board_updated
            
        
    def rotate_shape_counterclockwise(self):
        is_board_updated = True
        self.take_shape()
        self.shape.rotate_counterclockwise()
        if not self.can_put_at(self.shape_x, self.shape_y, self.shape):
            self.shape.rotate_shape_clockwise()
            is_board_updated = False
        self.put_shape()
        
        return is_board_updated
        
        
    def move_shape_to(self, new_shape_x, new_shape_y):
        is_board_updated = True
        self.take_shape()
        
        if self.can_put_at(new_shape_x, new_shape_y, self.shape):
            self.shape_x = new_shape_x;
            self.shape_y = new_shape_y;
        else:
            is_board_updated = False
        
        self.put_shape()
        
        return is_board_updated;
        
        
    def move_shape_right(self):
        new_shape_x = self.shape_x + 1
        new_shape_y = self.shape_y
        
        return self.move_shape_to(new_shape_x, new_shape_y)
    
            
    def move_shape_left(self):
        new_shape_x = self.shape_x - 1
        new_shape_y = self.shape_y
        
        return self.move_shape_to(new_shape_x, new_shape_y)
            
               
    def move_shape_up(self):
        new_shape_x = self.shape_x
        new_shape_y = self.shape_y - 1
        
        return self.move_shape_to(new_shape_x, new_shape_y)
    
            
    def move_shape_down(self):
        new_shape_x = self.shape_x
        new_shape_y = self.shape_y + 1
        
        return self.move_shape_to(new_shape_x, new_shape_y)
      
      
    def change_shape(self, shape_index):
        is_board_updated = False
        
        if shape_index < 0 or shape_index >= len(SHAPE_BLUEPRINTS):
            return is_board_updated
        
        old_shape = self.shape
        new_shape = Shape(shape_index)

        self.take_shape()
        if self.can_put_at(self.shape_x, self.shape_y, new_shape):
            self.shape = new_shape 
            is_board_updated = True
        self.put_shape()
        
        return is_board_updated
        
    def next_shape(self):
        is_board_updated = False
        
        self.remove_full_rows()
        
        self.shape_x = int(BOARD_SIZE_X / 2) -2;
        self.shape_y = 0;
        self.shape_index += 1
        self.shape_index %= len(SHAPE_BLUEPRINTS)
        new_shape = Shape(self.shape_index)

        
        if self.can_put_at(self.shape_x, self.shape_y, new_shape):
            self.shape = new_shape 
            self.put_shape()
            is_board_updated = True
        
        return is_board_updated
    
    def remove_full_rows(self):
        line_from = self.shape_y
        line_to = line_from + len(self.shape.get_rotated_blueprint())
        for line in range(line_from, line_to):
           if self.is_line_full(line):
                self.game_board.pop(line)
                self.game_board.insert(0, [0 for c in range(self.board_size_x)])
                
    def is_line_full(self, line):
        
        for i in self.game_board[line]:
            if i == 0:
                return False
        return True