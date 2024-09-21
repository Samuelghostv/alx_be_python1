task = input("Please enter your task: ")

priority = input("Enter the task's priority (high, medium, low): ").lower()

time_bound = input("Is the task time-sensitive (yes or no)? ").lower()


while priority not in ['high', 'medium', 'low']:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Enter the task's priority (high, medium, low): ").lower()

while time_bound not in ['yes', 'no']:
    print("Invalid input. Please answer 'yes' or 'no'.")
    time_bound = input("Is the task time-sensitive (yes or no)? ").lower()

match priority:
    case 'high':
        reminder = f"Task: '{task}' is of high priority."
    case 'medium':
        reminder = f"Task: '{task}' is of medium priority."

    case 'low':
        reminder = f"Task: '{task}' is of low priority."
    case _:
        reminder = f"Task: '{task}' has an unknown priority."

if time_bound == 'yes':
    reminder += " It requires immediate attention today!"

print(reminder)

