# loops
## guess the number game
number = 7

while True:
    user_input = input("Enter 'y' if you would like to play: (Y/n)")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's woring!")

## for loops
friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")

## using the range function
for friend in range(4):
    print(friends[friend])

## using the range function with a start and end
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

## using the sum function
total = sum(grades)
amount = len(grades)
print(total / amount)