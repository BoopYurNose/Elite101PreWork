UserValue = False

print("Welcome user!")
NameInput = input("What is your name?")
print(f"Hello {NameInput}")
AgeInput = input("What is your Age?")

while UserValue == False:
    print("How can I help you I can help you with \n Mathmatics \n Programming \n General Advice \n and More! \n Type Quit to end the conversation")
    UserInput = input()
    if UserInput == "Quit":
        print("Alright then. Goodbye for now!")
        UserValue = True
