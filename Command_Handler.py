# Classes for Command Handling and the Parser for Input Strings
import Table
import Robot


def string_to_command_parser(input_string,robot,table):
    string_split = input_string.strip().split()
    command_name = string_split[0].upper()
    
    if command_name == "PLACE":
        try:
            x,y,f = string_split[1].split(',')
        except:
            print('ERROR: Please ensure the PLACE command is in the correct format')
        robot.place(table,int(x),int(y),f.upper())
   
    elif command_name == "MOVE":
        if robot.robot_has_been_placed == False:
            print("ERROR: Please place the robot first!")
        elif table.check_for_edge(robot.direction,robot) == True:
            print("ERROR: Cannot move off the table")
        else:
            robot.move(table)
    
    elif command_name == "LEFT" or command_name == "RIGHT":
        if robot.robot_has_been_placed == False:
            print("ERROR: Please place the robot first!")
        else:
            robot.turn(command_name)
    
    elif command_name == "REPORT":
        if robot.robot_has_been_placed == False:
            print("ERROR: Please place the robot first!")
        return robot.report(table)
    
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
        
