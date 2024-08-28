"""
Table Class

Initialises a table object and provides methods to check for edges and a function to draw the table
"""

class Table:
    def __init__(self):
        self.x = self.ask_for_table_width()
        self.y = self.ask_for_table_height()
        self.x_grid = list(range(self.x))
        self.y_grid = list(range(self.y))
    
    def ask_for_table_width(self):
        while True:
            try:
                x = int(input("Please enter the width of the table: "))
                if x < 1:
                    print("ERROR: Please enter a number greater than 0")
                elif x > 10:
                    print("ERROR: Please enter a number less than 11")
                else:
                    print(f'Table width is: {x}')
                    return x
            except:
                print("ERROR: Please enter a valid number")
    
    def ask_for_table_height(self):
        while True:
            try:
                y = int(input("Please enter the height of the table: "))
                if y < 1:
                    print("ERROR: Please enter a number greater than 0")
                elif y > 10:
                    print("ERROR: Please enter a number less than 11")
                else:
                    print(f'Table width is: {y}')
                    return y
            except:
                print("ERROR: Please enter a valid number")    
   
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
        
        
    def draw_table(self,robot):
        table_grid = [["  " for _ in range(self.table.x)] for _ in range(self.table.y)]

        robot_symbol = {"NORTH": "^ ", "SOUTH": "v ", "EAST": "> ", "WEST": "< "}
        if robot.robot_has_been_placed:
            table_grid[robot.y][robot.x] = robot_symbol[robot.direction]

        print("     " + "    ".join(str(i) for i in range(self.table.x)))
        for y in range(self.table.y-1, -1, -1):
            print(f"{y} |  " + " | ".join(table_grid[y]) + " |")
            if y > 0:
                print("   " + "-----" * self.table.x)
        print("     " + "    ".join(str(i) for i in range(self.table.x)))