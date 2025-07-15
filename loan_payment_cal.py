from pydoc import apropos


money_owed= float(input("Total loan?"))
apr= float(input("anual rate of interest"))
payement=float(input("how much you will pay each month?"))
num_months = int(input("no. of months you have paid"))

for i in range(num_months):
# cal interest to pay
    interest_paid = apr/100/12
    #add interest
    money_owed = money_owed + interest_paid
    #make payement
    money_owed = money_owed -payement

    print('paid', payement, 'of which', interest_paid, 'was interest', end=' ')
    print('now i owe', money_owed)