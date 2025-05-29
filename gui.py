from modules import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type in a to- do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=fn.get_todos(), key="todos",
                      enable_events=True, size=(45, 5))
edit_button = sg.Button("Edit")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [exit_button], [list_box, edit_button]],
                   font = ('Helvetica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = fn.get_todos()
            todos.append(values['todo'] + "\n")
            fn.write_todos(todos)
            window["todos"].update(todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = fn.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fn.write_todos(todos)
            window["todos"].update(todos)

        case "todos":
            window['todo'].update(values['todos'][0])

        case "Exit" | sg.WIN_CLOSED:
            break
window.close()