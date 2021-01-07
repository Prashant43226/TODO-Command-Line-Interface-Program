import sys
import os
import datetime as dt

#default output

def default():
    try:
        if os.stat("todo.txt").st_size > 0:
            read_from_file = open("todo.txt", "r")
            task = read_from_file.readlines()
            n = len(task)
            if n > 0:
                task_text = ""
                for i in range(n, 0, -1):
                    task_text += f'{[i]} ' + task[i - 1]
                print(sys.stdout.buffer.write(task_text.encode('utf8')))
                read_from_file.close()
        else:
            print("There are no pending todos!")
    except OSError:
        print("There are no pending todos!")

#add a task

def add_task(task):
    add_to_file = open("todo.txt", 'a')
    add_to_file.write(task + '\n')
    print("Added todo: " + f'"{task}"')
    add_to_file.close()


#completed tasks

def done_task(task_number):
    read_from_file = open("todo.txt", "r")
    done_file = open("done.txt", "a")
    task = read_from_file.readlines()
    read_from_file.close()
    if 0 < int(task_number) <= len(task):
        read_from_file = open("todo.txt", "w")
        removed_task = task.pop(int(task_number) - 1)
        print(f"Marked todo #{task_number} as done.")
        done_file.write(removed_task)
        read_from_file.writelines(task)
        read_from_file.close()
        done_file.close()
    else:
        print(f"Error: todo #{task_number} does not exist.")

#delete a task

def delete_task(task_number):
    read_from_file = open("todo.txt", "r")
    task = read_from_file.readlines()
    read_from_file.close()
    if 0 < int(task_number) <= len(task):
        print(f"Deleted todo #{task_number}")
        read_from_file = open("todo.txt", "w")
        task.pop(int(task_number) - 1)
        read_from_file.writelines(task)
        read_from_file.close()
    else:
        print(f"Error: todo #{task_number} does not exist. Nothing deleted.")


#final report

def report():
    done = open("done.txt", "r")
    remaining = open("todo.txt", "r")
    remaining_tasks = remaining.readlines()
    done_tasks = done.readlines()
    print(
        f"{dt.datetime.today().strftime('%Y-%m-%d')} Pending : {len(remaining_tasks)} Completed : {len(done_tasks)}")


n = len(sys.argv) - 1
sys.argv.pop(0)

help_text = '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''

if n == 0 or sys.argv[0] == 'help':
    print(sys.stdout.buffer.write(help_text.encode('utf8')))

if n > 0:
    if sys.argv[0] == 'add':
        if n == 1:
            print("Error: Missing todo string. Nothing added!")
        else:
            add_task(sys.argv[1])
    if sys.argv[0] == 'ls':
        default()
    if sys.argv[0] == 'del':
        if n == 1:
            print("Error: Missing NUMBER for deleting todo.")
        else:
            delete_task(sys.argv[1])
    if sys.argv[0] == 'done':
        if n == 1:
            print("Error: Missing NUMBER for marking todo as done.")
        else:
            done_task(sys.argv[1])
    if sys.argv[0] == 'report':
        report()