from modules import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type in a to- do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box,add_button],[exit_button]],
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
        case "Exit" | sg.WIN_CLOSED:
            break
window.close()