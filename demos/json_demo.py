import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")  # fake data from a server
todos = json.loads(response.text)  # deserializes the text attribute of the JSON object into a Python list

"""
print(todos == response.json())

print(type(todos))

print(todos[:10])  # look at first 10 items in todos

print(todos)
"""

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)  # connects each user name with the string " and "

s = "s" if len(users) > 1 else ""
# print(top_users)
# print(f"user{s} {max_users} completed {max_complete} TODOs")


# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count  # makes sure todo is completed and has a max count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))  # filters only the todos that should be kept
    json.dump(filtered_todos, data_file, indent=2)  # dumps filtered todos to a .json file