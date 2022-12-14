import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,"B":4,"C":6,"D":8
}
symbol_values = {
    "A":5,"B":4,"C":3,"D":2
}

def check_win(columns, lines, bet, values):
    winnings = 0 
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)

    return winnings,winning_line

def getslot_onspin(rows,cols,symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)        
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print (column[row], end = " | ")
            else:
                print (column[row], end ="")
        print()

def deposit():
    while True:
        amount = input("enter the amount that you would like to deposit $")
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
    
def spins(balance):
    lines = getno_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("insufficient balance, your balance is $ ",balance)
        else :
            break

    print (f"you are betting ${bet} on {lines} lines . Total bet is equal to: ${total_bet}")

    slot = getslot_onspin(ROWS, COLS, symbol_count)
    print_slot(slot)
    winnings,winning_line = check_win(slot, lines, bet, symbol_values)

    print(f"you won ${winnings}..")
    print(f"you won on lines: ",*winning_line)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print (f"current balance is ${balance}")
        spin = input("press enter to spin (q to quit)...")
        if spin == "q":
            break
        else:
            balance += spins(balance)

    print (f"you current balance is ${balance}")   
    
main()