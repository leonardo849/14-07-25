totalValue = 0
quantity = 0
categories = ["A", "B", "C"]
while True:
    age = int(input("how old are you?"))
    kindOfTicket = input("what kind of ticket do you want?").upper()
    price = 0
    discount = 1
    finalPrice = 0
    while kindOfTicket not in categories:
        print("wtf are you sending me bro?")
        kindOfTicket = input("what kind of ticket do you want?").upper()
        

    if age < 18 or age >= 60:
        discount = 0.5
    
    if kindOfTicket == "A":
        price = 40
    elif kindOfTicket == "B":
        price = 30
    else:
        price = 25

    finalPrice = discount * price
    quantity += 1
    totalValue += finalPrice
    print(f"that ticket was ${finalPrice}")

    doesUserWantContinueString = input("do you want to continue buying tickets?").upper()
    if doesUserWantContinueString == "N":
        break

print(f"you got {quantity} tickets. totalValue: {totalValue}")