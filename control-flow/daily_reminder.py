task = input("Enter the task description: ")

priority = input("Enter the priority (high, medium , low): "). lower()

time_bound = input("Enter the time bound in minutes: ").lower()

match priority:
    case "high":
        reminder = f"High priority reminder: task: '{task}'"

    case "medium":
        reminder = f"Medium priority reminder: task: '{task}'"
    case "low":
        reminder = f"Low priority reminder: task: '{task}'"    
    case _:
        reminder = "priority not recognized"

if time_bound == "yes":
    reminder += " that requires a time immeddiate attention today!"

elif time_bound == "no":
    reminder += " that can be complete later."   

    print(reminder)


