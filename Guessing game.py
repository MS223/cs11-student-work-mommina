import random
n = raw_input ("What is your name ?")
q = input ("What is the highest value ?")
g = input ("What number do you think it is ?")
r = random.randint (1,q)
while g != r:
    if g < r:
        print ("Too low!")
        g = input ("What number do you think it is ?")
    elif g > r:
        print ("Too high!")
        g = input ("What number do you think it is ?")
print "You got it!"
