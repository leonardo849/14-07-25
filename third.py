people = []

def sortHeights(e):
    return e["height"]

def isHeightGreaterThanOneHundredAndEightyFive(e):
    return e["height"] > 185


ageSum = 0
heightSum = 0

while True:
    info = input("create a person. Type: name space age space height (in centimeters)").split(" ")
    name = info[0]
    age = int(info[1])
    height = int(info[2])
    people.append({"name": name, "age": age, "height": height})
    ageSum += age
    heightSum += height

    doesUserWantToCreateAPersonAgain = input("do you want to create a person again?").upper()
    if doesUserWantToCreateAPersonAgain == "N":
        break


people.sort(key=sortHeights)
smallestPersonInGroup = people[0]

print(f"the smallest person in group: name {smallestPersonInGroup["name"]}, age {smallestPersonInGroup["age"]}", )
print(f"average age {round(ageSum / len(people), 2)} average height {round(heightSum/len(people), 2)}")

filtered = len([p for p in people if p["height"] > 185])
print(f"quantitys of tall people: {filtered}")