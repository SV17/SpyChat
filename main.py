# Importing spy_details
from spy_details import spy

# Importing classes(Spy, ChatMessage) and list(friends) from spy_details
from spy_details import Spy, ChatMessage, friends

# Importing steganography library for encoding and decoding
from steganography.steganography import Steganography


# Start greeting
print ("Hello!!!")
print('******* << Welcome to SpyChat >> *******')
# Using escape sequence
print ("Let\'s get started...\n")

# List used for storing old status messages
STATUS_MESSAGES = ['I\'m busy', 'Available', 'Loving Life!', 'Sleeping',"Diamonds are forever", "SAD!"]

# Declaring function for adding status
def add_status(current_status_message):
    # Checking whether any old status is set
    if current_status_message != None:
        print "Your current status message is: " + current_status_message     # Displays current status message
    else:
        # When no old status is set
        print"\nYou don't have any status currently!"

    # Asking whether we want to select any old status or not
    status = raw_input("\nDo you want to select from old statuses? (Y/N) : ")
    # Checking whether user has entered anything or not
    if len(status)>= 1:                     # len() function returns the length
        if status.upper() == 'Y':           # upper() function converts from any case to upper case
            # Initializing serial_number variable with 1
            serial_number = 1
            # Displaying old statuses from list
            for old_status in STATUS_MESSAGES:                 # old_status is a local variable of "for" loop
                # Concatenating serial number with old status
                print str(serial_number) + ". " + old_status
                # Incrementing serial number each time to display all statuses
                serial_number = serial_number + 1
            # Asking the user to select one of the displayed statuses
            user_selection = input("\nWhich one do you want to select? ")
            # Value selected by user should not exceed list's length
            if len(STATUS_MESSAGES)>=user_selection:
                new_status = STATUS_MESSAGES[user_selection - 1]
            else:
                # If user selects a value greater than the length of status messages
                print("Invalid selection!")
            # Returning the status
            return new_status

        elif status.upper() == 'N':
            new_status = raw_input("Enter your new status: ")
            # Checking whether user has entered something or not
            if len(new_status) > 1:
                # Appending the new status to the list
                STATUS_MESSAGES.append(new_status)
            else:
                # When user doesn't enter anything
                print("Please enter something atleast...")
            # Returning the new status entered by the user
            return new_status
        else:
            print("Invalid entry!")

    else:
        # When user presses enter without choosing anything
        set_status = 'No status'
        return set_status

# Declaring function for adding friend
def add_friend():
    # Using Class
    new_friend = Spy("",0,0.0)
    # Taking values for new friend
    new_friend.name = raw_input("What is the name of friend? ")
    new_friend.salutation = raw_input("What should we call you(Mr. or Ms.)?  ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = input("Age of friend: ")
    new_friend.rating = input("Rating of friend: ")
    # Validating name,age and spy rating
    if len(new_friend.name) >= 3 and 50>=new_friend.age>=12 and new_friend.rating>=spy.rating:
        # Appending new friend to list
        friends.append(new_friend)
    else:
        # If validation fails
        print "\nFriend cannot be added! "
    # Returning the number of friends
    return len(friends)

# Declaring function for selecting the friend to whom message will be sent
def select_a_friend():
    serial_number = 1
    # Using loop
    for friend in friends:                                    # friend is a local variable of "for" loop
        # Concatenating serial number and name
        print str(serial_number) + ". " + friend.name
        serial_number = serial_number + 1
    # Asking user to select one of the friends
    user_selected_friend = input("\nSelect your friend: ")
    user_index = user_selected_friend - 1
    # Returning the index of selected friend
    return user_index

# Declaring function for sending message
def send_message():
    # Selecting a friend to send message
    friend_choice = select_a_friend()
    # Asking for name of image to be encoded with secret message
    original_image = raw_input("\nWhat is the name of your image? ")
    # Asking for the secret message
    text = raw_input("What is your secret message? ")
    # Storing the encoded message(image+secret message) in a variable
    output_path = "output.jpg"
    # Using encode() funtion from Steganography library to encrypt the message
    Steganography.encode(original_image,output_path,text)
    new_chat = ChatMessage(text,True)
    # The message will be appended in ChatMessage class
    friends[friend_choice].chats.append(new_chat)
    print "Your message encrypted successfully!"

# Declaring funtion for reading the secret message
def read_message():
    # Selecting the friend
    sender = select_a_friend()
    # Asking the name of image from where secret message is to be decoded
    output_path = raw_input("What is the name of the file? ")
    # Using decode() funtion with file name of encrypted message as parameter
    secret_text = Steganography.decode(output_path)
    print "Your secret message is: " + secret_text
    # Adding the chat to sender
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)      # Appending the message to existing list of messages

# Declaring function for starting chat
def start_chat(spy_name,spy_age,spy_rating):
    # Initializing current status message with None
    current_status_message = None
    # Initializing show_menu variable with true value
    show_menu = True
    while show_menu:
        # Displaying options to select different features of application
        menu_choice = input("\nWhat do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Send a secret message\n 4. Read a secret message\n 5. Read chats from a user\n 0. Close application\n")
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
            number_of_friends = add_friend()    # Calling the add_friend() function for adding friend
            print "You have " + str(number_of_friends) + " friend/friends."     # Displaying the number of friend/friends
        elif menu_choice == 3:
            send_message()              # Calling the send_message() function for sending the secret message
        elif menu_choice == 4:
            read_message()              # Calling the read_message() function for reading the secret message
        elif menu_choice == 5:
            print ("Reading chats...")     #Module not created (Classes not held yet)
        elif menu_choice == 0:          # For exitting from menu
            show_menu = False
        else:
            # If user chooses something other than menu choices
            print("Invalid choice!!!")


# Asking the spy whether to continue with existing values or create a new user
spy_exist = raw_input("Are you an existing user?(Y or N) : ")

# Validating input
if spy_exist.upper() == 'Y':        # .upper() converts from any case to upper case

    # Existing user
    print("We already have your details!")

    # Calling function to start chat application
    start_chat(spy.name, spy.age, spy.rating)
elif spy_exist.upper() == 'N':
    # New user
    spy.name = raw_input("\nWhat is your spy name? ")

    # Checking whether spy has entered any name or not
    if len(spy.name)>=2:
        print "Welcome " +spy.name + ", Glad to meet you!"
        # Asking for salutation
        spy.salutation = raw_input("What should we call you(Mr. or Ms.)? " )

        # Validating salutation
        if len(spy.salutation)>0:

            # Concatenating salutation and name of spy
            spy.name = spy.salutation + " " + spy.name
            print "Alright " + spy.name + ". I'd like to know a little bit more about you..."
            # Asking for age
            spy.age = input("Enter your age: ")
            # Age cannot be less than 12 and greater than 50
            # Nested if
            if spy.age>=12 and spy.age<50:
                print ("Your age is fine to become a spy!\n ")
                # Asking for rating
                spy.rating = input("Enter your rating: ")
                # Conditions for displaying comments according to the spy rating
                if spy.rating>4.5:
                    print("Great ace!\n")
                elif spy.rating >3.5 and spy.rating <= 4.5:
                    print("You are one of the good ones.\n")
                elif spy.rating >= 2.5 and spy.rating <= 3.5:
                    print("You can always do better.\n")
                else:
                    print("We can always use somebody to help in the office.\n")

                # Default Value
                spy_is_online = True
                # Using placeholders(%s,%d,etc.)
                print "Authentication complete! %s, Welcome to SPY COMMUNITY... \nAge: %d and Rating of: %.2f\nProud to have you onboard !" %(spy.name,spy.age,spy.rating)

                # Calling function to start chat application with spy name, spy age and spy rating as parameters
                start_chat(spy.name, spy.age, spy.rating)
            else:
                # Age not within the specified limits
                print("Sorrry! Age inappropriate to become a spy... ")
        else:
            # Salutation not within the specified limits
            print("Invalid salutation!")
    else:
        # Name too small
        print("Invalid name! Enter a 2 letter name atleast ")
