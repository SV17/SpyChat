# Importing datetime library to show date and time of chat
from datetime import datetime

# Using Spy class to store values of Spy
class Spy:
  # Using constructor
  def __init__(self, name, age, rating):
    # Initializing the values
    self.name = name
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None

# For existing user
spy = Spy('Ms. Shikha Verma',22,7.7)

# Existing friends of spy
friend_one = Spy('Mr. Himanshu Dohan', 22, 7)
friend_two = Spy('Ms. Shruti Sharma', 23, 5.2)
friend_three = Spy('Ms. Ritu Saxena ', 25, 6.9)

# List for storing friends of spy
friends = [friend_one, friend_two, friend_three]

# Using ChatMessage class to store messages
class ChatMessage:
  # Using constructor
  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()  # now() function displays current date and time
    self.sent_by_me = sent_by_me