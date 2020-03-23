# Sam Cole
# This is the first in first out paper system
from Queue import Queue

# this is the menu
totalstock = Queue()
totalmoney = Queue()
profit = 0
answer = 0
while answer != 4:
    print("""Please type the number to select what you would like to do
            1.buy stock
            2.sell stock
            3.see your profit
            4.close program""")
    answer = int(input())
    if answer == 1:
        print("How much did paper did you buy?")
        stock = input()
        print("How much was it per unit? please only the number")
        money = input()
        totalstock.push(stock)
        totalmoney.push(money)

    elif answer == 2:
        print("How much are you selling?")
        reqstock = int(input())
        print("For how much per unit? please only the number")
        money = int(input())
        oldstock = int(totalstock.pop())
        oldmoney = int(totalmoney.pop())
        profit = (money - oldmoney) * reqstock
        while reqstock > oldstock:
            reqstock = reqstock - oldstock
            oldstock = totalstock.pop()
        if reqstock < oldstock:
            oldstock = oldstock - reqstock
            totalstock.push(oldstock)
            totalmoney.push(oldmoney)

    elif answer == 3:
        print("$" + str(profit))
