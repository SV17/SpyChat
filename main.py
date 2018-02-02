print ("Hello!!!")
print('Welcome to SpyChat')
print ("Let's get started")
#Profile of a spy
spy_name = raw_input("What is your spy name? ")
if len(spy_name)>=2:    #Validation for spy name
    print "Welcome " +spy_name+ ", Glad to meet you!"
    spy_salutation = raw_input("What should we call you (Mr. or Ms.)?" )
    if len(spy_salutation)>0:      #Validation for salutation
        spy_name = spy_salutation + " " + spy_name     #Concatenation
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
            spy_is_online = True
            print "Authentication complete! Welcome %s... \nAge: %d and Rating of: %.2f\nProud to have you onboard !" %(spy_name,spy_age,spy_rating)
        else:
            print("Sorrry! Age inappropriate to be a spy ")
    else:
        print("Invalid salutation!")
else:
    print("Invalid name! Enter a 3 letter name atleast ")
