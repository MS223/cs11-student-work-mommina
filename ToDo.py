question = raw_input("What would you like to do?")
day = raw_input ("What day ?")
days_of_week = {
"monday":[],
"tuesday":[],
"wednesday":[],
"thursday":[],
"friday":[],
"saturday":[],
"sunday":[]
}
def add():
    days_of_week[day].append(question)
add()
print days_of_week

# trying to get the computer to store the value which is the answer given by
# someone so that when I print Print days of week it shows that I have something
# to do on whatever day that is chosen.
