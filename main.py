# Importing spy_details
from spy_details import spy

# Importing steganography library for encoding and decoding
from steganography.steganography import Steganography

# Importing datetime library
from datetime import datetime

# Start greeting
print ("Hello!!!")
print('******* << Welcome to SpyChat >> *******')
# Using escape sequence
print ("Let\'s get started...\n")

# List used for storing old status messages
STATUS_MESSAGES = ['I\'m busy', 'Available', 'Loving Life!', 'Sleeping']

friends = [{'name': 'Himanshu','salutation': 'Mr.','age': 22,'rating': 9.0, 'chats' : []},{'name': 'Shruti','salutation': 'Ms.','age': 23,'rating': 7.7,'chats' : []}]

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

# Declaring function for adding friend
def add_friend():
    # Using Dictionary type variable
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats' : []
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

# Declaring function for selecting the friend to whom message will be sent
def select_a_friend():
    serial_number = 1
    for friend in friends:
        print str(serial_number) + ". " + friend['name']
        serial_number = serial_number + 1
    user_selected_friend = input("\nSelect your friend: ")
    user_index = user_selected_friend - 1
    return user_index

def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("\nWhat is the name of your image? ")
    text = raw_input("What is your secret message? ")
    output_path = "output.jpg"
    Steganography.encode(original_image,output_path,text)
    new_chat = {
        'message' : text,
        'time' : datetime.now(),
        'sent_by_me' : True
    }
    # Saving chat
    friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"


def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file? ")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        'message': secret_text,
        'time': datetime.now(),
        'sent_by_me': False
    }
    # Saving chat
    friends[sender]['chats'].append(new_chat)
    print "Your secret message is: " + secret_text

# Declaring function
def start_chat(spy_name,spy_age,spy_rating):
    # Initializing current status message with None
    current_status_message = None
    # Initializing show_menu variable with true value
    show_menu = True
    while show_menu:
        # Displaying options to select different features of application
        menu_choice = input("\nWhat do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Send a secret message\n 4. Read a secret message\n 0. Exit\n")
        if menu_choice == 1:
            current_status_message = add_status(current_status_message)  # add_status function is called with current status message as parameter
            # Checking whether some status is there or not
            if len(current_status_message)>= 1:
                # If user doesn't select anything
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
            send_message()
        elif menu_choice == 4:
            read_message()
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
