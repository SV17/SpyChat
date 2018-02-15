# Importing spy_details
from spy_details import spy

# Importing classes(Spy, ChatMessage) and list(friends) from spy_details
from spy_details import Spy, ChatMessage, friends

# Importing steganography library for encoding and decoding
from steganography.steganography import Steganography

# Importing csv file
import csv

# Importing termcolor to get a colourful output
from termcolor import colored

# Start greeting
print ("Hello!!!")
print(colored("******* << Welcome to SpyChat >> *******" , "magenta"))
# Using escape sequence
print ("Let\'s get started...\n")


#=================================================================================================================================

# Defining  load friends function to load the friends when application starts
def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            name = row[0]
            age = row[1]
            rating = row[2]
            online = row[3]
            spy = Spy(name, age, rating, online)
            friends.append(spy)



#===================================================================================================================================

# Defining  load friends function to load the friends when application starts
def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        reader = list(csv.reader(chats_data))

        for row in reader[1:]:
            sender = row[0]
            message_sent_to = row[1]
            text = row[2]
            time = row[3]
            sent_by_me = row[4]
            #chats = ChatMessage(sender, message_sent_to, text, time, sent_by_me)
            chats.append(new_chat)

#====================================================================================================================================

# List used for storing old status messages
STATUS_MESSAGES = ['I\'m busy', 'Available', 'Loving Life!', 'Sleeping',"Diamonds are forever", "SAD!"]

#=====================================================================================================================================

# Declaring function for adding status
def add_status(current_status_message):
    # Checking whether any old status is set
    if current_status_message != None:
        print (colored("Your current status message is: " + current_status_message ,"cyan"))     # Displays current status message
    else:
        # When no old status is set
        print (colored("\nYou don't have any status currently!","red"))

    # Asking whether we want to select any old status or not
    status = raw_input(colored("\nDo you want to select from old statuses? (Y/N) : ","blue"))
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
            user_selection = input(colored("\nWhich one do you want to select? ","cyan"))
            # Value selected by user should not exceed list's length
            if len(STATUS_MESSAGES)>=user_selection:
                new_status = STATUS_MESSAGES[user_selection - 1]
            else:
                # If user selects a value greater than the length of status messages
                print(colored("Invalid selection!","red"))
            # Returning the status
            return new_status

        elif status.upper() == 'N':
            new_status = raw_input(colored("Enter your new status: ","blue"))
            # Checking whether user has entered something or not
            if len(new_status) > 1:
                # Appending the new status to the list
                STATUS_MESSAGES.append(new_status)
            else:
                # When user doesn't enter anything
                print(colored("Please enter something atleast...","red"))
            # Returning the new status entered by the user
            return new_status
        else:
            print(colored("Invalid entry!","red"))

    else:
        # When user presses enter without choosing anything
        set_status = 'No status'
        return set_status

#=========================================================================================================================================

# Declaring function for adding friend
def add_friend():
    # Using Class
    new_friend = Spy("",0,0.0, True)
    # Taking values for new friend
    new_friend.name = raw_input(colored("What is the name of friend? ","blue"))
    new_friend.salutation = raw_input(colored("What should we call you(Mr. or Ms.)?  ","blue"))
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = input(colored("Age of friend: ","blue"))
    new_friend.rating = input(colored("Rating of friend: ","blue"))
    # Validating name,age and spy rating
    if len(new_friend.name) >= 3 and 50>=new_friend.age>=12 and new_friend.rating>=spy.rating:
        # Appending new friend to list
        friends.append(new_friend)
        print(colored("Friend is added!","magenta"))
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.age, new_friend.rating, new_friend.is_online])
    else:
        # If validation fails
        print (colored("\nFriend cannot be added! ","red"))
    # Returning the number of friends
    return len(friends)

#=========================================================================================================================================


# Declaring function for selecting the friend to whom message will be sent
def select_a_friend():
    serial_number = 1
    # Using loop
    for friend in friends:                                    # friend is a local variable of "for" loop
        # Concatenating serial number and name
        print str(serial_number) + ". " + friend.name
        serial_number = serial_number + 1
    # Asking user to select one of the friends
    user_selected_friend = input(colored("\nSelect your friend: ","blue"))
    user_index = user_selected_friend - 1
    # Returning the index of selected friend
    return user_index

#======================================================================================================================================

# Declaring function for sending message
def send_message():
    # Selecting a friend to send message
    friend_choice = select_a_friend()
    # Asking for name of image to be encoded with secret message
    original_image = raw_input(colored("\nWhat is the name of your image? ","blue"))
    # Asking for the secret message
    text = raw_input(colored("What is your secret message? ","blue"))
    # Storing the encoded message(image+secret message) in a variable
    output_path = "output.jpg"
    # Using encode() funtion from Steganography library to encrypt the message
    Steganography.encode(original_image,output_path,text)
    new_chat = ChatMessage(text,True)

    with open('chats.csv', 'ab') as chats_data:
        write = csv.writer(chats_data)
        write.writerow([spy.name , friends[friend_choice].name , new_chat.message , new_chat.time , new_chat.sent_by_me])

    # The message will be appended in ChatMessage class
    friends[friend_choice].chats.append(new_chat)
    print (colored("Your message encrypted successfully!","cyan"))

#==============================================================================================================================

def send_help_message():
    # Selecting a friend
    friend_choice = select_a_friend()
    # The response
    text = colored("Don't worry... I'm coming to save you!","magenta")
    # Creating new chat
    new_chat = ChatMessage(colored(text,"red"),False)
    # Appending the chat
    friends[friend_choice].chats.append(new_chat)

#==============================================================================================================================

# Declaring funtion for reading the secret message
def read_message():
    # Selecting the friend
    sender = select_a_friend()
    # Asking the name of image from where secret message is to be decoded
    output_path = raw_input(colored("What is the name of the file you want to decode? ","blue"))

    try:
        # Using decode() funtion with file name of encrypted message as parameter
        secret_text = Steganography.decode(output_path)
        print (colored("Your secret message is:","cyan"))
        print (colored(secret_text,"blue"))

        # Converting secret_text to uppercase
        new_text = (secret_text.upper()).split()

        # Checking emergency templates for help
        if "SOS" in new_text or "SAVE" in new_text or "ACCIDENT" in new_text or "HELP" in new_text or "RESCUE" in new_text:

            # Emergency alert
            print colored("!", 'grey', 'on_yellow'),
            print colored("!", 'grey', 'on_yellow'),
            print colored("!", 'grey', 'on_yellow')

            print colored("The friend who sent this message needs your help!", "green")
            print colored("Please help your friend by sending a helping message...\n", "green")
            print colored("Select the friend to send a helping message.\n", "green")

            # Calling send_help_message() function to send the help
            send_help_message()

            # Message sent successfully
            print colored("You just sent a message to help your friend! ", "cyan")

            # Creating new chat
            new_chat = ChatMessage(secret_text, False)
            # Appending to chats
            friends[sender].chats.append(new_chat)

        # If there is no emergency messages or call for help
        else:
            new_chat = ChatMessage(secret_text, False)
            # Appending
            friends[sender].chats.append(new_chat)
            print colored("Your secret message has been saved.\n", 'cyan')

    # No message found exception
    except TypeError:
        print colored("Nothing to decode from the image...\n Sorry! There is no secret message", 'red')


#=================================================================================================================================


def read_chat_history():
    friend_choice = select_a_friend()

    print '\n'

    for chat in friends[friend_choice].chats:
        if chat.sent_by_me:
            print (colored(str(chat.time.strftime("%d %B %Y %A %H : %M")) + ",","blue")),
            # The message is printed in red
            print (colored("You : ","red")),
            # Default colour black for text
            print str(chat.message)

        # Message sent by another spy
        else:
            # Date and time is printed in blue
            print (colored(str(chat.time.strftime("%d %B %Y %A %H : %M"))+ "," ,"blue")),
            # The message is printed in red
            print (colored(str(friends[friend_choice].name) + " : ", "red")),
            # Black is by default
            print str(chat.message)

#====================================================================================================================================

# Declaring function for starting chat
def start_chat(spy_name,spy_age,spy_rating):
    # Initializing current status message with None
    current_status_message = None
    # Initializing show_menu variable with true value
    show_menu = True
    while show_menu:
        # Displaying options to select different features of application
        menu_choice = input(colored("\nWhat do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Send a secret message\n 4. Read a secret message\n 5. Read chats from a user\n 0. Close application\n","magenta"))
        if menu_choice == 1:
            current_status_message = add_status(current_status_message)  # add_status function is called with current status message as parameter
            # Checking whether some status is there or not
            if len(current_status_message)>= 1:
                # If user doesn't select anything
                if current_status_message == 'No status':
                    print(colored("You didn't select the status correctly!","red"))
                else:
                    # Prints the value returned from add_status function
                    print(colored( "Your status has been set to: " + current_status_message , "green"))
            else:
                print (colored("You didn't select the status correctly!","red"))
        elif menu_choice == 2:
            number_of_friends = add_friend()    # Calling the add_friend() function for adding friend
            print (colored("You have " + str(number_of_friends) + " friend/friends." ,"green"))   # Displaying the number of friend/friends
        elif menu_choice == 3:
            send_message()              # Calling the send_message() function for sending the secret message
        elif menu_choice == 4:
            read_message()              # Calling the read_message() function for reading the secret message
        elif menu_choice == 5:
            read_chat_history()                # Calling the read_chat_history() function for reading the chats
        elif menu_choice == 0:          # For exitting from menu
            show_menu = False
        else:
            # If user chooses something other than menu choices
            print(colored("Invalid choice!!!","red"))


# Asking the spy whether to continue with existing values or create a new user
spy_exist = raw_input(colored("Are you an existing user?(Y or N) : ","blue"))

# Validating input
if spy_exist.upper() == 'Y':        # .upper() converts from any case to upper case

    # Existing user
    print(colored("We already have your details!","cyan"))

    # Calling function to start chat application
    start_chat(spy.name, spy.age, spy.rating)
elif spy_exist.upper() == 'N':
    # New user
    spy.name = raw_input(colored("\nWhat is your spy name? ","blue"))

    # Checking whether spy has entered any name or not
    if len(spy.name)>=2:
        print (colored("Welcome " +spy.name + ", Glad to meet you!","red"))
        # Asking for salutation
        spy.salutation = raw_input(colored("What should we call you(Mr. or Ms.)? " ,"blue"))

        # Validating salutation
        if len(spy.salutation)>0:

            # Concatenating salutation and name of spy
            spy.name = spy.salutation + " " + spy.name
            print (colored("Alright " + spy.name + ". I'd like to know a little bit more about you..." , "red"))
            # Asking for age
            spy.age = input(colored("Enter your age: ","blue"))
            # Age cannot be less than 12 and greater than 50
            # Nested if
            if spy.age>=12 and spy.age<50:
                print (colored("Your age is fine to become a spy!\n ","magenta"))
                # Asking for rating
                spy.rating = input(colored("Enter your rating: ","blue"))
                # Conditions for displaying comments according to the spy rating
                if spy.rating>4.5:
                    print(colored("Great ace!\n","magenta"))
                elif spy.rating >3.5 and spy.rating <= 4.5:
                    print(colored("You are one of the good ones.\n","magenta"))
                elif spy.rating >= 2.5 and spy.rating <= 3.5:
                    print(colored("You can always do better.\n","red"))
                else:
                    print(colored("We can always use somebody to help in the office.\n","red"))

                # Default Value
                spy_is_online = True
                # Using placeholders(%s,%d,etc.)
                print "Authentication complete! %s, Welcome to SPY COMMUNITY... \nAge: %d and Rating of: %.2f\nProud to have you onboard !" %(spy.name,spy.age,spy.rating)

                # Calling function to start chat application with spy name, spy age and spy rating as parameters
                start_chat(spy.name, spy.age, spy.rating)
            else:
                # Age not within the specified limits
                print(colored("Sorrry! Age inappropriate to become a spy... ","red"))
        else:
            # Salutation not within the specified limits
            print(colored("Invalid salutation!","red"))
    else:
        # Name too small
        print(colored("Invalid name! Enter a 2 letter name atleast ","red"))