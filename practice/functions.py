def thank_you(name):
    print ("\nYou are doing an excelllent job, %s!" %name)
    print ("I would be more than willing to write a letter of recommendation")

thank_you('Brianna')

def show_students(students, message):
    #Prints out a message, then list of students
    print(message)
    for student in students:
        print ("- " + student.title())

students = ['Michael', 'Anthony', 'Mickey']
message = 'Welcome to U of M!'

show_students(students, message)


def govt_name(first_names, last_names):
    print ("\nYou are doing an excelllent job, %s!" %first_names)
    print ("Welcome to Mars " + first_names + " " + last_names)

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
govt_name(first_name, last_name)

strength = 5
print ("Your strength is %s" %strength)
while strength < 10:
    strength += 1
    print (strength)
print ("You are now super strong. Congrats.")

board_games = ['Checkers', 'Chess', 'Cards']
new_game = input("What games do you like to play?")
board_games.append(new_game)
print (board_games)

pets = { 'ziggy': 'canary', 'bob':'moose', 'erica': 'gorilla'}
for name, pet in pets.items():
    print("{} is a {}".format(name, pet))
