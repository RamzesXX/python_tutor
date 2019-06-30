SHAPE_BLUEPRINTS = [
    [
        [0, 1, 0],
        [1, 1, 1]
    ],
    
    [
        [1, 1, 1, 1, 1]
    ],
    
    [
        [1, 1, 0],
        [0, 1, 1],
    ],
    
    [
        [0, 1, 1],
        [1, 1, 0],
    ],
    
    [
        [1, 1],
        [1, 1],
    ],
    
    [
        [1, 1, 1],
        [1, 0, 0],
    ],
    
    [
        [1, 1, 1],
        [0, 0, 1],
    ]
    
]

class Shape:
    angle = 0
    color = 1
    blueprint = []
    
    def __init__(self, blueprint_index = 0, color = 1):
        self.blueprint = SHAPE_BLUEPRINTS[blueprint_index]
        self.color = color
        
    def rotate_clockwise(self):
        self.angle = (self.angle + 1) % 4
        
    def rotate_counterclockwise(self):
        self.angle = (self.angle + 3) % 4
        
        
    def get_rotated_blueprint(self):
        rotated_bluprint = []
        size_y = len(self.blueprint)
        size_x = len(self.blueprint[0])
        
        if self.angle == 0:
            rotated_bluprint = [ [self.blueprint[y][x] for x in range(size_x)] for y in range(size_y) ]
        elif self.angle == 1:
            rotated_bluprint = [ [self.blueprint[size_y - 1 - x][y] for x in range(size_y)] for y in range(size_x) ]
        elif self.angle == 2:
            rotated_bluprint = [ [self.blueprint[size_y - 1 - y][size_x - 1 - x] for x in range(size_x)] for y in range(size_y) ]
        elif self.angle == 3:
            rotated_bluprint = [ [self.blueprint[x][size_x - 1 - y] for x in range(size_y)] for y in range(size_x) ]
            
        return rotated_bluprint
