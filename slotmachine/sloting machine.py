MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = (input("enter the amount that you would like to deposit $"))
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount should be greater than 0!..")

        else:
            print("enter valid one")
    
    return amount

def getno_lines():
    while True:
        lines = (input("enter the no of lines to be bet on (1-" + str(MAX_LINE) + ")? "))
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("enter valid one")
    
    return lines

def get_bet():
    while True:
        amount = (input("enter the amount to bet on each line $"))
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("amount should be between ${MIN_BET}  and ${MAX_BET}..")

        else:
            print("enter valid one")
    
    return amount
    


def main():
    balance = deposit()
    lines = getno_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("insufficient balace, your balance is $ ",balance)
        else :
            break
    print (f"you are betting ${bet} on {lines} lines . Total bet is equal to: ${total_bet}")
    
main()