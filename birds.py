
from pathlib import Path

output_path = Path(__file__).with_name("birds_output.txt")
output_path.write_text("")

mybird1 = """ This is bird 1:
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            """

mybird2 = """ This is bird 2:
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
               
               
               """
print(mybird1,mybird2,sep="\n",end="\n")

mybird1_explanation = "Round bird. Round bird likes to snack and has many friends."

mybird2_explanation = "Big bird. Big bird takes no shit. Big bird is a bad ass."

print("Please answer the following questions!")

fbird = input("Which is your favorite bird?\n 1 or 2?\n")

if fbird == "1":
    print("Your favorite bird is..."+mybird1_explanation)
if fbird == "2":
    print("Your favorite bird is..."+mybird2_explanation)

cbird = input("What is your favorite color? Pick from ROYGBIV.\n")

#say which bird it is based on the answer
bird1_red = """ 
            \033[31m
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            \033[0m"""

bird2_red = """ 
            \033[31m
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
                             \033[0m"""

bird1_blue = """ 
            \033[34m
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            \033[0m"""

bird2_blue = """ 
            \033[34m
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
                             \033[0m"""


bird1_yellow = """ 
            \033[33m
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            \033[0m"""

bird2_yellow = """ 
            \033[33m
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
                             \033[0m"""


bird1_orange = """ 
            \033[38;5;208m
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            \033[0m"""

bird2_orange = """ 
            \033[38;5;208m
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
                             \033[0m"""


bird1_green = """ 
            \033[32m
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            \033[0m"""

bird2_green = """ 
            \033[32m
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
                             \033[0m"""


bird1_indigo = """ 
            \033[38;2;75;0;130m
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            \033[0m"""

bird2_indigo = """ 
            \033[38;2;75;0;130m
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
                             \033[0m"""


bird1_violet = """ 
            \033[38;2;138;43;226m
             /----------|
            |           |
            | |-|  |-|  | /------- 
            |   __      |/  / / /
            |    _____         /  
            |_________________/
                  |     |     
                 ///   ///       
                        
                            \033[0m"""

bird2_violet = """ 
            \033[38;2;138;43;226m
            |------|
            | ..   |
        /----      |
        --------   |
               |   |             ______ 
               |    ____________/     / 
                |   |         /      /
                 |   | -------      /
                  |________________/
                    | |     | |
                    | |     | |
                    ///    ///  
                             \033[0m"""


#need to add the colors

if fbird == "1" and cbird == "red":
    print("Look at your bird now! It is ",cbird,"!",bird1_red,sep='')
if fbird == "2" and cbird == "red":
    print("Look at your bird now! It is ",cbird,"!",bird2_red,sep='')

if fbird == "1" and cbird == "blue":
    print("Look at your bird now! It is ",cbird,"!",bird1_blue,sep='')
if fbird == "2" and cbird == "blue":
    print("Look at your bird now! It is ",cbird,"!",bird2_blue,sep='')

if fbird == "1" and cbird == "yellow":
    print("Look at your bird now! It is ",cbird,"!",bird1_yellow,sep='')
if fbird == "2" and cbird == "yellow":
    print("Look at your bird now! It is ",cbird,"!",bird2_yellow,sep='')

if fbird == "1" and cbird == "orange":
    print("Look at your bird now! It is ",cbird,"!",bird1_orange,sep='')
if fbird == "2" and cbird == "orange":
    print("Look at your bird now! It is ",cbird,"!",bird2_orange,sep='')

if fbird == "1" and cbird == "green":
    print("Look at your bird now! It is ",cbird,"!",bird1_green,sep='')
if fbird == "2" and cbird == "green":
    print("Look at your bird now! It is ",cbird,"!",bird2_green,sep='')

if fbird == "1" and cbird == "indigo":
    print("Look at your bird now! It is ",cbird,"!",bird1_indigo,sep='')
if fbird == "2" and cbird == "indigo":
    print("Look at your bird now! It is ",cbird,"!",bird2_indigo,sep='')

if fbird == "1" and cbird == "violet":
    print("Look at your bird now! It is ",cbird,"!",bird1_violet,sep='')
if fbird == "2" and cbird == "violet":
    print("Look at your bird now! It is ",cbird,"!",bird2_violet,sep='')

food_object = input("Are you an early bird (1) or night owl (2)? Please type the character 1 or 2.\n")

if food_object == "1":
    print("Since you are an early bird, your bird gets a worm!")
    print(""" 
              /------\\
             |______  \\
                    |  |    'this is a worm'
                    |  |
                    |  | 
                    |  |------------\\
                    \\______________//
                                           
                                        """)


if food_object == "2":
    print("Since you are a night owl, here is the moon!")
    print(""" 

          ----------
        /   .   .   . \\  'this is the moon'
        | .  .   .   . | 
        |.   .  ,   .  |
        \\   ,     ,   /
          -----------    

                          """)



print("Thank you for answering! Have a great day :)\n\n\n")


with output_path.open("a") as outputfile:
    print("Favorite Bird","Favorite Color", "Early Bird or Night Owl", sep='\t', file=outputfile)
    print(fbird, cbird, food_object, sep='\t', file=outputfile)


#get input from users
#make more interactive survey based on bird1/2 responses
#tabulate data in excel file
#take data from excel file and create bar graph
#def favorite_bird:
#    if fbird = 1