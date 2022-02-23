tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

1. Print a list of uncompleted tasks

# def uncompleted_tasks(list):
#         to_complete = []

#         for task in list:
#             if task["completed"] == False:
#                 to_complete.append(task)

#         return to_complete

# print(uncompleted_tasks(tasks))

2. Print a list of completed tasks

# def completed_tasks(list):
#         all_complete = []

#         for task in list:
#             if task["completed"] == True:
#                 all_complete.append(task)

#         return all_complete

# print(completed_tasks(tasks))

3. Print a list of all task descriptions

# def description_tasks(list):
#     all_tasks = []

#     for task in list:
#         all_tasks.append(task["description"])

#     return all_tasks

# print(description_tasks(tasks))


4. Print a list of tasks where time_taken is at least a given time

# def given_time(list):
#     short_activity= []

#     given_time = 25
#     for task in list:
#         if task["time_taken"] >= given_time:

#             short_activity.append(task["description"])

#     return short_activity

# print(given_time(tasks))

5. Print any task with a given description

# def given_description(list):
    
#     given_description = input("What is your task? ")
#     for task in list:
#         if task["description"] == given_description:

#             return task 

# print(given_description(tasks))

6. Given a description update that task to mark it as complete.

# def given_description(list):
    
#     given_description = input("What is your task? ")
#     for task in list:
#         if task["description"] == given_description:

#             task["completed"] = True
#             break 
#     print(tasks)
# print(given_description(tasks))

7. add a task to the list
def add_to_list(list, task):
    list.append(task)