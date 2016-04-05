import random
n = raw_input ("What is your name ?")
#Asks the user it's name.
q = input ("What is the highest value ?")
#Asks the user what's the hihest number they wanna guess up to. 
g = input ("What number do you think it is ?")
#Asks the user what their guess is.
r = random.randint (1,r)
#Computer chooses a random number between 1 and the highest value.
while g != r:
    #starting a while loop
    if g < r:
        #An if statement saying if g is not equal to r then print too low. 
        print ("Too low!")
        g = input ("What number do you think it is ?")
        #asks the user the question again.
    elif g > r:
        print ("Too high!")
        #Else if g is greater than r print too high. 
        g = input ("What number do you think it is ?")
        #Ask the user the question again. 
print "You got it!"
#print you got it, if the user gets the answer right. 
