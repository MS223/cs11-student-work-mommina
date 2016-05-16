my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print my_dictionary
print my_dictionary['dog']
print my_dictionary.get('dog')
print 'cat' in my_dictionary
print 'monkey' in my_dictionary
print my_dictionary ['chair']

# 1. what prints ?
# {'car': 'automobile', 'chair': 'furniture piece for sitting', 'dog': 'a domestic canine', 'cat': 'a domestic feline'}
# a domestic canine
# a domestic canine
# True
# False
# 2. A list, defining/naming the list. 
# 4. It won't work because kittens isn't a word in "my_dictionary"
