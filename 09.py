user = input("Type your name: ")
password = input("Password: ")

if user == "Thiago":
    print("Welcome again Thiago!")
elif user != "Thiago":
    print("User is incorrect!")
else:
    print("Ban!")

if password >= 100:
    print("The number is too high")
elif password <= 10:
    print("The number is too low")
else:
    print("Do not display")

