kindsOfPlans = ["A", "B", "C"]

countedPlans = 0
totalValue = 0
paymentPlans = ["M", "3M", "Y"]
while True:
    value = 0
    discount = 1
    plan = input("what plan do you want").upper()
    valueBeforeCheckAge = 0
    valueAfterCheckAge = 0
    while plan not in kindsOfPlans:
        plan = input("what plan do you want").upper()

    if plan == "A":
        value = 120
    elif plan == "B":
        value = 100
    else:
        value = 80
    
    kindOfPayment = input("do you want M, 3M, Y").upper()

    if kindOfPayment == "3M":
        discount = 0.9
    elif kindOfPayment == "Y":
        discount = 0.8

    valueBeforeCheckAge = discount * value

    age = int(input("how old are you"))

    valueAfterCheckAge = valueBeforeCheckAge 
    if age < 21 or age >= 65:
        valueAfterCheckAge = valueAfterCheckAge * 0.9
    
    countedPlans += 1
    totalValue += valueAfterCheckAge
    doesUserWantToContinue = input("do you want to continue?").upper()
    if doesUserWantToContinue == "N":
        break


print(f"counted plans:{countedPlans}. totalValue: {totalValue}")