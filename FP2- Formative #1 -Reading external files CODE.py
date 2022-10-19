#-------------------------------------------
#FP2- Formative #1 -  Reading external files
#Cole Patton
#-------------------------------------------
# Mine will be kind of the same as the lesson but it will do videogames.

def display_all():
    file = open('Video Games.txt', 'r')
    
    all_lines = file.read()
    print(all_lines)
    file.close()

def list_file():
    file = open('Video Games.txt', 'r')
    list_games = file.readlines()
    greatest_game = (list_games[0])
    print(f"The GREATEST game of all time is: {greatest_game}")
    second_best_game = (list_games[1])
    print(f"The SECOND best game of all time is: {second_best_game}")
    another_game = (list_games[4])
    print(f"Another good game, especially zombies mode, is: {another_game}")
    
    print("All the good games are:", (list_games))
    print("")
    
def read_line_by_line():
    file = open('Video Games.txt','r')
    
    line = file.readline()
    print(line)
    for games in file:
        print(games)
    

def main():
    display_all()
    list_file()
    read_line_by_line()

#--------------------------Main Code-----------------------------
main()
    

