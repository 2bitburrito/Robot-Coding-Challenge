"""
Robot Simulator Intro Functions
"""
import Table

def draw_art():
    print(
"""
                 ____                    |    
                [____]                   |    
                ][][][                   |    
              ___\__/___                 |    
             |__|    |__|                |    
              |_|_/\_|_|                 |    
_____________ | | __ | | ________________|    
              |_|[  ]|_|                  \   
              \_|_||_|_/                   \  
                |_||_|                      \ 
               _|_||_|_                      \\
              |___||___|                      
                                                """
    )
    
def welcome_message():
    print("+++ Welcome to the SEEK Robot Simulator +++")
    print()
    print("First, lets set up the table:")
    print()

def show_table_and_help_message(table,robot):
    print("Here is your table:")
    table.draw(robot)
    print("Please enter a command:")
    print()
    print("Type HELP or H for a list of available commands")
   