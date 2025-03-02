def table(X_moves, O_moves):
   zero= 'X' if X_moves[0] else('O' if O_moves[0] else 0)
   one= 'X' if X_moves[1] else('O' if O_moves[1] else 1)
   two= 'X' if X_moves[2] else('O' if O_moves[2] else 2)
   three= 'X' if X_moves[3] else('O' if O_moves[3] else 3)
   four= 'X' if X_moves[4] else('O' if O_moves[4] else 4)
   five= 'X' if X_moves[5] else('O' if O_moves[5] else 5)
   six= 'X' if X_moves[6] else('O' if O_moves[6] else 6)
   seven= 'X' if X_moves[7] else('O' if O_moves[7] else 7)
   eight= 'X' if X_moves[8] else('O' if O_moves[8] else 8)
   print(f" {zero} | {one} | {two} ")
   print("---|---|---")
   print(f" {three} | {four} | {five} ")
   print("---|---|---")
   print(f" {six} | {seven} | {eight} ")
   print("---|---|---")

def check(X_moves, O_moves):
    winning = [
        [0,1,2], [3,4,5], [6,7,8], #Rows
        [0,3,6], [1,4,7], [2,5,8], #columns
        [0,4,8], [2,4,6]          #Diagnols
    ]
    for win in winning:
        if(X_moves[win[0]] + X_moves[win[1]] + X_moves[win[2]] == 3):
            print("X won\n")
            return 1
        if(O_moves[win[0]] + O_moves[win[1]] + O_moves[win[2]] == 3):
            print("O won\n")
            return 0
    return -1


if __name__ == "__main__":
    X_moves=[0,0,0,0,0,0,0,0,0]
    O_moves=[0,0,0,0,0,0,0,0,0]
    chance=1



    while(True):
        table(X_moves,O_moves)
        print("")
        if(chance==1):
            print("X's Turn")
            value=int(input("Please enter a value:- "))
            X_moves[value]=1
        else:
            print("O's Turn")
            value=int(input("Please enter a value:- "))
            O_moves[value]=1
        win_check = check(X_moves, O_moves)
        if(win_check != -1):
            print("Good Game")
            print("Play Again")
            break
        chance = 1 - chance

