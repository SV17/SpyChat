#importing spy_details
from spy_details import spy_name,spy_age,spy_rating

#start greeting
print ("Hello!!!")
print('******* << Welcome to SpyChat >> *******')
print ("Let\'s get started...\n")

#Function declared
def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True
    while show_menu:
        menu_choice = input("What do you want to do? \n 1. Add a status update\n 0. Exit\n")
        if (menu_choice == 1):
            status = raw_input("Your status please: ")
            print status
        elif menu_choice == 0:
            show_menu = False
        else:
            print("Invalid choice!!!")
        #More features to be added

spy_exist = raw_input("Are you an existing user?(Y or N) : ")

# Validating input
if spy_exist.upper() == 'Y':

    # Existing user
    print("We already have your details!\n")

    # Function called to start chat application
    start_chat(spy_name, spy_age, spy_rating)
elif spy_exist.upper() == 'N':

    # New user
    spy_name = raw_input("What is your spy name? ")

    # Checking spy has any input or not
    if len(spy_name)>=2:
        print "Welcome " +spy_name+ ", Glad to meet you!"
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)?" )

        # Validating salutation
        if len(spy_salutation)>0:

            # Concatenation for salutation and name of spy
            spy_name = spy_salutation + " " + spy_name
            print "Alright " + spy_name + ". I'd like to know a little bit more about you..."
            spy_age = input("Enter your age: ")
            if spy_age>=12 and spy_age<50:
                print ("Your age is fine to be a spy! ")
                spy_rating = input("Enter your rating: ")
                if spy_rating>4.5:
                    print("Great ace!")
                elif spy_rating >3.5 and spy_rating <= 4.5:
                    print("You are one of the good ones.")
                elif spy_rating >= 2.5 and spy_rating <= 3.5:
                    print("You can always do better")
                else:
                    print("We can always use somebody to help in the office.")

                # Default Value
                spy_is_online = True
                print "Authentication complete! Welcome %s... \nAge: %d and Rating of: %.1f\nProud to have you onboard !\n" %(spy_name,spy_age,spy_rating)

                # Function called to start chat application
                start_chat(spy_name,spy_age,spy_rating)
            else:
                print("Sorrry! Age inappropriate to be a spy ")
        else:
            print("Invalid salutation!")
    else:
        print("Invalid name! Enter a 3 letter name atleast ")
