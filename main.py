from os import system as sys
from colorama import Fore as fore
from replit import db, clear

account = None 

def login(): 
    global account
    clear()
    user = str(input("Username: ")) 
    passw = str(input("Password: "))

    if user in db.keys():
        if db[user]["password"] == passw: 
            account = db.get(user)
        else:
            print("Inorrect Password")
            login()
    else:
        print("Not Real Account")
        login()

def signup():
    global account
    clear()
    user = str(input("Username: ")) 
    passw = str(input("Password: ")) 

    if user not in db.keys(): 
        db[user] = {
            "password": passw,
            "wins": 0, 
            "losses": 0,
            "ties": 0
        }
        print("Account Made!") 
        account = db.get(user)
    else:
        print("Account Already Exists") 
        signup()

ls = input("1: Login\n2: Signup\n\nOption: ")

if ls == "1":
    login()

else:
    signup()

green = fore.GREEN
reset = fore.RESET

a = [" ", " ", " "]
b = [" ", " ", " "]
c = [" ", " ", " "]

boards = {
    "a": a,
    "b": b,
    "c": c
}

boardsd = [a, b, c]

to = ["o", "x"]
num = 0

bot = None
clear()
B = input("Wins: {}\nLosses: {}\nTies: {}\n\n1: Single Player\n2: Multiplayer\n\nOption: ".format(account["wins"], account["losses"], account["ties"]))

if B == "1":
    bot = True

else:
    bot = False

while True:
    clear()

    if num % 2 == 0:
        turn = to[0]

    else:
        turn = to[1]

    num += 1

    print(turn + "'s Turn")

    def generateboard():
        board = f"""
    a  {" | ".join(a)}
      ---+---+----
    b  {" | ".join(b)}
      ---+---+----
    c  {" | ".join(c)}
    
       1   2   3
        """
        return board

    print(generateboard())

    if bot == True:

        if turn == "o":
        
            q = input("(ex. a2) Pick Your Spot: ")
    
        try:
    
            if turn == "o": # your move
    
                split = list(q)
                Board = boards[str(split[0])]
                number = int(split[1]) - 1
                
                if Board[number] == " ":
                    Board[number] = turn
                else:
                    input("That Spot Is Taken [ENTER]")
                    num += 1
                generateboard()
    
            else: # the bot's move
                if a[0] == "x" and b[1] == "x" and c[2] != "o": c[2] = "x"     
                elif c[0] == "x" and b[1] == "x" and a[2] != "o": a[2] = "x"     
                elif a[2] == "x" and b[1] == "x" and c[0] != "o": c[0] = "x"     
                elif c[2] == "x" and b[1] == "x" and a[0] != "o": a[0] = "x" # diagonal
                elif a[0] == "x" and a[1] == "x" and a[2] != "o": a[2] = "x"
                elif b[0] == "x" and b[1] == "x" and b[2] != "o": b[2] = "x"
                elif c[0] == "x" and c[1] == "x" and c[2] != "o": c[2] = "x" # forward
                elif c[2] == "x" and c[1] == "x" and c[0] != "o": c[0] = "x"
                elif b[2] == "x" and b[1] == "x" and b[0] != "o": b[0] = "x"
                elif a[2] == "x" and a[1] == "x" and a[0] != "o": a[0] = "x" # backward
                elif a[0] == "x" and b[0] == "x" and c[0] != "o": c[0] = "x"
                elif a[1] == "x" and b[1] == "x" and c[1] != "o": c[1] = "x"
                elif a[2] == "x" and b[2] == "x" and c[2] != "o": c[2] = "x" # down
                elif c[0] == "x" and b[0] == "x" and a[0] != "o": a[0] = "x"
                elif c[1] == "x" and b[1] == "x" and a[1] != "o": a[1] = "x"
                elif c[2] == "x" and b[2] == "x" and a[2] != "o": a[2] = "x" # up 
                elif a[0] == "x" and a[2] == "x" and a[1] != "o": a[1] = "x"
                elif b[0] == "x" and b[2] == "x" and b[1] != "o": b[1] = "x"
                elif c[0] == "x" and c[2] == "x" and c[1] != "o": c[1] = "x"           
                elif a[0] == "x" and c[0] == "x" and b[0] != "o": b[0] = "x"       
                elif a[1] == "x" and c[1] == "x" and b[1] != "o": b[1] = "x"       
                elif a[2] == "x" and c[2] == "x" and b[2] != "o": b[2] = "x" 
                elif b[1] == "x" and c[2] == "x" and a[2] != "o": a[2] = "x"
                elif a[2] == "x" and b[1] == "x" and c[2] != "o": c[2] = "x"
                elif a[0] == "x" and c[2] == "x" and b[1] != "o": b[1] = "x"
                elif a[2] == "x" and c[0] == "x" and b[1] != "o": b[1] = "x" # others
                # the above if statements are to check if the bot can win
                # the below if statements are to stop the opponent from winning
                elif a[0] == "o" and b[1] == "o" and c[2] != "x" and c[2] != "o": c[2] = "x"
                elif c[0] == "o" and b[1] == "o" and a[2] != "x" and a[2] != "o": a[2] = "x"     
                elif a[2] == "o" and b[1] == "o" and c[0] != "x" and c[0] != "o": c[0] = "x"     
                elif c[2] == "o" and b[1] == "o" and a[0] != "x" and a[0] != "o": a[0] = "x" # diagonal
                elif a[0] == "o" and a[1] == "o" and a[2] != "x" and a[2] != "o": a[2] = "x"
                elif b[0] == "o" and b[1] == "o" and b[2] != "x" and b[2] != "o": b[2] = "x"
                elif c[0] == "o" and c[1] == "o" and c[2] != "x" and c[2] != "o": c[2] = "x" # forward
                elif c[2] == "o" and c[1] == "o" and c[0] != "x" and c[0] != "o": c[0] = "x"
                elif b[2] == "o" and b[1] == "o" and b[0] != "x" and b[0] != "o": b[0] = "x"
                elif a[2] == "o" and a[1] == "o" and a[0] != "x" and a[0] != "o": a[0] = "x" # backward
                elif a[0] == "o" and b[0] == "o" and c[0] != "x" and c[0] != "o": c[0] = "x"
                elif a[1] == "o" and b[1] == "o" and c[1] != "x" and c[1] != "o": c[1] = "x"
                elif a[2] == "o" and b[2] == "o" and c[2] != "x" and c[2] != "o": c[2] = "x" # down
                elif c[0] == "o" and b[0] == "o" and a[0] != "x" and a[0] != "o": a[0] = "x"
                elif c[1] == "o" and b[1] == "o" and a[1] != "x" and a[1] != "o": a[1] = "x"
                elif c[2] == "o" and b[2] == "o" and a[2] != "x" and a[2] != "o": a[2] = "x" # up
                elif a[0] == "o" and a[2] == "o" and a[1] != "x" and a[1] != "o": a[1] = "x"
                elif b[0] == "o" and b[2] == "o" and b[1] != "x" and b[1] != "o": b[1] = "x"
                elif c[0] == "o" and c[2] == "o" and c[1] != "x" and c[1] != "o": c[1] = "x"           
                elif a[0] == "o" and c[0] == "o" and b[0] != "x" and b[0] != "o": b[0] = "x"       
                elif a[1] == "o" and c[1] == "o" and b[1] != "x" and b[1] != "o": b[1] = "x"       
                elif a[2] == "o" and c[2] == "o" and b[2] != "x" and b[2] != "o": b[2] = "x"
                elif b[1] == "o" and c[2] == "o" and a[2] != "x" and a[2] != "o": a[2] = "x"
                elif a[2] == "o" and b[1] == "o" and c[2] != "x" and c[2] != "o": c[2] = "x" 
                elif a[0] == "o" and c[2] == "o" and b[1] != "x" and c[1] != "o": b[1] = "x"
                elif a[2] == "o" and c[0] == "o" and b[1] != "x" and b[1] != "o": b[1] = "x" 
                elif c[1] == "o" and b[2] == "o" and a[2] != "x" and a[2] != "o": a[2] = "x" 
                elif c[0] == "o" and b[2] == "o" and c[2] != "x" and c[2] != "o": c[2] = "x" # others
                else:
                    if True:
                        b_one = False
                        def find_blank(qwerty):
                            i = 0
                            while True:
                                if qwerty[i] == " ":
                                    qwerty[i] = "x"
                                    return True
                                    break
                                i += 1
                        if b[1] == " ":
                            b[1] = "x"
                            b_one = True
                        if b_one == False:
                            if " " in a:
                                find_blank(a)
                            elif " " in b:
                                find_blank(b)
                            elif " " in c:
                                find_blank(c)
                generateboard()

        except:
            num += 1

    else:
        q = input("(ex. a2) Pick Your Spot: ")
        try:
            split = list(q)
            Board = boards[str(split[0])]
            number = int(split[1]) - 1
            
            if Board[number] == " ":
                Board[number] = turn
            else:
                input("That Spot Is Taken [ENTER]")
                num += 1
        except:
            num += 1

    def printboard():
        sys('clear')
        print(generateboard())

    if True:
        if a[0] == turn and a[1] == turn and a[2] == turn:
            a[0] = green + a[0] + reset
            a[1] = green + a[1] + reset
            a[2] = green + a[2] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        if b[0] == turn and b[1] == turn and b[2] == turn:
            b[0] = green + b[0] + reset
            b[1] = green + b[1] + reset
            b[2] = green + b[2] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        if c[0] == turn and c[1] == turn and c[2] == turn:
            c[0] = green + c[0] + reset
            c[1] = green + c[1] + reset
            c[2] = green + c[2] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        if a[0] == turn and b[1] == turn and c[2] == turn:
            a[0] = green + a[0] + reset
            b[1] = green + b[1] + reset
            c[2] = green + c[2] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        if a[2] == turn and b[1] == turn and c[0] == turn:
            c[0] = green + c[0] + reset
            b[1] = green + b[1] + reset
            a[2] = green + a[2] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        if a[0] == turn and b[0] == turn and c[0] == turn:
            a[0] = green + a[0] + reset
            b[0] = green + b[0] + reset
            c[0] = green + c[0] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        if a[1] == turn and b[1] == turn and c[1] == turn:
            a[1] = green + a[1] + reset
            b[1] = green + b[1] + reset
            c[1] = green + c[1] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        if a[2] == turn and b[2] == turn and c[2] == turn:
            a[2] = green + a[2] + reset
            b[2] = green + b[2] + reset
            c[2] = green + c[2] + reset
            printboard()
            print(turn, "Wins")
            if turn == "x": account["losses"] += 1
            else: account["wins"] += 1
            break

        # below checks for a tie
        blanks = 0
        for i in boardsd:
            for j in i:
                if j == " ":
                    blanks += 1
        if blanks == 0:
            printboard()
            print("Tie")
            account["ties"] += 1
            break