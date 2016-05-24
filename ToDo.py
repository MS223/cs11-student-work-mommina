days_of_week = {
"monday":[],
"tuesday":[],
"wednesday":[],
"thursday":[],
"friday":[],
"saturday":[],
"sunday":[]
}
def add(day,question):
    days_of_week[day].append(question)
# add()

def get(day,question):
    days_of_week[day].append(question)
# get()

def choice():
    user_choice = raw_input("How can I help you?")
    while user_choice != "exit":
        if user_choice == "get":
            day = raw_input ("What day ?")
            get(day)
        elif user_choice == "add":
            question = raw_input("What would you like to do?")
            day = raw_input ("what day?")
            add(day,question)
choice()


