print ("Hello!!!")
print('Welcome to SpyChat')
print ("Let's get started")
#Profile of a spy
spy_name = raw_input("What is your spy name? ")
if len(spy_name)>=3:    #Validation for spy name
    print "Welcome " +spy_name+ ", Glad to meet you!"
    spy_salutation = raw_input("What should we call you (Mr. or Ms.)?" )
    if len(spy_salutation)>0:      #Validation for salutation
        spy_name = spy_salutation + " " + spy_name     #Concatenation
        print "Alright " + spy_name + ". I'd like to know a little bit more about you..."
        spy_age = input("Enter your age: ")
        if spy_age>=12 and spy_age<50:
            print ("Your age is fine to be a spy! ")
            spy_rating = input("Enter your rating: ")
            if spy_rating>=7.5:
                print("Excellent spy")
            elif spy_rating>=5.5 and spy_rating<7.5:
                print("Good spy")
            elif spy_rating>=3.5 and spy_rating<5.5:
                print("Average spy")
            else:
                print("Bad spy")
            spy_is_online = True
            print "Authentication complete! Welcome " + spy_name + "... \nAge: " + str(spy_age) + " and Rating of: " + str(spy_rating) + " \nProud to have you onboard !"
        else:
            print("Sorrry! Age inappropriate to be a spy ")
    else:
        print("Invalid salutation!")
else:
    print("Invalid name! Enter a 3 letter name atleast ")
