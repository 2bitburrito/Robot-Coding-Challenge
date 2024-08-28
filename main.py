from Intros import draw_art, welcome_message
import Command_Handler
import Robot
import Table


# new_table = Table.Table(5,5)
new_robot = Robot.Robot()



draw_art()
welcome_message()
def main():
    new_table = Table.Table(int(input("How wide would you like your table? ")),int(input("How tall would you like your table? ")))
    while True:
        try:
            command = Command_Handler.string_to_command_parser(input(),new_robot,new_table)
            if command == "EXIT":
                break
            elif command:
                command.execute(new_robot,new_table)
        except Exception:
            print("ERROR: Please enter a valid command")


if __name__ == "__main__":
    main()

