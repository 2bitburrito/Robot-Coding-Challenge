# Classes for Command Handling and the Parser for Input Strings
import Classes

class Command:
    def execute(self,robot):
        raise NotImplementedError("Subclass must implement abstract method")
    
class PlaceCommand(Command):
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def execute(self,robot):
        robot.place(self.x,self.y,self.direction)
        
class MoveCommand(Command):
    def execute(self,robot):
        robot.move()

class TurnCommand(Command):
    def __init__(self,new_direction):
        self.new_direction = new_direction
    
    def execute(self,robot):
        robot.turn(self.new_direction)
        
class ReportCommand(Command):
    def execute(self,robot):
        Classes.draw_table(robot,robot.table)
        print(robot.report())
        
class RobotController:
    def process(self,commands,robot):
        for command in commands:
            command.execute(robot)




def string_to_command_parser(input_string,robot):
    string_split = input_string.strip().split()
    command_name = string_split[0].upper()
    
    if command_name == "PLACE":
        try:
            x,y,f = string_split[1].split(',')
        except:
            raise Exception('ERROR: Please ensure the PLACE command is in the correct format')
        return PlaceCommand(int(x),int(y),f.upper())
   
    elif command_name == "MOVE":
        if robot.robot_has_been_placed == False:
            print("ERROR: Please place the robot first!")
        elif robot.table.check_for_edge(robot.direction,robot) == True:
            print("ERROR: Cannot move off the table")
        else:
            return MoveCommand()
    
    elif command_name == "LEFT" or command_name == "RIGHT":
        if robot.robot_has_been_placed == False:
            raise Exception("ERROR: Please place the robot first!")
        else:
            return TurnCommand(command_name)
    
    elif command_name == "REPORT":
        if robot.robot_has_been_placed == False:
            raise Exception("ERROR: Please place the robot first!")
        return ReportCommand()
    
    elif command_name == "EXIT":
        return "EXIT"
    
    elif command_name == "HELP" or command_name == "H":
        print('Your available commands are:')
        print()
        print("PLACE X,Y,DIRECTION: Place the robot on the table at position x,y and facing direction")
        print("\t\tChoose from the following directions: NORTH, EAST, SOUTH, WEST")
        print()
        print("MOVE: Move the robot one unit in the direction it is facing")
        print()
        print("LEFT: Turn the robot 90 degrees to the left")
        print()
        print("RIGHT: Turn the robot 90 degrees to the right")
        print()
        print("REPORT: Output the current position of the robot")
        print()
        print("EXIT: Exit the program")
        
    
    else:
        raise Exception(f'ERROR: Unrecognised command: {command_name}')