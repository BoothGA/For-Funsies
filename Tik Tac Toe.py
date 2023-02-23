board = """
     1   2   3
  A    |   |  
    ---|---|---
  B    |   |  
    ---|---|---
  C    |   |  
"""
board = list(board)
def GAME_START():
    p = "1"
    turn = "X"
    gameboard = board
    a1, a2, a3 = 21, 25, 29
    b1, b2, b3 = 52, 56, 60
    c1, c2, c3 = 83, 87, 91
    count = 0
    while(True):
        print("".join(board))
        p1 = input("Player " + p + " your turn... \nType what space to place an " + turn + ".\n")
        if p1.lower() == "a1" and gameboard[a1] == " ":
            gameboard[a1] = turn
            count += 1
        elif p1.lower() == "a2" and gameboard[a2] == " ":
            gameboard[a2] = turn
            count += 1
        elif p1.lower() == "a3" and gameboard[a3] == " ":
            gameboard[a3] = turn
            count += 1
        elif p1.lower() == "b1" and gameboard[b1] == " ":
            gameboard[b1] = turn
            count += 1
        elif p1.lower() == "b2" and gameboard[b2] == " ":
            gameboard[b2] = turn
            count += 1
        elif p1.lower() == "b3" and gameboard[b3] == " ":
            gameboard[b3] = turn
            count += 1
        elif p1.lower() == "c1" and gameboard[c1] == " ":
            gameboard[c1] = turn
            count += 1
        elif p1.lower() == "c2" and gameboard[c2] == " ":
            gameboard[c2] = turn
            count += 1
        elif p1.lower() == "c3" and gameboard[c3] == " ":
            gameboard[c3] = turn
            count += 1
        else:
            print("You cannot do that!".upper())
            continue
    #win condition
        if  gameboard[a1] == gameboard[a2] == board[a3] != " ":
            print("Player ",p, "wins!")
            break
        if  gameboard[b1] == gameboard[b2] == gameboard[b3] != " ":
            print("Player ",p, "wins!")
            break
        if  gameboard[c1] == gameboard[c2] == gameboard[c3] != " ":
            print("Player ",p, "wins!")
            break
        if gameboard[a1] == gameboard[b1] == gameboard[c1] != " ":
            print("Player ",p, "wins!")
            break
        if  gameboard[a2] == gameboard[b2] == gameboard[c2] != " ":
            print("Player ",p, "wins!")
            break
        if  gameboard[a3] == gameboard[b3] == gameboard[c3] != " ":
            print("Player ",p, "wins!")
            break
        if  gameboard[a1] == gameboard[b2] == gameboard[c3] != " ":
            print("Player ",p, "wins!")
            break
        if  gameboard[a3] == gameboard[b2] == gameboard[c1] != " ":
            print("Player ",p, "wins!")
            break
        if count == 9:
            print("It's a draw!".upper())
            break
    #Switch players turn
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"
        if p == "1":
            p = "2"
        elif p == "2":
            p = "1"
GAME_START()
print("".join(board))
input("Press enter to end.")
board = """
     1   2   3
  A    |   |  
    ---|---|---
  B    |   |  
    ---|---|---
  C    |   |  
"""