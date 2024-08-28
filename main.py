from Classes import Table, Robot, draw_art, welcome_message
import Command_Handler


new_table = Table(5,5)
bender = Robot(new_table)



draw_art()
welcome_message()
def main():
    while True:
        try:
            command = Command_Handler.string_to_command_parser(input(),bender)
            if command == "EXIT":
                break
            elif command:
                command.execute(bender)
        except Exception:
            print("ERROR: Please enter a valid command")


if __name__ == "__main__":
    main()