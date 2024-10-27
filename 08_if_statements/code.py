# if statements
day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's Tuesday!")
elif day_of_week == "friday":
    print("It's the end of the week! Have a great weekend!")
else:
    print("Full speed ahead!")

print("This always runs.")