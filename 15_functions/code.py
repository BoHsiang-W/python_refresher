# funciton
def hello():
    print('Hello')

hello()

## funciton with parameters
def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in seconds program!")
user_age_in_seconds()
print("Goodbye!")

## function with parameters
friends = ["Rolf", "Jen", "Bob", "Anne"]
def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]
    
add_friend()
print(friends)

## function with parameters
friends = []
def add_friend():
    friends.append("Rolf")

add_friend()
print(friends)