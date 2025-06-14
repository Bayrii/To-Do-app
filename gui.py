from modules import functions as fn
import FreeSimpleGUI as sg
import time

sg.theme("DarkBrown")

clock = sg.Text("", key = "clock")

label = sg.Text("Type in a to- do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=fn.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                            [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                           ],
                   font = ('Helvetica',20))
while True:
    event, values = window.read(timeout = 200)
    match event:
        case "Exit" | sg.WIN_CLOSED:
            break
        case "Add":
            todos = fn.get_todos()
            todos.append(values['todo'] + "\n")
            fn.write_todos(todos)
            window["todos"].update(todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fn.write_todos(todos)
                window["todos"].update(todos)
            except IndexError:
                sg.popup("Please select an item first.",font = ('Helvetica',20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = fn.get_todos()
                todos.remove(todo_to_complete)
                fn.write_todos(todos)
                window["todos"].update(values = todos)
                window["todo"].update(value = "")
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(values['todos'][0])

    window["clock"].update(value = time.strftime("%Y %b %d, %H:%M:%S"))


window.close()