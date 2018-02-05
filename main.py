# importing spy_details
from spy_details import spy_name,spy_age,spy_rating

# Start greeting
print ("Hello!!!")
print('******* << Welcome to SpyChat >> *******')
# Using escape sequence
print ("Let\'s get started...\n")

STATUS_MESSAGES = ['I\'m busy', 'Available', 'Loving Life!', 'Sleeping']

# Declaring function for adding status
def add_status(current_status_message):
    if current_status_message != None:
        print "Your current status message is: " + current_status_message     # Displays current status message
    else:
        print"\nYou don't have any status currently!"

    # Asking whether we want to select any old status or not
    status = raw_input("\nDo you want to select from old statuses? (Y/N) : ")
    if status.upper() == 'Y':
        # Displaying old statuses
        serial_number = 1
        for old_status in STATUS_MESSAGES:
            print str(serial_number) + ". " + old_status
            serial_number = serial_number + 1
        user_selection = input("\nWhich one do you want to select? ")
        if len(STATUS_MESSAGES)>=user_selection:
            new_status = STATUS_MESSAGES[user_selection - 1]
        else:
            print("Invalid selection!")
    elif status.upper() == 'N':
        new_status = raw_input("Enter your new status: ")
        if len(new_status) > 1:
            STATUS_MESSAGES.append(new_status)
        else:
            print("Please enter something atleast!")
    else:
            print("Invalid entry!")
    return new_status

# Declaring function
def start_chat(spy_name,spy_age,spy_rating):
    # Initializing current status message with None
    current_status_message = None
    # Initializing show_menu variable with true value
    show_menu = True
    while show_menu:
        # Displaying options to select different features of application
        menu_choice = input("\nWhat do you want to do? \n 1. Add a status update\n 0. Exit\n")
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)  # add_status function is called with current status message as parameter
            print "Your status has been set to: " + updated_status_message
        elif menu_choice == 0:
            show_menu = False
        else:
            print("Invalid choice!!!")
        # More features to be added

# Asking the spy whether to continue with existing values or create a new user
spy_exist = raw_input("Are you an existing user?(Y or N) : ")

# Validating input
if spy_exist.upper() == 'Y':        # .upper() converts from any case to upper case

    # Existing user
    print("We already have your details!")

    # Calling function to start chat application
    start_chat(spy_name, spy_age, spy_rating)
elif spy_exist.upper() == 'N':

    # New user
    spy_name = raw_input("\nWhat is your spy name? ")

    # Checking whether spy has entered any name or not
    if len(spy_name)>=2:
        print "Welcome " +spy_name+ ", Glad to meet you!"
        # Asking for salutation
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)? " )

        # Validating salutation
        if len(spy_salutation)>0:

            # Concatenating salutation and name of spy
            spy_name = spy_salutation + " " + spy_name
            print "Alright " + spy_name + ". I'd like to know a little bit more about you..."
            # Asking for age
            spy_age = input("Enter your age: ")
            # Age cannot be less than 12 and greater than 50
            # Nested if
            if spy_age>=12 and spy_age<50:
                print ("Your age is fine to become a spy!\n ")
                # Asking for rating
                spy_rating = input("Enter your rating: ")
                # Conditions for displaying comments according to the spy_rating
                if spy_rating>4.5:
                    print("Great ace!\n")
                elif spy_rating >3.5 and spy_rating <= 4.5:
                    print("You are one of the good ones.\n")
                elif spy_rating >= 2.5 and spy_rating <= 3.5:
                    print("You can always do better.\n")
                else:
                    print("We can always use somebody to help in the office.\n")

                # Default Value
                spy_is_online = True
                # Using placeholders(%s,%d,etc.)
                print "Authentication complete! %s, Welcome to SPY COMMUNITY... \nAge: %d and Rating of: %.1f\nProud to have you onboard !" %(spy_name,spy_age,spy_rating)

                # Calling function to start chat application
                start_chat(spy_name,spy_age,spy_rating)
            else:
                # Age not within the specified limits
                print("Sorrry! Age inappropriate to become a spy... ")
        else:
            # Salutation not within the specified limits
            print("Invalid salutation!")
    else:
        # Name too small
        print("Invalid name! Enter a 2 letter name atleast ")
