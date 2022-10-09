# Создайте программу для игры в 'Крестики-нолики'.
position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
victories = [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
win = ""
def get_result():
    
 
    for i in range(len(victories)):
        if victories[i] == "X":
            win = "X"
        if victories[i] == "O":
            win = "O"   
             
    return win
 

sign = "0"
while True:
    if sign == "0":
       sign = "X"
    else:
        sign = "0"
    
    print(f'{position[0]:^5}|{position[1]:^5}|{position[2]:^5}')
    print("-------------------")
    print(f'{position[3]:^5}|{position[4]:^5}|{position[5]:^5}')
    print("-------------------")
    print(f'{position[6]:^5}|{position[7]:^5}|{position[8]:^5}')
    
    index = int(input("\n\nСделайте ход: "))
    
    position[index - 1] = sign
    if win != "":
        game_over = 'победили X'
    else:
        game_over = 'победили 0'
    print(game_over)
    