
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"

        else:
            reminder += ". You can complete it when you have some time."

    case "medium":
        reminder = f"'{task}' is a medium priority task"

        if time_bound == "yes":
            reminder += " that requires attention soon!"

        else:
            reminder += ". Consider completing it when you can."

    case "low":
        reminder = f"'{task}' is a low priority task"

        if time_bound == "yes":
            reminder += " but still deserves some attention today!"

        else:
            reminder += ". You can complete it whenever you have free time."
    case _:
        reminder = "Invalid priority level entered."


print(f"Reminder: {reminder}")
