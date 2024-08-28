"""
Robot Tabletop
"""
class Robot:
    def __init__(self,table):
        self.table = table
        self.x = 0
        self.y = 0
        self.direction = None
        self.move_amount = 1
        self.robot_has_been_placed = False
        self.direction_list = ['NORTH','EAST','SOUTH','WEST']
    
    def place(self,x=0,y=0,direction="NORTH"):
        direction = self.fix_direction_string(direction)
        if self.position_is_valid(x,y) and direction in self.direction_list:
            self.x = x
            self.y = y
            self.direction = direction
            self.robot_has_been_placed = True
        else:
            raise Exception('ERROR: Please ensure the position and direction are valid')
            
    def move(self):
        if self.robot_has_been_placed == False:
            raise Exception("ERROR: Please place the robot first!")
        elif self.table.check_for_edge(self.direction,self):
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
        new_direction = new_direction.upper()
        current_direction_index = self.direction_list.index(self.direction)
        if new_direction == "LEFT":
            new_index = (current_direction_index - 1) % len(self.direction_list)
        elif new_direction == "RIGHT":
            new_index = (current_direction_index + 1) % len(self.direction_list)
        self.direction = self.direction_list[new_index]
        return self.direction

    def position_is_valid(self,x,y):
        if type(x) != int or type(y) != int:
            raise Exception('ERROR: Please ensure both indicies are a valid number')
        elif x not in self.table.x_grid or y not in self.table.y_grid:
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
            
    def report(self):
        return f'{self.x},{self.y},{self.direction}'
            
class Table:
    def __init__(self,table_x,table_y):
        self.x = table_x
        self.y = table_y
        self.x_grid = list(range(table_x))
        self.y_grid = list(range(table_y))
        
    
    def check_for_edge(self,direction,robot):
        if direction == "NORTH" and robot.y == self.y_grid[-1]:
            return True
        if direction == "SOUTH" and robot.y == self.y_grid[0]:
            return True
        if direction == "EAST" and robot.x == self.x_grid[-1]:
            return True
        if direction == "WEST" and robot.x == self.x_grid[0]:
            return True
        return False
    
    def draw(self,robot):
        table_grid = [["  " for _ in range(self.x)] for _ in range(self.y)]

        robot_symbol = {"NORTH": "^ ", "SOUTH": "v ", "EAST": "> ", "WEST": "< "}
        if robot.robot_has_been_placed:
            table_grid[robot.y][robot.x] = robot_symbol[robot.direction]

        print("     " + "    ".join(str(i) for i in range(self.x)))
        for y in range(self.y-1, -1, -1):
            print(f"{y} |  " + " | ".join(table_grid[y]) + " |")
            if y > 0:
                print("   " + "-----" * self.x)
        print("     " + "    ".join(str(i) for i in range(self.x)))
        

def draw_table(robot,table):
    table_grid = [["  " for _ in range(table.x)] for _ in range(table.y)]

    robot_symbol = {"NORTH": "^ ", "SOUTH": "v ", "EAST": "> ", "WEST": "< "}
    if robot.robot_has_been_placed:
        table_grid[robot.y][robot.x] = robot_symbol[robot.direction]

    print("     " + "    ".join(str(i) for i in range(table.x)))
    for y in range(table.y-1, -1, -1):
        print(f"{y} |  " + " | ".join(table_grid[y]) + " |")
        if y > 0:
            print("   " + "-----" * table.x)
    print("     " + "    ".join(str(i) for i in range(table.x)))
        
def draw_art():
    print(
"""
                 ____                    |    
                [____]                   |    
                ]()()[                   |    
              ___\__/___                 |    
             |__|    |__|                |    
              |_|_/\_|_|                 |    
_____________ | | __ | | ________________|    
              |_|[::]|_|                  \   
              \_|_||_|_/                   \  
                |_||_|                      \ 
               _|_||_|_                      \\
              |___||___|                      
                                                """
    )
    
def welcome_message():
    print("+++ Welcome to the SEEK Robot Simulator +++")
    print()
    print("Please enter a command:")
    print()
    print("Type HELP or H for a list of available commands")

        
#  TEST STUFF HERE:

# new_table = Table(5,5)
# bender = Robot(new_table)


# bender.place(0,0,"NORTH")
# bender.turn("RIGHT")
# # bender.turn("RIGHT")
# print(bender.report())
# bender.move()
# bender.move()
# print(bender.report())
# bender.turn("LEFT")
# # bender.turn("LEFT")
# print(bender.report())
# bender.move()
# print(bender.report())
# bender.move()
# bender.move()
# bender.move()
# # bender.move()
# # bender.move()
# print(bender.report())









