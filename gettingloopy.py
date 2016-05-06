print "hello"[1:]
#takes out the first letter of the world hello and leaves ello.
print "hello"[:4]
#takes out the fourth letter from the world hello and leaves hell.
print "hello"[2:4]
#takes out the first, second and fourth letter and leaves ll.

print "github"[1:3]
print "hamburger"[3:]
print "dongle"[1:3]
print "snapchat"[1:4]

def fruit_pluralizer(lists_of_strings):
    for word in lists_of_strings:
        if  word [-1:] == "y":

