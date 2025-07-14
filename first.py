countValidNumbers = 0
countOddNumbers = 0
sumOddNumbers = 0

while True:
    number = int(input("send to a me a number"))
    if number < 0:
        break
    if number >= 25 and number < 50:
        countValidNumbers += 1
    if number % 2 != 0:
        countOddNumbers += 1
        sumOddNumbers += number

print("quantity of numbers between 25 and < 50:", countValidNumbers)
if countOddNumbers > 0:
    print("average:", sumOddNumbers/countOddNumbers)