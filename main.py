from Intros import draw_art, show_table_and_help_message, welcome_message
import Command_Handler
import Robot
import Table

def main():
    draw_art()
    welcome_message()
    new_robot = Robot.Robot()
    new_table = Table.Table()
    show_table_and_help_message(new_table, new_robot)
    while True:
        try:
            command = Command_Handler.string_to_command_parser(input(),new_robot,new_table)
            if command == "EXIT":
                break
        except Exception:
            print("ERROR: Please enter a valid command")

if __name__ == "__main__":
    main()

