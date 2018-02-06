# importing spy_details
from spy_details import spy

# Start greeting
print ("Hello!!!")
print('******* << Welcome to SpyChat >> *******')
# Using escape sequence
print ("Let\'s get started...\n")

# List used for storing old status messages
STATUS_MESSAGES = ['I\'m busy', 'Available', 'Loving Life!', 'Sleeping']

friends = []

# Declaring function for adding status
def add_status(current_status_message):
    # Checking whether any old status exists
    if current_status_message != None:
        print "Your current status message is: " + current_status_message     # Displays current status message
    else:
        # When no old status exists
        print"\nYou don't have any status currently!"

    # Asking whether we want to select any old status or not
    status = raw_input("\nDo you want to select from old statuses? (Y/N) : ")
    if len(status)>= 1:
        if status.upper() == 'Y':
            serial_number = 1
            # Displaying old statuses from list
            for old_status in STATUS_MESSAGES:
                print str(serial_number) + ". " + old_status
                # Incrementing serial number each time to display all statuses
                serial_number = serial_number + 1
            # Asking the user to select one of the displayed statuses
            user_selection = input("\nWhich one do you want to select? ")
            # Value selected by user should not exceed list's length
            if len(STATUS_MESSAGES)>=user_selection:
                new_status = STATUS_MESSAGES[user_selection - 1]
            else:
                print("Invalid selection!")
            return new_status

        elif status.upper() == 'N':
            new_status = raw_input("Enter your new status: ")
            # Checking whether user has entered anything or not
            if len(new_status) > 1:
                # Appending the new status to the list
                STATUS_MESSAGES.append(new_status)
            else:
                # When user doesn't enter anything
                print("Please enter something atleast...")
            return new_status
        else:
            print("Invalid entry!")

    else:
        set_status = 'No status'
        return set_status
    # Returning the value of new status to function

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = raw_input("What is the name of friend? ")
    new_friend['salutation'] = raw_input("What should we call you(Mr. or Ms.)?  ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = input("Age of friend: ")
    new_friend['rating'] = input("Rating of friend: ")
    if len(new_friend['name']) >= 3 and 50>=new_friend['age']>=12 and new_friend['rating']>=spy['rating']:
        friends.append(new_friend)
    else:
        print "\nFriend cannot be added! "
    return len(friends)

def select_a_friend():
    serial_number = 1
    for friend in friends:
        print str(serial_number) + ". " + friend['name']
        serial_number = serial_number + 1
    user_selected_friend = input("\nSelect your friend: ")
    user_index = friends[user_selected_friend - 1]
    return user_index

# Declaring function
def start_chat(spy_name,spy_age,spy_rating):
    # Initializing current status message with None
    current_status_message = None
    # Initializing show_menu variable with true value
    show_menu = True
    while show_menu:
        # Displaying options to select different features of application
        menu_choice = input("\nWhat do you want to do? \n 1. Add a status update\n 2. Add a new friend\n 3. Send a message\n 0. Exit\n")
        if menu_choice == 1:
            current_status_message = add_status(current_status_message)  # add_status function is called with current status message as parameter
            if len(current_status_message)>= 1:
                if current_status_message == 'No status':
                    print "You didn't select the status correctly!"
                else:
                    # Prints the value returned from add_status function
                    print "Your status has been set to: " + current_status_message
            else:
                print "You didn't select the status correctly!"
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print "You have " + str(number_of_friends) + " friend/friends."
        elif menu_choice == 3:
            user_friend = select_a_friend()

        # For exitting from menu
        elif menu_choice == 0:
            show_menu = False
        else:
            print("Invalid choice!!!")
        # More features to be added...

# Asking the spy whether to continue with existing values or create a new user
spy_exist = raw_input("Are you an existing user?(Y or N) : ")

# Validating input
if spy_exist.upper() == 'Y':        # .upper() converts from any case to upper case

    # Existing user
    print("We already have your details!")

    # Calling function to start chat application
    start_chat(spy['name'], spy['age'], spy['rating'])
elif spy_exist.upper() == 'N':
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    # New user
    spy['name'] = raw_input("\nWhat is your spy name? ")

    # Checking whether spy has entered any name or not
    if len(spy['name'])>=2:
        print "Welcome " +spy['name']+ ", Glad to meet you!"
        # Asking for salutation
        spy['salutation'] = raw_input("What should we call you(Mr. or Ms.)? " )

        # Validating salutation
        if len(spy['salutation'])>0:

            # Concatenating salutation and name of spy
            spy['name'] = spy['salutation'] + " " + spy['name']
            print "Alright " + spy['name'] + ". I'd like to know a little bit more about you..."
            # Asking for age
            spy['age'] = input("Enter your age: ")
            # Age cannot be less than 12 and greater than 50
            # Nested if
            if spy['age']>=12 and spy['age']<50:
                print ("Your age is fine to become a spy!\n ")
                # Asking for rating
                spy['rating'] = input("Enter your rating: ")
                # Conditions for displaying comments according to the spy['rating']
                if spy['rating']>4.5:
                    print("Great ace!\n")
                elif spy['rating'] >3.5 and spy['rating'] <= 4.5:
                    print("You are one of the good ones.\n")
                elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
                    print("You can always do better.\n")
                else:
                    print("We can always use somebody to help in the office.\n")

                # Default Value
                spy_is_online = True
                # Using placeholders(%s,%d,etc.)
                print "Authentication complete! %s, Welcome to SPY COMMUNITY... \nAge: %d and Rating of: %.1f\nProud to have you onboard !" %(spy['name'],spy['age'],spy['rating'])

                # Calling function to start chat application
                start_chat(spy['name'], spy['age'], spy['rating'])
            else:
                # Age not within the specified limits
                print("Sorrry! Age inappropriate to become a spy... ")
        else:
            # Salutation not within the specified limits
            print("Invalid salutation!")
    else:
        # Name too small
        print("Invalid name! Enter a 2 letter name atleast ")
