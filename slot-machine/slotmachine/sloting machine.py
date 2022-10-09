def deposit():
    while True:
        amount = (input("enter the amount that you would like to deposit "))
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount should be greater than 0!..")

        else:
            print("enter valid one")
    else:
        return amount

deposit()

