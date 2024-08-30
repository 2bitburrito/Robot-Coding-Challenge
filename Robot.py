"""
Robot Class

Initialises a robot object and provides methods to place, move, turn and report the robot's position and direction
"""

class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.move_amount = 1
        self.robot_has_been_placed = False
        self.direction_list = ['NORTH','EAST','SOUTH','WEST']
    
    def place(self,table,x=0,y=0,direction="NORTH"):
        direction = self.fix_direction_string(direction)
        if self.position_is_valid(table,x,y) and direction in self.direction_list:
            self.x = x
            self.y = y
            self.direction = direction
            self.robot_has_been_placed = True
        else:
            raise Exception('ERROR: Please ensure the position and direction are valid')
            
    def move(self,table):
        if self.robot_has_been_placed == False:
            raise Exception("ERROR: Please place the robot first!")
        elif table.check_for_edge(self.direction,self):
            raise Exception("ERROR: Cannot move off the table")
        
        if self.direction == "NORTH":
            self.y += self.move_amount    
        elif self.direction == "SOUTH":
            self.y -= self.move_amount  
        elif self.direction == "EAST":
            self.x += self.move_amount 
        elif self.direction == "WEST":
            self.x -= self.move_amount

    
    def turn(self,new_direction):
        current_direction_index = self.direction_list.index(self.direction)
        if new_direction == "LEFT":
            new_index = (current_direction_index - 1) % len(self.direction_list)
        elif new_direction == "RIGHT":
            new_index = (current_direction_index + 1) % len(self.direction_list)
        self.direction = self.direction_list[new_index]
        return self.direction

    def position_is_valid(self,table,x,y):
        if type(x) != int or type(y) != int:
            raise Exception('ERROR: Please ensure both indicies are a valid number')
        elif x not in table.x_grid or y not in table.y_grid:
            raise Exception('ERROR: Given indices are outside the range of the table')
        else:
            return True
            
    def fix_direction_string(self,direction):
        direction = direction.upper()
        if  direction == "N":
            direction = "NORTH"
        elif direction == "S":
            direction = "SOUTH"
        elif direction == "E":
            direction = "EAST"
        elif direction == "W":
            direction = "WEST"
        return direction
            
    def report(self,table):
        if self.x == None or self.y == None or self.direction == None:
            print('Robot not yet placed')
        else:
            print (f'{self.x},{self.y},{self.direction}')
        table.draw(self)