task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()


while priority not in ['high', 'medium', 'low']:

    print("Invalid priority. Please enter high, medium, or low.")

    priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ['yes', 'no']:

    print("Invalid input. Please answer 'yes' or 'no'.")

    time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
        
    case 'medium':
        reminder = f"'{task}' is a medium priority task"

    case 'low':
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

if time_bound == 'yes':
    reminder = f"Reminder: {reminder} that requires immediate attention today!"

else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."


print(reminder)
