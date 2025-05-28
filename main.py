from modules import functions as fn

print("Welcome to TodoList app!")
user_prompt = "Enter a todo: "
action_prompt = "Type add, show, edit, complete or exit: "
ask_prompt = "Number of the todo to edit: "
todos = []
stop = False

while not stop:
    action = input(action_prompt).strip()
    if action.startswith("add"):
        todo = action[4:] + "\n"

        # read from file
        todos = fn.get_todos()
        todos.append(todo)

        # write to file
        fn.write_todos(todos)

    elif action.startswith("show"):
        # read from file
        todos = fn.get_todos()

        if todos.__len__():
            for i, item in enumerate(todos):
                print(f"{i + 1}. {item.title().strip("\n")}")
        else:
            print("You have no todos, add one")

    elif action.startswith("edit"):
        try:

            number = int(action[5:])
            print(f"Your todo: {todos[number - 1].strip("\n")} ")
            todos[number - 1] = input("Reenter todo: ") + "\n"
            fn.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number")
            continue
    elif action.startswith("complete"):
        try:
            # read from file
            todos = fn.get_todos()

            number = int(action[9:])
            removed_todo = todos[number - 1]
            todos.remove(todos[number - 1])

            fn.write_todos(todos)

            print(f"Todo: {removed_todo.strip("\n")} removed")

        except IndexError:
            print("There is no item with that number")
            continue

        except ValueError:
            print("Your command is not valid")
            continue

    elif action.startswith("exit"):
        stop = True
    else:
        print("Wrong command!")

print("Bye!")
