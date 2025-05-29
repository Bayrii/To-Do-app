import streamlit as st
from modules import functions as fn

todos = fn.get_todos()

def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)


st.title("🚀 Launch Your Day with Purpose")
st.subheader("Your tasks, tracked and tackled.")
st.write("This app helps you break big goals "
         "into small wins — one task at a time.")

with st.container(height=400):
    for todo in todos:
        st.checkbox(todo)

st.text_input(label='Enter a todo',
              placeholder="Add new todo ...",
              on_change=add_todo, key="new todo")